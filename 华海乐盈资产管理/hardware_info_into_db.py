import os
import csv
import pymysql


def csv_to_list(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as csv_content:
        reader = csv.reader(csv_content)
        for line in reader:
            return line


def mac_address_format(mac):
    i = mac.split(":")
    return "{}{}-{}{}-{}{}".format(i[0], i[1], i[2], i[3], i[4], i[5])


# 打开数据库连接
db = pymysql.connect("localhost", "hhly", "hhly2017", "hhly")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)


hardware_info_file = r"D:\sc\IDC机房网络\资产管理开发\硬件信息收集\dg"
room_name = hardware_info_file.split("\\")[-1].upper()


successful_list = []
fail_list = []
for i in os.listdir(hardware_info_file):
    record = csv_to_list(os.path.join(hardware_info_file, i))
    insert_sql = "INSERT INTO hardwareinfo(room_name, os, version, wanip, wan_nic, wan_mac, lanip, lan_nic, lan_mac, \
    serial_number, manufacturer, product_name, processor_count, processor_version, memory_slot, memory_installed, \
    memory_size_by_single, memory_total_size, Raid_Level, disk_count, disk_size_by_single) VALUES ('{}', '{}', '{}', '{}', \
    '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        room_name, record[0], record[1], record[2], record[3], mac_address_format(record[4]), record[5], record[6], \
        mac_address_format(record[7]), record[8], record[9], record[10], record[11], record[12], record[13], \
        record[14], record[15], record[16], record[17], record[18], record[19]
    )
    #print(insert_sql)
    #print(mac_address_format(record[4]))
    ip = i.split("_")[2]
    try:
        cursor.execute(insert_sql)
        db.commit()
        print("{} import successful.".format(ip))
        successful_list.append(i)
    except:
        db.rollback()
        print("{} import fail.".format(ip))
        fail_list.append(i)


db.commit()

# 关闭数据库连接
db.close()

print("\n")
print("Total import successful:{}".format(len(successful_list)))
print("Total import fail:{}".format(len(fail_list)))


