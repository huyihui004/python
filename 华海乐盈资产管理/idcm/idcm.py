from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['idc_room_name'] != 'None':
            #return request.form['idc_room_name']
            db = pymysql.connect("localhost", "root", "siman4mysql", "hhly")
            cursor = db.cursor()
            cursor.execute("SELECT room_name,os,version,wanip,lanip,serial_number,manufacturer,product_name,processor_version,\
            memory_installed,memory_total_size,Raid_Level,disk_count,disk_size_by_single from hardware_server\
             where room_name like '%{}%' and serial_number not like '%VMware%'".format(request.form['idc_room_name']))
            room_name = request.form['idc_room_name']
            results = cursor.fetchall()
            total_record = len(results)
            return render_template('index.html', room_name=room_name, total_record=total_record, results=results)
        elif request.form['ip']:
            db = pymysql.connect("localhost", "root", "siman4mysql", "hhly")
            cursor = db.cursor()
            cursor.execute("SELECT room_name,os,version,wanip,lanip,serial_number,manufacturer,product_name,processor_version,\
                        memory_installed,memory_total_size,Raid_Level,disk_count,disk_size_by_single from hardware_server\
                         where wanip like '%{}%'".format(request.form['ip']))
            results = cursor.fetchall()
            if not results:
                db = pymysql.connect("localhost", "root", "siman4mysql", "hhly")
                cursor = db.cursor()
                cursor.execute("SELECT room_name,os,version,wanip,lanip,serial_number,manufacturer,product_name,processor_version,\
                                        memory_installed,memory_total_size,Raid_Level,disk_count,disk_size_by_single from hardware_server\
                                         where lanip like '%{}%'".format(request.form['ip']))
                results = cursor.fetchall()
                total_record = len(results)
                return render_template('index.html', total_record=total_record, results=results)
            total_record = len(results)
            return render_template('index.html', total_record=total_record, results=results)
        elif request.form['sn']:
            db = pymysql.connect("localhost", "root", "siman4mysql", "hhly")
            cursor = db.cursor()
            cursor.execute("SELECT room_name,os,version,wanip,lanip,serial_number,manufacturer,product_name,processor_version,\
                        memory_installed,memory_total_size,Raid_Level,disk_count,disk_size_by_single from hardware_server\
                         where serial_number like '%{}%'".format(request.form['sn']))
            results = cursor.fetchall()
            total_record = len(results)
            return render_template('index.html', total_record=total_record, results=results)


    db = pymysql.connect("localhost", "root", "siman4mysql", "hhly")
    cursor = db.cursor()
    #cursor.execute("select lanip from hardware_server where lanip like '%10.14.188.111%'")
    cursor.execute("SELECT room_name,os,version,wanip,lanip,serial_number,manufacturer,product_name,processor_version,\
memory_installed,memory_total_size,Raid_Level,disk_count,disk_size_by_single from hardware_server\
 where serial_number not like '%VMware%'")
    #return cursor.fetchone()
    results = cursor.fetchall()
    total_record = len(results)
    return render_template('index.html', total_record=total_record, results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
