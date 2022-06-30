from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(240))
    completed = db.Column(db.Boolean, default=False, nullable=False)
