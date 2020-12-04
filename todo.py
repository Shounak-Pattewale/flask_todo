from flask import Flask
from flask import render_template, redirect, request, url_for, flash
from datetime import datetime
import os

todo = Flask(__name__)

from models import List
List = List()

todo.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@todo.route('/',methods=['GET','POST'])
def home():
    data = list(List.find_todo())
    priority = [d['date'] for d in data]
    priority.sort()

    return render_template('todo.html',data=data,priority=priority)

@todo.route('/add_todo', methods=['POST','GET'])
def add_todo():
    if request.method=='GET':
        return redirect(url_for('home'))
    
    else:
        req = request.form
        task = req.get('add-list')
        dt = req.get('date')
        new_list = {
            'task':task,
            'date':dt
        }
        List.add_todo(new_list)
        flash('Data Inserted Successfully','success')
        data = list(List.find_todo())
        return redirect(url_for('home'))    
    
@todo.route('/remove_todo', methods=['POST','GET'])
def remove_todo():
    if request.method=='GET':
        return redirect(url_for('home'))
    
    else:
        try:
            req = request.form
            _id = req.get('rm-list')
            List.remove_todo(_id)
            flash('Data Removed Successfully','warning')
            return redirect(url_for('home'))
        except Exception as error:
            print(error)
            flash('List is already empty','danger')
            data = list(List.find_todo())
            return redirect(url_for('home'))

if __name__=='__main__':
    todo.run(debug=True)