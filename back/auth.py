from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from .db_api import get_user_auth, get_all_users
import json

bp = Blueprint('auth', __name__, url_prefix='/auth')

def init_app(app):
    app.config['JWT_SECRET_KEY'] = 'super-secret'

    jwt = JWTManager()
    jwt.init_app(app)

def pack_at_data(username):
    users = get_all_users()
    for user in users:
        if user.USER_USERNAME == username:
            at_data = dict(
                id=user.USER_ID,
                username=user.USER_USERNAME
            )
            return create_access_token(identity=json.dumps(at_data))
    return None

@bp.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    db_password = get_user_auth(username)
    if password == db_password:
        access_token = pack_at_data(username)
        return jsonify(access_token=access_token)
    else:
        print("Password hashes dont match!")
        print("Expected:", db_password, "- Got:", password)
        return abort(401)

@bp.route("/ident", methods=['GET'])
@jwt_required()
def protected():
    ident = get_jwt_identity()
    user  = json.loads(ident)
    return jsonify(identity=user['username'])