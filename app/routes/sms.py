from flask import Blueprint, request, jsonify
from app import db
from app.models import SMSLog
from flask_jwt_extended import jwt_required

sms_bp = Blueprint('sms', __name__)

@sms_bp.route('', methods=['POST'])
@jwt_required()
def add_sms():
    data = request.get_json()
    sms = SMSLog(
        device_id=data['device_id'],
        phone_number=data['phone_number'],
        message_body=data['body'],
        direction=data['direction'],
        timestamp=data.get('timestamp')
    )
    db.session.add(sms)
    db.session.commit()
    return jsonify({'msg': 'SMS log saved'}), 201

@sms_bp.route('', methods=['GET'])
@jwt_required()
def get_sms():
    device_id = request.args.get('deviceId')
    msgs = SMSLog.query.filter_by(device_id=device_id).all()
    return jsonify([{
        'phone_number': m.phone_number,
        'body': m.message_body,
        'direction': m.direction,
        'timestamp': m.timestamp
    } for m in msgs]), 200
