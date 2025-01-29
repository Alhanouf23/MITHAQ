from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models import Employee

router = APIRouter()

# الاتصال بقاعدة البيانات
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/employees/")
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.post("/employees/")
def create_employee(employee: Employee, db: Session = Depends(get_db)):
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee
