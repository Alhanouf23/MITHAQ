from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from pydantic import BaseModel

class Employee(Base):
    __tablename__ = "Employee"
    employee_id = Column(Integer, primary_key=True, index=True)
    region = Column(Integer)
    recruitment_channel = Column(String(30))
    adminId = Column(Integer, ForeignKey("Admin.admin_id"))
    DoB = Column(Date)
    age = Column(Integer)
    gender = Column(String(6))
    first_name = Column(String(25))
    last_name = Column(String(25))
    promot_id = Column(Integer, ForeignKey("Promotion.promotion_id"))
    depart_id = Column(Integer, ForeignKey("Department.department_id"))

    # Relationships
    admin = relationship("Admin", back_populates="employees")
    promotion = relationship("Promotion", back_populates="employees") 
    department = relationship("Department", back_populates="employees")


class Department(Base):
    __tablename__ = "Department"
    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(20))

    # Relationships
    employees = relationship("Employee", back_populates="department")
    trainings = relationship("Training", back_populates="department")


class Admin(Base):
    __tablename__ = "Admin"  
    
    admin_id = Column(Integer, primary_key=True, index=True)
    region = Column(String(50))
    gender = Column(String(6))
    full_name = Column(String(50))
    birth_date = Column(Date)
    age = Column(Integer)
    phone_number = Column(String(25))
    department = Column(String(20))  
    password = Column(String(50))

    # Relationships
    employees = relationship("Employee", back_populates="admin")


class Promotion(Base):
    __tablename__ = "Promotion"
    promotion_id = Column(Integer, primary_key=True, index=True)
    awards_won = Column(Integer)
    education = Column(String(20))
    previous_year_rating = Column(Float)  # Use Float for ratings
    length_of_service = Column(Integer)
    is_promoted = Column(Integer)

    # Relationships
    employees = relationship("Employee", back_populates="promotion")
    trainings = relationship("Training", back_populates="promotion")


class Training(Base):
    __tablename__ = "Training"
    training_id = Column(Integer, primary_key=True, index=True)
    avg_training_score = Column(Float)
    no_of_trainings = Column(Integer)
    depart_id = Column(Integer, ForeignKey("Department.department_id"))
    promot_id = Column(Integer, ForeignKey("Promotion.promotion_id"))

    # Relationships
    department = relationship("Department", back_populates="trainings")
    promotion = relationship("Promotion", back_populates="trainings")


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    gender: str
    employee_id: int
    recruitment_channel: str
    department: str
    education: str
    avg_training_score: float
    length_of_service: int
    previous_year_rating: float
    region: int
    no_of_trainings: int  
    age: int
    awards_won: int
    is_promoted: int
    DoB: str
    department: str
    adminId: int

    class Config:
        orm_mode = True
