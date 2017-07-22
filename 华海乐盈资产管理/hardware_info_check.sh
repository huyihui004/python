#!/bin/bash
#Date:20170206
#Author:Siman Chou
#Version:1.0
#Require:CentOS<7.0,Ubuntu
#Description:check hardware info,like cpu,memory,disk,SN...
#create two result file in /tmp,one like hardware_info.txt for human read,another like hardware_info.csv for import to db.

#检测是否是root用户
#if [ $(id -u) != "0" ]; then
#    printf "\e[42m\e[31mError: You must be root to run this install script.\e[0m\n"
#    exit 1
#fi

#判断系统版本
os=`cat /etc/issue | grep -E "(CentOS|Ubuntu)" | awk '{print $1}'`
if [ -z "$os" ];then
    cat /etc/issue | grep "Oracle" > /dev/null
	if [ $? = 0 ];then
	    os="OracleServer"
	fi
fi
if [ "$os" = "CentOS" ];then
    version=`cat /etc/issue | grep -E "(CentOS|Ubuntu)" | awk '{print $3}'`
elif [ "$os" = "Ubuntu" ];then
    version=`cat /etc/issue | grep -E "(CentOS|Ubuntu)" | awk '{print $2}'`
elif [ "$os" = "OracleServer" ];then
    version=`cat /etc/issue | grep "release" | awk '{print $5}'`
else
    version="Unknown"
fi
#echo $os
#echo $version

#定义不同操作系统的软件的安装方法
declare -A install_tool=(["CentOS"]="yum install -y " ["OracleServer"]="yum install -y " ["Ubuntu"]="sudo apt-get install -y ")

#安装必需软件
if [ "$os" = "CentOS" ];then
    dmidecode_install_result=`rpm -qa dmidecode`
	if [ -z "$dmidecode_install_result" ];then
        ${install_tool["CentOS"]} dmidecode >/dev/null 2>&1
	fi
	ftp_install_result=`rpm -qa ftp`
	if [ -z "$ftp_install_result" ];then
        ${install_tool["CentOS"]} ftp >/dev/null 2>&1
	fi
	megecli_install_result=`rpm -qa MegaCli`
	if [ -z "$megecli_install_result" ];then
	    wget -O /tmp/MegaCli-8.07.14-1.noarch.rpm --http-user=hhly --http-passwd=hhly2017 \
	    http://203.19.33.119:65432/MegaCli-8.07.14-1.noarch.rpm >/dev/null 2>&1
        rpm -ivh /tmp/MegaCli-8.07.14-1.noarch.rpm >/dev/null 2>&1
	fi
elif [ "$os" = "OracleServer" ];then
    dmidecode_install_result=`rpm -qa dmidecode`
	if [ -z "$dmidecode_install_result" ];then
        ${install_tool["OracleServer"]} dmidecode ftp >/dev/null 2>&1
	fi
	ftp_install_result=`rpm -qa ftp`
	if [ -z "$ftp_install_result" ];then
        ${install_tool["OracleServer"]} ftp >/dev/null 2>&1
	fi
	megecli_install_result=`rpm -qa MegaCli`
	if [ -z "$megecli_install_result" ];then
	    wget -O /tmp/MegaCli-8.07.14-1.noarch.rpm --http-user=hhly --http-passwd=hhly2017 \
	    http://203.19.33.119:65432/MegaCli-8.07.14-1.noarch.rpm >/dev/null 2>&1
        rpm -ivh /tmp/MegaCli-8.07.14-1.noarch.rpm >/dev/null 2>&1
	fi
elif [ "$os" = "Ubuntu" ];then
    dmidecode_install_result=`dpkg --get-selections | grep dmidecode | awk '{print $2}'`
	if [ "$dmidecode_install_result" != "install" ];then
        ${install_tool["Ubuntu"]} dmidecode >/dev/null 2>&1
	fi
	ftp_install_result=`dpkg --get-selections | grep ftp | awk '{print $2}'`
	if [ "$ftp_install_result" != "install" ];then
        ${install_tool["Ubuntu"]} ftp >/dev/null 2>&1
	fi
	megecli_install_result=`dpkg --get-selections | grep -i MegaCli | awk '{print $2}'`
	if [ "$megecli_install_result" != "install" ];then
	    wget -O /tmp/megacli_8.07.14-2_all.deb --http-user=hhly --http-passwd=hhly2017 \
	    http://203.19.33.119:65432/megacli_8.07.14-2_all.deb >/dev/null 2>&1
        sudo dpkg -i /tmp/megacli_8.07.14-2_all.deb >/dev/null 2>&1
	fi
