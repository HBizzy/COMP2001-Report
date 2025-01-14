import logging
from sqlalchemy.orm import Session
from models.trail_model import Trail

logger = logging.getLogger(__name__)

class TrailService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_trails(self):
        return self.db_session.query(Trail).all()

    def get_trail_by_id(self, trail_id: int):
        return self.db_session.query(Trail).filter(Trail.TrailID == trail_id).first()

    def create_trail(self, data: dict):
        try:
            new_trail = Trail(
                TrailID=data['TrailID'],
                Trail_name=data['Trail_name'],
                Trail_Summary=data['Trail_Summary'],
                Trail_Description=data['Trail_Description'],
                Difficulty=data['Difficulty'],
                Location=data['Location'],
                Length=data['Length'],
                Elevation_gain=data['Elevation_gain'],
                Route_type=data['Route_type'],
                OwnerID=data['OwnerID'],
                Pt1_Lat=data['Pt1_Lat'],
                Pt1_Long=data['Pt1_Long'],
                Pt1_Desc=data['Pt1_Desc'],
                Pt2_Lat=data['Pt2_Lat'],
                Pt2_Long=data['Pt2_Long'],
                Pt2_Desc=data['Pt2_Desc']
            )
            self.db_session.add(new_trail)
            self.db_session.commit()
            return new_trail
        except Exception as e:
            logger.error(f"Error creating trail: {e}")
            self.db_session.rollback()
            raise

    def update_trail(self, trail_id: int, data: dict):
        try:
            trail = self.get_trail_by_id(trail_id)
            if not trail:
                return None
            for key, value in data.items():
                setattr(trail, key, value)
            self.db_session.commit()
            return trail
        except Exception as e:
            logger.error(f"Error updating trail {trail_id}: {e}")
            self.db_session.rollback()
            raise

    def delete_trail(self, trail_id: int):
        try:
            trail = self.get_trail_by_id(trail_id)
            if not trail:
                return False
            self.db_session.delete(trail)
            self.db_session.commit()
            return True
        except Exception as e:
            logger.error(f"Error deleting trail {trail_id}: {e}")
            self.db_session.rollback()
            raise