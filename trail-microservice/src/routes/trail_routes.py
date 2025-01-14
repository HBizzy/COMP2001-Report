from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
from controllers.trail_controller import TrailController
from utils.auth import authenticate_user

def setup_routes(app):
    trail_controller = TrailController()

    trail_bp = Blueprint('trail_bp', __name__)

    @trail_bp.route('/login', methods=['POST'])
    @swag_from({
        'parameters': [
            {
                'name': 'Authorization',
                'in': 'header',
                'type': 'string',
                'required': True,
                'description': 'Basic auth credentials in the format "username:password"'
            }
        ],
        'responses': {
            200: {
                'description': 'JWT token',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'token': {'type': 'string'}
                    }
                }
            },
            401: {
                'description': 'Unauthorized'
            }
        }
    })
    def login():
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({'error': 'Unauthorized'}), 401

        token = authenticate_user(auth.username, auth.password)
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        return jsonify({'token': token})

    @trail_bp.route('/trails', methods=['GET'])
    @swag_from({
        'responses': {
            200: {
                'description': 'A list of trails',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'TrailID': {'type': 'integer'},
                            'Trail_name': {'type': 'string'},
                            'Trail_Summary': {'type': 'string'},
                            'Trail_Description': {'type': 'string'},
                            'Difficulty': {'type': 'string'},
                            'Location': {'type': 'string'},
                            'Length': {'type': 'number'},
                            'Elevation_gain': {'type': 'integer'},
                            'Route_type': {'type': 'string'},
                            'OwnerID': {'type': 'integer'},
                            'Pt1_Lat': {'type': 'number'},
                            'Pt1_Long': {'type': 'number'},
                            'Pt1_Desc': {'type': 'string'},
                            'Pt2_Lat': {'type': 'number'},
                            'Pt2_Long': {'type': 'number'},
                            'Pt2_Desc': {'type': 'string'}
                        }
                    }
                }
            }
        }
    })
    def get_trails():
        return trail_controller.get_trails()

    @trail_bp.route('/trails/<int:trail_id>', methods=['GET'])
    @swag_from({
        'parameters': [
            {
                'name': 'trail_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'The ID of the trail'
            }
        ],
        'responses': {
            200: {
                'description': 'A single trail',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'TrailID': {'type': 'integer'},
                        'Trail_name': {'type': 'string'},
                        'Trail_Summary': {'type': 'string'},
                        'Trail_Description': {'type': 'string'},
                        'Difficulty': {'type': 'string'},
                        'Location': {'type': 'string'},
                        'Length': {'type': 'number'},
                        'Elevation_gain': {'type': 'integer'},
                        'Route_type': {'type': 'string'},
                        'OwnerID': {'type': 'integer'},
                        'Pt1_Lat': {'type': 'number'},
                        'Pt1_Long': {'type': 'number'},
                        'Pt1_Desc': {'type': 'string'},
                        'Pt2_Lat': {'type': 'number'},
                        'Pt2_Long': {'type': 'number'},
                        'Pt2_Desc': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Trail not found'
            }
        }
    })
    def get_trail(trail_id):
        return trail_controller.get_trail(trail_id)

    @trail_bp.route('/trails', methods=['POST'])
    @swag_from({
        'parameters': [
            {
                'name': 'Authorization',
                'in': 'header',
                'type': 'string',
                'required': True,
                'description': 'Bearer token'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'TrailID': {'type': 'integer'},
                        'Trail_name': {'type': 'string'},
                        'Trail_Summary': {'type': 'string'},
                        'Trail_Description': {'type': 'string'},
                        'Difficulty': {'type': 'string'},
                        'Location': {'type': 'string'},
                        'Length': {'type': 'number'},
                        'Elevation_gain': {'type': 'integer'},
                        'Route_type': {'type': 'string'},
                        'OwnerID': {'type': 'integer'},
                        'Pt1_Lat': {'type': 'number'},
                        'Pt1_Long': {'type': 'number'},
                        'Pt1_Desc': {'type': 'string'},
                        'Pt2_Lat': {'type': 'number'},
                        'Pt2_Long': {'type': 'number'},
                        'Pt2_Desc': {'type': 'string'}
                    }
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Trail created',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'TrailID': {'type': 'integer'},
                        'Trail_name': {'type': 'string'},
                        'Trail_Summary': {'type': 'string'},
                        'Trail_Description': {'type': 'string'},
                        'Difficulty': {'type': 'string'},
                        'Location': {'type': 'string'},
                        'Length': {'type': 'number'},
                        'Elevation_gain': {'type': 'integer'},
                        'Route_type': {'type': 'string'},
                        'OwnerID': {'type': 'integer'},
                        'Pt1_Lat': {'type': 'number'},
                        'Pt1_Long': {'type': 'number'},
                        'Pt1_Desc': {'type': 'string'},
                        'Pt2_Lat': {'type': 'number'},
                        'Pt2_Long': {'type': 'number'},
                        'Pt2_Desc': {'type': 'string'}
                    }
                }
            }
        }
    })
    def create_trail():
        return trail_controller.create_trail()

    @trail_bp.route('/trails/<int:trail_id>', methods=['PUT'])
    @swag_from({
        'parameters': [
            {
                'name': 'Authorization',
                'in': 'header',
                'type': 'string',
                'required': True,
                'description': 'Bearer token'
            },
            {
                'name': 'trail_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'The ID of the trail'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'Trail_name': {'type': 'string'},
                        'Trail_Summary': {'type': 'string'},
                        'Trail_Description': {'type': 'string'},
                        'Difficulty': {'type': 'string'},
                        'Location': {'type': 'string'},
                        'Length': {'type': 'number'},
                        'Elevation_gain': {'type': 'integer'},
                        'Route_type': {'type': 'string'},
                        'OwnerID': {'type': 'integer'},
                        'Pt1_Lat': {'type': 'number'},
                        'Pt1_Long': {'type': 'number'},
                        'Pt1_Desc': {'type': 'string'},
                        'Pt2_Lat': {'type': 'number'},
                        'Pt2_Long': {'type': 'number'},
                        'Pt2_Desc': {'type': 'string'}
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Trail updated',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'TrailID': {'type': 'integer'},
                        'Trail_name': {'type': 'string'},
                        'Trail_Summary': {'type': 'string'},
                        'Trail_Description': {'type': 'string'},
                        'Difficulty': {'type': 'string'},
                        'Location': {'type': 'string'},
                        'Length': {'type': 'number'},
                        'Elevation_gain': {'type': 'integer'},
                        'Route_type': {'type': 'string'},
                        'OwnerID': {'type': 'integer'},
                        'Pt1_Lat': {'type': 'number'},
                        'Pt1_Long': {'type': 'number'},
                        'Pt1_Desc': {'type': 'string'},
                        'Pt2_Lat': {'type': 'number'},
                        'Pt2_Long': {'type': 'number'},
                        'Pt2_Desc': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Trail not found'
            }
        }
    })
    def update_trail(trail_id):
        return trail_controller.update_trail(trail_id)

    @trail_bp.route('/trails/<int:trail_id>', methods=['DELETE'])
    @swag_from({
        'parameters': [
            {
                'name': 'Authorization',
                'in': 'header',
                'type': 'string',
                'required': True,
                'description': 'Bearer token'
            },
            {
                'name': 'trail_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'The ID of the trail'
            }
        ],
        'responses': {
            200: {
                'description': 'Trail deleted',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'Trail not found'
            }
        }
    })
    def delete_trail(trail_id):
        return trail_controller.delete_trail(trail_id)

    app.register_blueprint(trail_bp)