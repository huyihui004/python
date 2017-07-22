1、在所有目标服务器执行hardware_info_check.sh。
2、目标服务器会生成hardware_info_ip_*.csv和hardware_info_ip_*.txt两个文件，并自动把csv文件上传到指定ftp服务器。
3、手动从ftp服务器上面把csv文件下载到本地指定盘。
4、在本地执行hardware_info_into_db.py脚本，把所有csv文件导入到数据库服务器。
5、在服务器上运行idcm目录下的idcm.py脚本，启动网站服务。
6、浏览器打开http://ip:5000即可。