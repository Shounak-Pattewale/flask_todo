# flask_todo

A simplest To-Do App build with Flask Framework

### Requirements
* pip install flask

### dot-env Structure
FLASK_APP=todo.py<br>
FLASK_ENV=development<br>
SECRET_KEY =<br>
MONGO_URI=

### Run Command
* Method one :
1. export FLASK_APP=run.py
2. export FLASK_ENV=development
3. flask run

* Method two :
1. Launch your bash terminal, and type
2. ./run
<br>
This is a pretty cool method which I have once discovered out of curiosity

#### Note : 
Secret Key is needed for flashing purpose in flask. Make sure to add it in a seperate config or env file.