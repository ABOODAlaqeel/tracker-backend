from flask import Blueprint, request, jsonify
from app import db
from app.models import Device
from flask_jwt_extended import jwt_required, get_jwt_identity

devices_bp = Blueprint('devices', __name__)

@devices_bp.route('', methods=['POST'])
@jwt_required()
def add_device():
    data = request.get_json()
    user_id = get_jwt_identity()
    device = Device(user_id=user_id, name=data.get('name'))
    db.session.add(device)
    db.session.commit()
    return jsonify({'device_id': device.id}), 201
