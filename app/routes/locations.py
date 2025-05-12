from flask import Blueprint, request, jsonify
from app import db
from app.models import Location
from flask_jwt_extended import jwt_required

locations_bp = Blueprint('locations', __name__)

@locations_bp.route('', methods=['POST'])
@jwt_required()
def add_location():
    data = request.get_json()
    loc = Location(
        device_id=data['device_id'],
        latitude=data['lat'],
        longitude=data['lng'],
        accuracy=data.get('accuracy'),
        timestamp=data.get('timestamp')
    )
    db.session.add(loc)
    db.session.commit()
    return jsonify({'msg': 'Location saved'}), 201

@locations_bp.route('', methods=['GET'])
@jwt_required()
def get_locations():
    device_id = request.args.get('deviceId')
    locs = Location.query.filter_by(device_id=device_id).all()
    return jsonify([{
        'lat': l.latitude, 'lng': l.longitude, 'accuracy': l.accuracy, 'timestamp': l.timestamp
    } for l in locs]), 200
