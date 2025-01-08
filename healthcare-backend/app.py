from flask import Flask
from flask_mysqldb import MySQL
from app.config import Config


#Initialize the app and database
app=Flask(__name__)
app.config.from_object(Config)

mysql=MySQL(app)


if __name__=="main":
    app.run(debgug=True)

