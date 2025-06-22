from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from db_api import get_user_settings, get_user, user_to_dict, add_user_time, add_user_category, add_user_region

bp = Blueprint('settings', __name__, url_prefix='/settings')

@bp.route("", methods=['GET'])
@jwt_required()
def get_settings():
    ident = get_jwt_identity()
    user = json.loads(ident)
    user_id = user['id']

    # Daten aus DB
    user_region, user_categories, user_times = get_user_settings(user_id)
    user_obj = get_user(user_id)
    user_info = user_to_dict(user_obj) if user_obj else {}


    region = None
    if user_region and len(user_region) > 0:
        r = user_region[0]
        region = {
            "id": r.REGION_ID,
            "zip": r.REGION_ZIP,
            "name": r.REGION_NAME,
        }

    # Kategorien als Liste von Dicts
    categories = []
    for c in user_categories:
        categories.append({
            "id": c.CATEGORY_ID,
            "name": c.CATEGORY_NAME,
            "description": c.CATEGORY_DESCRIPTION,
            "min": c.CATEGORY_MIN,
            "acceptance_ratio": c.CATEGORY_ACCEPTION_RATIO,
        })

    # Zeiten als Liste von Dicts
    times = []
    for t in user_times:
        times.append({
            "user_time_id": t.USER_TIME_ID,
            "hour_id": t.HOUR_ID,
            "hour_name": t.HOUR_NAME,
            "weekday_id": t.WEEKDAY_ID,
            "weekday_name": t.WEEKDAY_NAME,
        })

    return jsonify({
        "user": user_info,
        "region": region,
        "categories": categories,
        "times": times,
    })


@bp.route("", methods=['POST'])
@jwt_required()
def post_settings():
    ident = get_jwt_identity()
    user = json.loads(ident)
    user_id = user['id']

    data = request.json
    if not data:
        return abort(400, "No data provided")

    # Region updaten (wenn vorhanden)
    if "region" in data:
        zip_code = data["region"].get("zip")
        if zip_code:
            add_user_region(user_id, zip_code)

    # Kategorien hinzufügen
    if "categories" in data:
        for cat in data["categories"]:
            add_user_category(user_id, cat["id"])

    # Zeiten hinzufügen (wir können nicht löschen und ist auch nicht in db_api implementiert)
    if "times" in data:
        for time_entry in data["times"]:
            add_user_time(user_id, time_entry["hour_id"], time_entry["weekday_id"])

    return '', 204 # No Content response for successful POST without body


#times
@bp.route("/times", methods=['GET'])
@jwt_required()
def get_user_times():
    ident = get_jwt_identity()
    user = json.loads(ident)
    user_id = user['id']

    _, _, user_times = get_user_settings(user_id)

    times = []
    for t in user_times:
        times.append({
            "user_time_id": t.USER_TIME_ID,
            "hour_id": t.HOUR_ID,
            "hour_name": t.HOUR_NAME,
            "weekday_id": t.WEEKDAY_ID,
            "weekday_name": t.WEEKDAY_NAME,
        })

    return jsonify(times=times)
@bp.route("/categories", methods=['GET'])
@jwt_required()
def get_user_categories():
    ident = get_jwt_identity()
    user = json.loads(ident)
    user_id = user['id']

    _, user_categories, _ = get_user_settings(user_id)

    categories = []
    for c in user_categories:
        categories.append({
            "id": c.CATEGORY_ID,
            "name": c.CATEGORY_NAME,
            "description": c.CATEGORY_DESCRIPTION,
            "min": c.CATEGORY_MIN,
            "acceptance_ratio": c.CATEGORY_ACCEPTION_RATIO,
        })

    return jsonify(categories=categories)

@bp.route("/regions", methods=['GET'])
@jwt_required()
def get_user_region():
    ident = get_jwt_identity()
    user = json.loads(ident)
    user_id = user['id']

    user_region, _, _ = get_user_settings(user_id)

    region = None
    if user_region and len(user_region) > 0:
        r = user_region[0]
        region = {
            "id": r.REGION_ID,
            "zip": r.REGION_ZIP,
            "name": r.REGION_NAME,
        }

    return jsonify(region=region)