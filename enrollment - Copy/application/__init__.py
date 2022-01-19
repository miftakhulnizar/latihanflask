from flask import Flask 
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_sample'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'secret124'

# Enter your database connection details below
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'framework'

# Intialize MySQL
# mysql = MySQL(app)

from application import routes

