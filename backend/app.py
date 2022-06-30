from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import true
from routes import simple_page

app = Flask(__name__)

# blueprint for routes
app.register_blueprint(simple_page)

# import model to start the process of initializing the database (this line must be here)
from cam_model import db

# for the model to create database 
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)   

# setting which configuration to use depending on the environment
if app.config["ENV"] == "production":
    app.config.from_object('config.ProductionConfig')
elif app.config["ENV"] == "testing":
    app.config.from_object('config.TestingConfig')
elif app.config["ENV"] == "development":
    app.config.from_object('config.DevelopmentConfig')

# prevent CORS
CORS(app)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=true)






