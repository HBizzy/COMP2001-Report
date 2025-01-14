from sqlalchemy import Column, Float, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.user_model import User  # Import User model to establish relationship

class Trail(Base):
    __tablename__ = 'TRAIL'
    __table_args__ = {'schema': 'CW2'}

    TrailID = Column(Integer, primary_key=True)
    Trail_name = Column(String, nullable=False)
    Trail_Summary = Column(String, nullable=False)
    Trail_Description = Column(String, nullable=False)
    Difficulty = Column(String, nullable=False)
    Location = Column(String, nullable=False)
    Length = Column(Float, nullable=False)
    Elevation_gain = Column(Integer, nullable=False)
    Route_type = Column(String, nullable=False)
    OwnerID = Column(Integer, ForeignKey('CW2.USER.UserID'), nullable=False)
    Pt1_Lat = Column(Float, nullable=False)
    Pt1_Long = Column(Float, nullable=False)
    Pt1_Desc = Column(String, nullable=False)
    Pt2_Lat = Column(Float, nullable=False)
    Pt2_Long = Column(Float, nullable=False)
    Pt2_Desc = Column(String, nullable=False)

    owner = relationship("User", back_populates="trails")

    def to_dict(self):
        return {
            "TrailID": self.TrailID,
            "Trail_name": self.Trail_name,
            "Trail_Summary": self.Trail_Summary,
            "Trail_Description": self.Trail_Description,
            "Difficulty": self.Difficulty,
            "Location": self.Location,
            "Length": self.Length,
            "Elevation_gain": self.Elevation_gain,
            "Route_type": self.Route_type,
            "OwnerID": self.OwnerID,
            "Pt1_Lat": self.Pt1_Lat,
            "Pt1_Long": self.Pt1_Long,
            "Pt1_Desc": self.Pt1_Desc,
            "Pt2_Lat": self.Pt2_Lat,
            "Pt2_Long": self.Pt2_Long,
            "Pt2_Desc": self.Pt2_Desc
        }

    def __repr__(self):
        return f"<Trail(name={self.Trail_name}, location={self.Location})>"