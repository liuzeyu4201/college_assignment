import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='Mysql1024.', db='dorm_management')
    print("连接成功")
except Exception as e:
    print("连接失败:", str(e))
