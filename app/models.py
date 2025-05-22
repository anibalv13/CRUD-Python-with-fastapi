from sqlalchemy import Column, Integer, String, Date
from .database import Base 

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    date_birth = Column(Date)
    status = Column(Integer ,default=1)