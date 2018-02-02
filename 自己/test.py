#!/usr/bin/python
#coding:utf-8
import datetime

def insert_toMysql(data_list):
    """将dict数据导入mysql"""
    # 创建Connection连接

    # conn = connect(host='localhost', port=3306, database='yachang_preview', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    # cs1 = conn.cursor()
    i = 0
    for content in data_list:
        # pdb.set_trace()
        if i > 0:
            break
        # 增加一条数据
        values = tuple(content.values())
        print values
        keys = ','.join(content.keys())  # 字段名
        print keys
        sql_add = 'insert into zy_auction(%s) values %s' % (keys, values)
        print sql_add
        # count = cs1.execute(sql_add)
        # 提交之前的操作，此处为insert操作
        i += 1
        print "增加%d条数据"%i
        # conn.commit()
    # 关闭Cursor对象
    # cs1.close()
    # conn.close()

a = datetime.datetime(2018, 1, 12, 20, 34, 20, 260396)
print(a)
data_list = [{'hold_place': "\xe4\xbc\xa6\xe6\x95\xa6\xe4\xbd\xb3\xe5\xa3\xab\xe5\xbe\x97\xef\xbc\x88\xe5\x9b\xbd\xe7\x8e\x8b\xe8\xa1\x97\xef\xbc\x898 King Street  St. James's London SW1Y 6QT", 'preview_time': u'2017.12.09-2017.12.14', 'name': u'\u4f26\u6566\u4f73\u58eb\u5f97\uff1a\u5341\u4e5d\u4e16\u7eaa\u6b27\u6d32\u53ca\u4e1c\u65b9\u4e3b\u4e49\u827a\u672f', 'turnover_rate': u'71.43%', 'preview_place': "\xe4\xbc\xa6\xe6\x95\xa6\xe4\xbd\xb3\xe5\xa3\xab\xe5\xbe\x97\xef\xbc\x88\xe5\x9b\xbd\xe7\x8e\x8b\xe8\xa1\x97\xef\xbc\x898 King Street  St. James's London SW1Y 6QT", 'flow_rate': '28.57%', 'a_id': u'ab7d75fa7e7648e99a8ea8a253039cf5', 'operator': 0, 'create_date': u'2018-01-12 20:34:20.260396', 'auction_date': u'2017-12-14', 'hold_time': u'2017.12.14 14:30', 'ac_id': u'cf7a666d015b4dfcb9ab48b284091712'}]
insert_toMysql(data_list)