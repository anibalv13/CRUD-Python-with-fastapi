from datetime import datetime
from pydantic import BaseModel


class StudentEntity(BaseModel):
    id: int
    name: str
    last_name: str
    date_birth: datetime
    status : int 
    
    class Config:
        orm_mode = True
        
class StudentCreate(BaseModel):
    name: str
    last_name: str
    date_birth: datetime
    status : int = 1
    
    class Config:
        orm_mode = True