fi


#查询公网/内网IP
ethlist=$(ip link | grep "state UP" | awk -F: '{print $2}' | sed 's/^[ \t]*//g')
nic_count=`printf "${ethlist}\n" | wc -l`
#echo $nic_count
lannic_tmp=/tmp/lannic_tmp.txt
lanip_tmp=/tmp/lanip_tmp.txt
if [ $nic_count -gt 1 ]; then
    for i in $ethlist;do
        ip_prefix=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/' | awk -F'.' '{print $1}'`
        if [ -n "$ip_prefix" ];then
		    if [[ $(printf "${ip_prefix}\n" | wc -l) -gt 1 ]]; then
			    ip_prefix=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/' | awk -F'.' '{print $1}' | head -1`
		        if [ "$ip_prefix" = "10" ];then
			        lan_nic=$i
                    lanip=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/' | sed 'N;s/\n/ /'`
					echo $lan_nic>>$lannic_tmp
					echo $lanip>>$lanip_tmp
    	        else
			        wan_nic=$i
    	            wanip=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/'`
			    	if [[ $(printf "${wanip}\n" | wc -l) -gt 1 ]]; then
			    	    wanip=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/' | sed 'N;s/\n/ /'`
    	        	fi
    	        fi
			else
			    if [ "$ip_prefix" = "10" ];then
			        lan_nic=$i
                    lanip=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/' | sed 'N;s/\n/ /'`
					echo $lan_nic>>$lannic_tmp
					echo $lanip>>$lanip_tmp
    	        else
			        wan_nic=$i
    	            wanip=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/'`
			    	if [[ $(printf "${wanip}\n" | wc -l) -gt 1 ]]; then
			    	    wanip=`ip -4 -f inet addr show $i | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/' | sed 'N;s/\n/ /'`
    	        	fi
    	        fi
			fi	
        fi
	done
else
    wan_nic=`echo $ethlist`
	wanip=`ip -4 -f inet addr show $wan_nic | grep 'inet' | sed 's/.*inet \([0-9\.]\+\).*/\1/'`
fi

lan_nic=`cat $lannic_tmp | sed 'N;s/\n/ /'`
lanip=`cat $lanip_tmp | sed 'N;s/\n/ /'`
rm $lanip_tmp
rm $lannic_tmp
#echo $lanip
#echo $wanip
#echo $lan_nic
#echo $wan_nic
lanmac_tmp=/tmp/lanmac_tmp.txt
if [ $nic_count -gt 1 ]; then
    if [[ $(echo $lan_nic | sed 's/ /\n/g' | wc -l) -gt 1 ]]; then
	    for i in $lan_nic;do
            lan_mac=`ip -4 -f link link show $i | grep link | awk '{print $2}'`
			echo $lan_mac>>$lanmac_tmp
		done
		wan_mac=`ip -4 -f link link show $wan_nic | grep link | awk '{print $2}'`
    else
	    lan_mac=`ip -4 -f link link show $lan_nic | grep link | awk '{print $2}'`
		echo $lan_mac>>$lanmac_tmp
		wan_mac=`ip -4 -f link link show $wan_nic | grep link | awk '{print $2}'`
	fi
else
    wan_mac=`ip -4 -f link link show $wan_nic | grep link | awk '{print $2}'`
fi

lan_mac=`cat $lanmac_tmp | sed 'N;s/\n/ /'`
rm $lanmac_tmp
#echo $wan_mac
#echo $lan_mac


#定义不同操作系统的软件的运行方法
declare -A soft_running=(["CentOS"]="" ["OracleServer"]="" ["Ubuntu"]="sudo ")

