from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

from .db_api import (
    get_user_settings, get_user, add_user_time, add_user_category, add_user_region,
    get_all_times, get_all_regions, get_all_categories
)

bp = Blueprint('settings', __name__, url_prefix='/api/settings')

@bp.route("", methods=['GET'])
@jwt_required()
def get_settings():
    ident = get_jwt_identity()
    user = json.loads(ident)
    user_id = user['id']

    # Daten aus DB
    user_region, user_categories, user_times = get_user_settings(user_id)
    user_obj = get_user(user_id)

    user_info = None
    if user_obj:
        user_info = dict(
            firstname=user_obj['USER_FIRSTNAME'],
            surname=user_obj['USER_SURNAME'],
            dayofbirth=user_obj['USER_BIRTHDATE'],
            username=user_obj['USER_USERNAME'],
            email=user_obj['USER_EMAIL'],
            region=user_obj['USER_REGION'],
        )

    categories = []
    for c in user_categories:
        categories.append(c['CATEGORY_ID'])

    # Zeiten als Liste von Dicts
    times: list[dict[str, int | list[int]]] = []
    for t in user_times:
        wd = t['WEEKDAY_ID']
        hr = t['HOUR_ID']

        # Add hour entry to existing weekday if exists
        w_kvp = [ kvp for kvp in times if kvp['weekday'] == wd]
        if len(w_kvp) > 0:
            w_kvp[0]['hours'].append(hr)
        else:
            times.append({
                'weekday': wd,
                'hours': [hr]
            })

    return jsonify(dict(
        user=user_info,
        categories=categories,
        times=times
    ))


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
def get_times():
    return jsonify(get_all_times())

@bp.route("/categories", methods=['GET'])
@jwt_required()
def get_categories():
    return jsonify(get_all_categories())

@bp.route("/regions", methods=['GET'])
@jwt_required()
def get_regions():
    return jsonify(get_all_regions())