from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.utils import hash_password, verify_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'Email already exists'}), 400
    user = User(name=data['name'], email=data['email'], password_hash=hash_password(data['password']))
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'User created'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not verify_password(user.password_hash, data['password']):
        return jsonify({'msg': 'Bad credentials'}), 401
    token = create_access_token(identity=user.id)
    return jsonify({'access_token': token}), 200
