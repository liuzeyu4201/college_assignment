import unittest
from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Mysql1024."
app.config['MYSQL_DB'] = "dorm_management"
app.config['MYSQL_HOST'] = "localhost"
mysql = MySQL(app)

class TestDBConnection(unittest.TestCase):
    def setUp(self):
        # 在测试前配置
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_database_connection(self):
        """ 测试数据库连接是否成功 """
        try:
            # 尝试建立数据库连接并查询
            cur = mysql.connection.cursor()
            cur.execute("SELECT 1")
            result = cur.fetchone()
            self.assertIsNotNone(result, "数据库连接失败或无法查询数据")
        except Exception as e:
            self.fail(f"数据库连接测试失败，错误：{str(e)}")

if __name__ == '__main__':
    unittest.main()
