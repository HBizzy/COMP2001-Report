import logging
from flask import request, jsonify
from models.trail_model import Trail
from services.trail_service import TrailService
from database import SessionLocal
from utils.auth import decode_jwt
import pyodbc

logger = logging.getLogger(__name__)

class TrailController:
    def __init__(self):
        self.db_session = SessionLocal()
        self.trail_service = TrailService(self.db_session)

    def get_trails(self):
        try:
            trails = self.trail_service.get_all_trails()
            return jsonify([trail.to_dict() for trail in trails])
        except Exception as e:
            logger.error(f"Error fetching trails: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def get_trail(self, trail_id):
        try:
            trail = self.trail_service.get_trail_by_id(trail_id)
            if trail:
                return jsonify(trail.to_dict())
            return jsonify({'error': 'Trail not found'}), 404
        except Exception as e:
            logger.error(f"Error fetching trail {trail_id}: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def create_trail(self):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        user_data = decode_jwt(token)
        if not user_data or user_data["role"] != "admin":
            return jsonify({'error': 'Forbidden'}), 403

        try:
            data = request.get_json()
            conn = self.db_session.connection().connection  # Get raw DBAPI connection
            cursor = conn.cursor()
            cursor.execute("""
                EXEC CW2.CreateTrail
                    @TrailID = ?, 
                    @Trail_name = ?, 
                    @Trail_Summary = ?, 
                    @Trail_Description = ?, 
                    @Difficulty = ?, 
                    @Location = ?, 
                    @Length = ?, 
                    @Elevation_gain = ?, 
                    @Route_type = ?, 
                    @OwnerID = ?, 
                    @Pt1_Lat = ?, 
                    @Pt1_Long = ?, 
                    @Pt1_Desc = ?, 
                    @Pt2_Lat = ?, 
                    @Pt2_Long = ?, 
                    @Pt2_Desc = ?""",
                data["TrailID"], data["Trail_name"], data["Trail_Summary"], data["Trail_Description"], data["Difficulty"], data["Location"], data["Length"], data["Elevation_gain"], data["Route_type"], data["OwnerID"], data["Pt1_Lat"], data["Pt1_Long"], data["Pt1_Desc"], data["Pt2_Lat"], data["Pt2_Long"], data["Pt2_Desc"])
            conn.commit()
            logger.info("Trail created successfully!")
            return jsonify({'message': 'Trail created successfully!'}), 201
        except pyodbc.Error as e:
            logger.error(f"Error creating trail: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def update_trail(self, trail_id):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        user_data = decode_jwt(token)
        if not user_data or user_data["role"] != "admin":
            return jsonify({'error': 'Forbidden'}), 403

        try:
            data = request.get_json()
            updated_trail = self.trail_service.update_trail(trail_id, data)
            if updated_trail:
                return jsonify(updated_trail.to_dict())
            return jsonify({'error': 'Trail not found'}), 404
        except Exception as e:
            logger.error(f"Error updating trail {trail_id}: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def delete_trail(self, trail_id):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        user_data = decode_jwt(token)
        if not user_data or user_data["role"] != "admin":
            return jsonify({'error': 'Forbidden'}), 403

        try:
            result = self.trail_service.delete_trail(trail_id)
            if result:
                return jsonify({'message': 'Trail deleted'})
            return jsonify({'error': 'Trail not found'}), 404
        except Exception as e:
            logger.error(f"Error deleting trail {trail_id}: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500