#序列号
serial_number=`${soft_running["$os"]} dmidecode -s system-serial-number`
#163RYC2
#设备厂商
manufacturer=`${soft_running["$os"]} dmidecode -s system-manufacturer | awk '{print $1}' | sed 's/,//g'`
#echo $manufacturer
#Dell
#型号
product_name=`${soft_running["$os"]} dmidecode -s system-product-name`
#R820
#CPU数量
processor_count=`${soft_running["$os"]} dmidecode -s processor-version | grep -v "Not Specified" | wc -l`
#2
#CPU型号
processor_version=`${soft_running["$os"]} dmidecode -s processor-version | grep -v "Not Specified" | head -1 | sed 's/^[ \t]*//g'`
#      Intel(R) Xeon(R) CPU E5-4603 v2 @ 2.20GHz
#      Intel(R) Xeon(R) CPU E5-4603 v2 @ 2.20GHz
#内存插槽
memory_slot=`${soft_running["$os"]} dmidecode -t memory | grep "Number Of Devices" | awk '{print $4}'`
#24
#已安装内存数量
memory_installed=`${soft_running["$os"]} dmidecode -t memory | grep "Size:" | sed 's/^[ \t]*//g' | grep -E "^Size:.*MB$" | wc -l`
#6
#每条内存容量
memory_size_by_single=`${soft_running["$os"]} dmidecode -t memory | grep "Size:" | sed 's/^[ \t]*//g' | grep -E "^Size:.*MB$" | awk '{print $2/1024}' | sort -u | wc -l`
if [[ $memory_size_by_single -gt 1 ]]; then
    memory_size_by_single=`${soft_running["$os"]} dmidecode -t memory | grep "Size:" | sed 's/^[ \t]*//g' | grep -E "^Size:.*MB$" | awk '{print $2/1024}' | sort -u | sed 'N;s/\n/ /'`
else
    memory_size_by_single=`${soft_running["$os"]} dmidecode -t memory | grep "Size:" | sed 's/^[ \t]*//g' | grep -E "^Size:.*MB$" | awk '{print $2/1024}' | sort -u`
fi
#8192
#8192
#8192
#8192
#8192
#8192
#echo $memory_size_by_single
#内存总量
memory_total_size_list=$(${soft_running["$os"]} dmidecode -t memory | grep "Size:" | sed 's/^[ \t]*//g' | grep -E "^Size:.*MB$" | awk '{print $2}')
let memory_total_size=`printf "${memory_total_size_list}\n" | awk '{sum += $1};END {print sum}'`/1024
#echo $memory_total_size

#Raid_info_tool
check_raid_tool=/opt/MegaRAID/MegaCli/MegaCli64

#Raid level
raid=`${soft_running["$os"]} $check_raid_tool -cfgdsply -aALL|grep "RAID Level"|cut -d: -f2 | sed 's/^[ \t]*//g'`

if [ ! "$raid" ];then
Raid_Level="N/A"
else
    case "$raid" in
        "Primary-1, Secondary-0, RAID Level Qualifier-0")
    	Raid_Level="1"
    	;;
    	"Primary-0, Secondary-0, RAID Level Qualifier-0")
    	Raid_Level="0"
    	;;
    	"Primary-5, Secondary-0, RAID Level Qualifier-3")
    	Raid_Level="5"
    	;;
    	"Primary-1, Secondary-3, RAID Level Qualifier-0")
    	Raid_Level="10"
    	;;
		*)
		Raid_Level="Unknown"
		;;
    esac
fi
#echo $Raid_Level

#硬盘容量
disk_size_by_single=`${soft_running["$os"]} lsblk | grep "disk" | grep "sd" | awk '{print $4}' | sed 's/G//g'`
if [[ $(printf "${disk_size_by_single}\n" | wc -l) -gt 1 ]]; then
    disk_size_by_single=`${soft_running["$os"]} lsblk | grep "disk" | grep "sd" | awk '{print $4}' | sed 's/G//g' | sed 'N;s/\n/ /'`
fi
#echo $disk_size_by_single

if [ "$Raid_Level" = "N/A" ];then
    #硬盘数量
	disk_count=`${soft_running["$os"]} lsblk | grep "disk" | grep "sd" | wc -l`
	#盘位
	disk_slot="N/A"
	#硬盘容量
	#disk_size_by_single=`${soft_running["$os"]} lsblk | grep "disk" | grep "sd" | awk '{print $3}'`
else	
    #硬盘数量
    disk_count=`${soft_running["$os"]} $check_raid_tool -PDList -aALL | grep "Slot Number" | wc -l`
    #2
    #盘位
    disk_slot=`${soft_running["$os"]} $check_raid_tool -PDList -aALL | grep "Slot Number" | awk '{print $3}'`
    #0
    #1
    #硬盘容量
    #disk_size_by_single=`${soft_running["$os"]} $check_raid_tool -PDList -aALL | grep "Raw Size" | awk '{print $3}' | head -1`
    #279.396
    #279.396
