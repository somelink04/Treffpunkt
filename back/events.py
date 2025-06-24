from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from .db_api import (
    get_confirmed_user_event,
    get_unconfirmed_user_event,
    add_confirm,
    revoke_confirm,
)
import json

bp = Blueprint('events', __name__, url_prefix='/events')


@bp.route('/suggestion', methods=['GET'])
@jwt_required()
def get_suggestions():
    user_identity = json.loads(get_jwt_identity())
    user_id = user_identity['id']

    #events ohne zusage
    events = get_unconfirmed_user_event(user_id)
    return jsonify([{
        "id": e['EVENT_ID'],
        "name": e['CATEGORY_NAME'],
        "description": e['CATEGORY_DESCRIPTION'],
        "location": e['REGION_NAME'],
        "date": e['EVENT_TIME'].isoformat() if e['EVENT_TIME'] else None
    } for e in events])



#Post testen? Bekomm hier einen network error
@bp.route('/reply', methods=['POST'])
@jwt_required()
def reply_to_events():
    user_identity = json.loads(get_jwt_identity())
    user_id = user_identity['id']

    responses = request.json
    if not isinstance(responses, list):
        return abort(400, "Expected a list of event replies")

    for r in responses:
        event_id = r.get('id')
        accepted = r.get('accepted')

        if event_id is None or accepted is None:
            continue

        if accepted:
            add_confirm(event_id)
        else:
            revoke_confirm(event_id)

    return jsonify({"status": "success"})


@bp.route('/accepted', methods=['GET'])
@jwt_required()
def get_accepted_events():
    user_identity = json.loads(get_jwt_identity())
    user_id = user_identity['id']

    events = get_confirmed_user_event(user_id)

    return jsonify([{
        "id": e['EVENT_ID'],
        "name": e['CATEGORY_NAME'],
        "description": e['CATEGORY_DESCRIPTION'],
        "location": e['REGION_NAME'],
        "date": e['EVENT_TIME'].isoformat() if e['EVENT_TIME'] else None,
        "participants": []  # keine ahung was hier ist
    } for e in events])