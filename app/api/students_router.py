from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.entity.student_entity import StudentCreate
from ..database import get_db  
from ..models import Students  

router = APIRouter()
    
@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Students).all()
    return students

@router.get("/students/active")
def get_active_students(db: Session = Depends(get_db)):
    students = db.query(Students).filter(Students.status == 1).all()
    return students

@router.get("/students/inactive")
def get_inactive_students(db: Session = Depends(get_db)):
    students = db.query(Students).filter(Students.status == 2).all()
    return students

@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if not student:
        return {"error": "Student not found"}
    return student

@router.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Students(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message": "Student created successfully", "student": db_student}

@router.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(Students).filter(Students.id == student_id).first()
    if not db_student:
        return {"error": "Student not found"}
    
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    
    db.commit()
    db.refresh(db_student)
    return {"message": "Student updated successfully", "student": db_student}

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Students).filter(Students.id == student_id).first()
    if not db_student:
        return {"error": "Student not found"}
    db_student.status = 2
    
    db.merge (db_student)
    db.commit()
    return {"message": "Student deleted successfully"}

@router.delete("/students/force/{student_id}")
def force_delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Students).filter(Students.id == student_id).first()
    if not db_student:
        return {"error": "Student not found"}
    
    db.delete(db_student)
    db.commit()
    return {"message": "Student force deleted successfully"}

@router.put("/students/restore/{student_id}")
def restore_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Students).filter(Students.id == student_id).first()
    if not db_student:
        return {"error": "Student not found"}
    
    db_student.status = 1
    db.merge (db_student)
    db.commit()
    return {"message": "Student restored successfully"}