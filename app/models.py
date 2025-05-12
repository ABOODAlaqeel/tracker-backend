import uuid
from datetime import datetime
from app import db

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Device(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120))
    last_seen_at = db.Column(db.DateTime, default=datetime.utcnow)

class Location(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    device_id = db.Column(db.String, db.ForeignKey('device.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    accuracy = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class CallLog(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    device_id = db.Column(db.String, db.ForeignKey('device.id'), nullable=False)
    phone_number = db.Column(db.String(20))
    call_type = db.Column(db.String(10))  # 'in' or 'out'
    duration = db.Column(db.Integer)  # seconds
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    recording_url = db.Column(db.String)

class SMSLog(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    device_id = db.Column(db.String, db.ForeignKey('device.id'), nullable=False)
    phone_number = db.Column(db.String(20))
    message_body = db.Column(db.Text)
    direction = db.Column(db.String(10))  # 'in' or 'out'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class AppMessage(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    device_id = db.Column(db.String, db.ForeignKey('device.id'), nullable=False)
    app_name = db.Column(db.String(50))
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
