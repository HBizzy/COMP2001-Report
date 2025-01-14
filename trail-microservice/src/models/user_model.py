from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'USER'
    __table_args__ = {'schema': 'CW2'}

    UserID = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    trails = relationship("Trail", back_populates="owner")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"