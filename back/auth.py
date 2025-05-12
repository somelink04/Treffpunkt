from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

bp = Blueprint('auth', __name__, url_prefix='/auth')

def init_app(app):
    app.config['JWT_SECRET_KEY'] = 'super-secret'

    jwt = JWTManager()
    jwt.init_app(app)

@bp.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    if username == 'test' and password == 'test':
        access_token = create_access_token(identity=username)
        return jsonify(dict(access_token=access_token))

    else:
        return abort(401)

@bp.route("/ident", methods=['GET'])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return jsonify(identity=user)