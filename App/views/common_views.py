from flask import Blueprint, request, jsonify
from App.controllers.admin import admin_view_all_areas, admin_view_all_streets
from App.models import Drive, Street

common_views = Blueprint('common_views', __name__)


@common_views.route('/areas', methods=['GET'])
def get_areas():
    areas = admin_view_all_areas()
    items = [a.get_json() if hasattr(a, 'get_json') else a for a in (areas or [])]
    return jsonify({'items': items}), 200


@common_views.route('/streets', methods=['GET'])
def get_streets():
    area_id = request.args.get('area_id')
    if area_id:
        streets = Street.query.filter_by(areaId=area_id).all()
    else:
        streets = admin_view_all_streets()
    items = [s.get_json() if hasattr(s, 'get_json') else s for s in (streets or [])]
    return jsonify({'items': items}), 200


@common_views.route('/streets/<int:street_id>/drives', methods=['GET'])
def street_drives(street_id):
    date = request.args.get('date')
    if date:
        drives = Drive.query.filter_by(streetId=street_id, date=date).all()
    else:
        drives = Drive.query.filter_by(streetId=street_id).all()
    items = [d.get_json() if hasattr(d, 'get_json') else d for d in (drives or [])]
    return jsonify({'items': items}), 200
