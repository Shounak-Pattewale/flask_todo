import os
from flask_pymongo import PyMongo
from todo import todo
from bson.objectid import ObjectId

mongo = PyMongo(todo,uri=os.environ.get('MONGO_URI'))

class List:

    def add_todo(self,new_list):
        mongo.db.todo.insert_one({'task':new_list['task'],'date':new_list['date']})
        # print('Todo Added : ',add)

    def remove_todo(self,_id):
        mongo.db.todo.delete_one({'_id':ObjectId(_id)})
        # print('ID REMOVE : ',_id)

    def find_todo(self):
        data = mongo.db.todo.find({})
        return data