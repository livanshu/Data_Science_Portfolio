from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class InfoModel(db.Model):
    __tablename__ = 'info_table'

    index = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Text())
    mac_address = db.Column(db.Text())
    scan_timestamp = db.Column(db.Text())
    rssi = db.Column(db.Text())
    broadcast_data = db.Column(db.Text())
    broadcast_name = db.Column(db.Text())

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}:{self.age}"