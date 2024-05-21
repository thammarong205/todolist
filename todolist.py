from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

# การกำหนดค่า URI ของฐานข้อมูล
app.config['SQLALCHEMY_DATABASE_URI'] = 'cnx = mysql.connector.connect(user="todolist", password="{Pa$$w0rd}", host="todolist.mysql.database.azure.com", port=3306, database="{todolistsql}", ssl_ca="{ca-cert filename}", ssl_disabled=False)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# การเริ่มต้นฐานข้อมูล
db = SQLAlchemy(app)

# การตั้งค่าการบันทึกข้อผิดพลาด
logging.basicConfig(level=logging.DEBUG)

# การกำหนดโมเดล
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# การสร้างตารางฐานข้อมูล
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form['content']
    new_todo = Todo(content=content)

    try:
        db.session.add(new_todo)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        app.logger.error(f'Error adding todo: {e}')
        return 'There was an issue adding your todo'

@app.route('/delete/<int:id>')
def delete(id):
    todo_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(todo_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        app.logger.error(f'Error deleting todo: {e}')
        return 'There was a problem deleting that todo'

if __name__ == "__main__":
    app.run(debug=True)
