from flask import Blueprint, request, jsonify
from app import db
from app.models import CallLog
from flask_jwt_extended import jwt_required

calls_bp = Blueprint('calls', __name__)

@calls_bp.route('', methods=['POST'])
@jwt_required()
def add_call():
    data = request.get_json()
    call = CallLog(
        device_id=data['device_id'],
        phone_number=data['phone_number'],
        call_type=data['type'],
        duration=data.get('duration'),
        timestamp=data.get('timestamp'),
        recording_url=data.get('recording_url')
    )
    db.session.add(call)
    db.session.commit()
    return jsonify({'msg': 'Call log saved'}), 201

@calls_bp.route('', methods=['GET'])
@jwt_required()
def get_calls():
    device_id = request.args.get('deviceId')
    calls = CallLog.query.filter_by(device_id=device_id).all()
    return jsonify([{
        'phone_number': c.phone_number,
        'type': c.call_type,
        'duration': c.duration,
        'timestamp': c.timestamp,
        'recording_url': c.recording_url
    } for c in calls]), 200
