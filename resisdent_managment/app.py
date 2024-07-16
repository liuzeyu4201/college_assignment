from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql1024.'
app.config['MYSQL_DB'] = 'dorm_management'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add_student_page():
    return render_template('add.html')

@app.route('/search')
def search_student_page():
    return render_template('search.html')

@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    cur = mysql.connection.cursor()
    print("Manage Students Called")
    
    if request.method == 'POST':
        data = request.json
        print("Received data for POST:", data)
        cur.execute("INSERT INTO students (student_id, name, gender, dorm_number, phone) VALUES (%s, %s, %s, %s, %s)",
                    (data['student_id'], data['name'], data['gender'], data['dorm_number'], data['phone']))
        mysql.connection.commit()
        return jsonify({'message': 'Student added successfully'}), 201
    
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("Fetched students:", rows)
    return jsonify(rows)

@app.route('/students/<id>', methods=['GET', 'DELETE'])
@app.route('/students/<id>', methods=['GET', 'DELETE'])
def student_by_id(id):
    cur = mysql.connection.cursor()
    
    if request.method == 'DELETE':
        print("Deleting student with ID:", id)  # 日志输出
        cur.execute("DELETE FROM students WHERE student_id = %s", [id])
        mysql.connection.commit()
        print("Deleted successfully, check database now")  # 日志输出
        return jsonify({'message': 'Student deleted successfully'}), 200
    
    cur.execute("SELECT student_id, name, gender, dorm_number, phone FROM students WHERE student_id = %s", [id])
    row = cur.fetchone()
    if row:
        student = {
            'student_id': row[0],
            'name': row[1],
            'gender': row[2],
            'dorm_number': row[3],
            'phone': row[4]
        }
        return jsonify(student)
    else:
        return jsonify({}), 404





if __name__ == '__main__':
    app.run(debug=True)
