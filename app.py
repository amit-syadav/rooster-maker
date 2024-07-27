# flask --app app run --debug
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

import get_rooster as rooster

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Rooster.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Employee(db.Model):
    name = db.Column(db.String(200), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"name :{self.name} - date_created:{self.date_created}"





def add_employees(employees):
    with app.app_context():
        # Create the database tables
        db.create_all()
        
        # Add each employee to the database
        for emp_name in employees:
            employee = Employee(name=emp_name)
            db.session.add(employee)
            
            # Commit the changesd
            db.session.commit()
            print("Employees added to the database")


@app.route('/')
def get_rooster():
    final_table=rooster.get_rooster()
    return render_template('rooster.html', final_table=final_table)

@app.route('/edit-employees', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        name = request.form['name'] 
        emp = Employee(name=name)
        db.session.add(emp)
        db.session.commit()
        
    allTodo = Employee.query.all() 
    return render_template('index.html', allTodo=allTodo)



@app.route('/inclusion-exclusion', methods=['GET', 'POST'])
def inclusion_exclusion():
    forced_exclusions,forced_inclusions = rooster.get_exclusions()
    return render_template('inclusion-exclusion.html', forced_exclusions=forced_exclusions, forced_inclusions=forced_inclusions)




@app.route('/delete/<string:name>', methods=['GET', 'POST'])
def delete(name):
    print(name)
    todo = Employee.query.filter_by(name=name).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/") 


@app.route('/update/<string:name>', methods=['GET', 'POST'])
def update(name):
    print('updating',name)
    if request.method=='POST':
        new_name = request.form['name'] 
        print(new_name)
        todo = Employee.query.filter_by(name=name).first()
        print('todo ', todo)
        todo.name = new_name 
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = Employee.query.filter_by(name=name).first()
    return render_template('update.html', todo=todo)