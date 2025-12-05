from flask import Blueprint, redirect, request, jsonify
from App.controllers import create_user, initialize

index_views = Blueprint('index_views', __name__)

@index_views.route('/', methods=['GET'])
def index_page():
    return jsonify({'message': 'Bread Van API', 'status': 'running'})

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})