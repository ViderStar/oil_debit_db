from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Well(Base):
    __tablename__ = "Well"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_well = Column(Integer, nullable=False)
    id_tag = Column(Integer, nullable=False)
    tag_val = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)