fi

#echo $disk_count

file_create_time=`date +%Y%m%d%H%M%S`

info_file_path=/tmp
info_file_name=hardware_info_`echo $wanip|sed 's/ /_/g'`"_"$file_create_time.txt
if [ ! -f $info_file_path/$info_file_name ];then
    touch $info_file_path/$info_file_name
else
    rm -rf $info_file_path/$info_file_name
	touch $info_file_path/$info_file_name
fi

info_file_csv_name=hardware_info_`echo $wanip|sed 's/ /_/g'`"_"$file_create_time.csv

#create info txt file
echo "OS:$os" >>$info_file_path/$info_file_name_path/$info_file_name
echo "Version:$version" >>$info_file_path/$info_file_name
echo "Wan IP:$wanip" >>$info_file_path/$info_file_name
echo "Wan Nic:$wan_nic" >>$info_file_path/$info_file_name
echo "Wan MAC:$wan_mac" >>$info_file_path/$info_file_name
echo "Lan IP:$lanip" >>$info_file_path/$info_file_name
echo "Lan Nic:$lan_nic" >>$info_file_path/$info_file_name
echo "Lan MAC:$lan_mac" >>$info_file_path/$info_file_name
echo "Serial Number:$serial_number" >>$info_file_path/$info_file_name
echo "Manufacturer:$manufacturer" >>$info_file_path/$info_file_name
echo "Product Name:$product_name" >>$info_file_path/$info_file_name
echo "Processor Count:$processor_count" >>$info_file_path/$info_file_name
echo "Processor Version:$processor_version" >>$info_file_path/$info_file_name
echo "Memory Slots:$memory_slot" >>$info_file_path/$info_file_name
echo "Memory Installed:$memory_installed" >>$info_file_path/$info_file_name
echo "Memory Size By Single:$memory_size_by_single GB" >>$info_file_path/$info_file_name
echo "Memory Total Size:$memory_total_size GB" >>$info_file_path/$info_file_name
echo "Raid Level:$Raid_Level" >>$info_file_path/$info_file_name
echo "Disk Count:$disk_count" >>$info_file_path/$info_file_name
echo "Disk Size By Single:$disk_size_by_single GB" >>$info_file_path/$info_file_name

#more $info_file_path/$info_file_name


#create info csv file
#structure
#wanip,lanip,serial_number,manufacturer,product_name,processor_count,processor_version,memory_slot,memory_installed,memory_size_by_single,memory_total_size,Raid_Level,disk_count,disk_size_by_single
echo "$os,$version,$wanip,$wan_nic,$wan_mac,$lanip,$lan_nic,$lan_mac,$serial_number,$manufacturer,$product_name,$processor_count,\
$processor_version,$memory_slot,$memory_installed,$memory_size_by_single,\
$memory_total_size,$Raid_Level,$disk_count,$disk_size_by_single" >$info_file_path/$info_file_csv_name





#执行FTP上传动作将检测结果上传到FTP服务器，仅上传csv文件。FTP服务器203.19.33.119，用户名switch，密码ftp-passwd_Hhly2017，上传到FTP的upload目录
ftp_upload_result=/tmp/ftp_upload.log
echo "
open 203.19.33.119
prompt
user switch ftp-passwd_Hhly2017
cd upload
binary
put $info_file_path/$info_file_csv_name ./$info_file_csv_name
close
bye
"|ftp -v -n |sed 's/^/>/g' >>$ftp_upload_result

#检查FTP上传结果
if [ -s $ftp_upload_result ];then
	login_result=`grep 'Login successful' $ftp_upload_result`
	if [ $? -eq 0 ];then
	    echo "FTP LOGGING SUCCESS!"
        SEARCH=`grep 'bytes sent in' $ftp_upload_result`
        if [ $? -eq 0 ];then
            echo "Hardware_info file upload successful."
            rm -rf $ftp_upload_result
        else
            echo "Hardware_info file upload fail."
            mv $ftp_upload_result /tmp/ftp_upload_fail_${file_create_time}.log
	    	echo "Please read /tmp/ftp_upload_fail_${file_create_time}.log for more detail."
        fi
	else
	    echo "FTP LOGGING FAIL!"
        exit 1
	fi
else
    echo "FTP LOGGING FAIL!"
    exit 1
fi

rm $0
