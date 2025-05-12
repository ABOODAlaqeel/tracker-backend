from flask import Blueprint, request, jsonify
from app import db
from app.models import AppMessage
from flask_jwt_extended import jwt_required

apps_bp = Blueprint('apps', __name__)

@apps_bp.route('', methods=['POST'])
@jwt_required()
def add_app_message():
    data = request.get_json()
    msg = AppMessage(
        device_id=data['device_id'],
        app_name=data['app_name'],
        title=data.get('title'),
        body=data.get('body'),
        timestamp=data.get('timestamp')
    )
    db.session.add(msg)
    db.session.commit()
    return jsonify({'msg': 'App message saved'}), 201

@apps_bp.route('', methods=['GET'])
@jwt_required()
def get_app_messages():
    device_id = request.args.get('deviceId')
    msgs = AppMessage.query.filter_by(device_id=device_id).all()
    return jsonify([{
        'app_name': m.app_name,
        'title': m.title,
        'body': m.body,
        'timestamp': m.timestamp
    } for m in msgs]), 200
