from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import joblib
import sys
import os
import random
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException
from twilio.rest import Client
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import func
from fastapi.middleware.cors import CORSMiddleware
from config import SessionLocal, engine
from models import Base, Employee, Department, Promotion, Training, Admin, EmployeeCreate
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql import text
from fastapi.responses import JSONResponse, HTMLResponse
from datetime import date
from typing import Optional
from sqlalchemy import create_engine, text
from fastapi.staticfiles import StaticFiles
from datetime import datetime, date
from typing import Optional
import re


# Load the model
model = joblib.load("model/model.pkl")

account_sid = "TWTLIO-ACCOUNT-SID"
auth_token = "TWILIO-AUTH-TOKEN"   
client = Client(account_sid, auth_token)


SECRET_KEY = "72e15850306775e5820106b5eeda480828fb13ba82dd8be3be4cbb720f84bdec"

# Create the FastAPI app
app = FastAPI()
app.mount("/Assets", StaticFiles(directory=os.path.join("D:/MITHAQ/app/Assets")), name="Assets")
app.mount("/Layouts", StaticFiles(directory=os.path.join("D:/MITHAQ/app/Views/Layouts")), name="Layouts")

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create database tables
Base.metadata.create_all(bind=engine)

# Define a Pydantic model for input validation
class ModelInput(BaseModel):
    department: int
    education: int
    region: int
    avg_training_score: float
    length_of_service: int
    previous_year_rating: float


# Define a Pydantic model for Sign-In
class SignInRequest(BaseModel):
    id: int
    password: str
    
# Mapping regions to names
region_mapping = {
    1: "New York",
    2: "Los Angeles",
    3: "Chicago",
    4: "Houston",
    5: "Phoenix",
    6: "Philadelphia",
    7: "San Antonio",
    8: "San Diego",
    9: "Dallas",
    10: "San Jose",
    11: "Austin",
    12: "Jacksonville",
    13: "Fort Worth",
    14: "Columbus",
    15: "Charlotte",
    16: "San Francisco",
    17: "Indianapolis",
    18: "Seattle",
    19: "Denver",
    20: "Washington",
    21: "Boston",
    22: "El Paso",
    23: "Nashville",
    24: "Detroit",
    25: "Oklahoma City",
    26: "Portland",
    27: "Las Vegas",
    28: "Memphis",
    29: "Louisville",
    30: "Baltimore",
    31: "Milwaukee",
    32: "Albuquerque",
    33: "Tucson",
    34: "Fresno",
    35: "Sacramento"
}
# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# OTP cache to store temporary OTPs
otp_cache = {}

# Pydantic models
class ForgotPasswordRequest(BaseModel):
    admin_id: int

class VerifyOTPRequest(BaseModel):
    admin_id: int
    otp: int

class ResetPasswordRequest(BaseModel):
    admin_id: int
    new_password: str

# =====================================================================================================================================


# Forgot Password Route
@app.post("/forgot-password/")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    """Send OTP to the admin's registered phone number."""
    admin = db.query(Admin).filter(Admin.admin_id == request.admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found.")

 # Generate random OTP
    otp = random.randint(100000, 999999)
    
        # Send OTP via Twilio
    try:
        client.messages.create(
            body=f"Your OTP is {otp}",
            from_="whatsapp:+14155238886",
            to=f"{admin.phone_number}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send OTP: {e}")

    # Store OTP in the cache
    otp_cache[request.admin_id] = otp
    return {"message": "OTP sent successfully."}
# Verify OTP Route
@app.post("/verify-otp/")
def verify_otp(request: VerifyOTPRequest):
    """Verify the OTP provided by the admin."""
    if request.admin_id not in otp_cache or otp_cache[request.admin_id] != request.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP.")
    
    # Remove OTP from the cache after successful verification
    del otp_cache[request.admin_id]
    return {"message": "OTP verified successfully."}
# Reset Password Route
@app.post("/reset-password/")
def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    """Reset the password after verifying its validity."""
    admin = db.query(Admin).filter(Admin.admin_id == request.admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found.")
    
    if admin.password == request.new_password:
        raise HTTPException(status_code=400, detail="New password must be different from the old password.")
    
  # Verify the validity of the password
    password = request.new_password
    password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    print(f"Password: {password}")
    print(f"Match: {re.match(password_pattern, password)}")
    if not re.match(password_pattern, password):
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")
    
# If the password is correct, we update it in the database
    admin.password = request.new_password
    db.commit()
    return {"message": "Password reset successfully."}

# Root Route    
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("D:/MITHAQ/app/Views/Layouts/loginPage.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Main Page 
@app.get("/main", response_class=HTMLResponse)
async def get_main_page():
    with open("D:/MITHAQ/app/Views/Layouts/main.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Results Page 
@app.get("/resultsPage", response_class=HTMLResponse)
async def get_results_page():
    with open("D:/MITHAQ/app/Views/Layouts/resultsPage.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
    
# Dashboard page
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page():
    with open("D:/MITHAQ/app/Views/Layouts/dashboard.html", "r", encoding="utf-8") as f:
        return f.read()

# newEmployee page
@app.get("/newEmplyoee", response_class=HTMLResponse)
def dashboard_page():
    with open("D:/MITHAQ/app/Views/Layouts/newEmplyoee.html", "r", encoding="utf-8") as f:
        return f.read()
        
# Reports Page 
@app.get("/reportsPage", response_class=HTMLResponse)
async def get_reports_page():
    try:
        with open("D:/MITHAQ/app/Views/Layouts/reportsPage.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
    
# Promotion Criteria Page Route
@app.get("/promotionCriteria", response_class=HTMLResponse)
async def get_promotionCriteria_page():
    try:
        with open("D:/MITHAQ/app/Views/Layouts/promotionCriteria.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
    
    
 # Profile (Personal Information) Page Route
@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    # Fetch admin_id from the session
    admin_id = request.session.get("admin_id")  # Take id from session
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response with a message
        return HTMLResponse(content="<h1>You need to log in first</h1>", status_code=401)

    # Open the HTML file without needing to replace {{ admin_id }}
    with open("D:/MITHAQ/app/Views/Layouts/profile.html", "r", encoding="utf-8") as file:
        # Read the content of the HTML file
        html_content = file.read()

    # Return the HTML content as a response
    return HTMLResponse(content=html_content)
    

    
    
    # Edit Profile (Personal Information) Page Route
@app.get("/editProfile", response_class=HTMLResponse)
async def get_editProfile():
    try:
        with open("D:/MITHAQ/app/Views/Layouts/editProfile.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
    

    
    # Edit Profile (Password) Page Route
@app.get("/editPassword", response_class=HTMLResponse)
async def get_editProfile():
    try:
        with open("D:/MITHAQ/app/Views/Layouts/editPassword.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
        
    
    
    
# Logout Route
@app.post("/logout")

def logout(request: Request):
    request.session.clear()
    return {"message": " logged out successfully!"}
    

        
# Function to authenticate admin
def authenticate_admin(db: Session, admin_id: int, password: str):
    return db.query(Admin).filter(Admin.admin_id == admin_id, Admin.password == password).first()

# Sign In Route
# Start of sign-in
@app.post("/")
def sign_in(request: Request, login_data: SignInRequest, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(
        Admin.admin_id == login_data.id, Admin.password == login_data.password
    ).first()

    if not admin:
        raise HTTPException(status_code=401, detail="Invalid ID or password")
    
    request.session["admin_id"] = admin.admin_id
    request.session["password"] = admin.password

    return {"message": "Login successful, session created."}
# End of sign-in

# Verify the session
@app.get("/check-session")
def check_session(request: Request):
    admin_id = request.session.get("admin_id")
    password = request.session.get("password")

    if not admin_id or not password:
        raise HTTPException(status_code=401, detail="No active session found.")

    return {"admin_id": admin_id, "password": password}


# =====================================================================================================================================

# Statistics Route 
@app.get("/statistics")
def get_statistics(db: Session = Depends(get_db)):
    try:
        # Fetch data by joining Employee, Department, Promotion, and Training tables
        results = db.query(
            Employee.employee_id,
            Employee.first_name,
            Employee.last_name,
            Department.department_name,
            Promotion.education,
            Employee.region,
            Promotion.previous_year_rating,
            Training.avg_training_score,
            Promotion.length_of_service,
            Employee.gender
        ).outerjoin(
            Department, Employee.depart_id == Department.department_id
        ).outerjoin(
            Promotion, Employee.promot_id == Promotion.promotion_id
        ).outerjoin(
            Training, (Employee.depart_id == Training.depart_id) & (Employee.promot_id == Training.promot_id)
        ).all()
# General statistics initialization
        total_employees = len(results)
        total_departments = db.query(func.count(Department.department_id)).scalar() or 0
# Counters for promoted and unpromoted employees
        promoted_count = 0
        unpromoted_count = 0
        employees_per_department = {}
        promotions_by_department = {}
# Initialize dictionaries for department and gender-based statistics
        employees_distribution = {
            "female": {},
            "male": {}
        }
# Iterate through each employee record to calculate statistics
        for result in results:
            department_name = result.department_name or "Unknown"

            # Prepare input data for the model
            department_mapping = {
                "R&D": 0, "Legal": 1, "HR": 2, "Finance": 3, "Analytics": 4,
                "Procurement": 5, "Technology": 6, "Operations": 7, "Sales & Marketing": 8
            }
            department_number = department_mapping.get(department_name, 0)

            education_mapping = {
                "Below Secondary": 0, "Bachelor": 1, "Master & above": 2
            }
            education_number = education_mapping.get(result.education, 0)
# Prepare input data for prediction model
            input_data = np.array([[
                department_number,  
                education_number,   
                result.region,
                result.avg_training_score or 0.0,
                result.length_of_service or 0,
                result.previous_year_rating or 0.0
            ]])

            feature_names = ['department', 'education', 'region', 'avg_training_score', 'length_of_service', 'previous_year_rating']
            input_data_df = pd.DataFrame(input_data, columns=feature_names)

            # Predict promotion status using the model
            prediction = model.predict(input_data_df)

            # Count promoted and unpromoted based on model prediction
            if prediction[0] == 1:
                promoted_count += 1
                promotions_by_department[department_name] = promotions_by_department.get(department_name, 0) + 1
            else:
                unpromoted_count += 1

            # Count employees per department
            if department_name in employees_per_department:
                employees_per_department[department_name] += 1
            else:
                employees_per_department[department_name] = 1

            # Count gender distribution per department
            if result.gender == "Female":
                if department_name in employees_distribution["female"]:
                    employees_distribution["female"][department_name] += 1
                else:
                    employees_distribution["female"][department_name] = 1
            elif result.gender == "Male":
                if department_name in employees_distribution["male"]:
                    employees_distribution["male"][department_name] += 1
                else:
                    employees_distribution["male"][department_name] = 1

        # Prepare promotions by department with default values for missing departments
        all_departments = db.query(Department.department_name).all()
        for dept in all_departments:
            dept_name = dept[0]
            if dept_name not in promotions_by_department:
                promotions_by_department[dept_name] = 0
            if dept_name not in employees_per_department:
                employees_per_department[dept_name] = 0
            if dept_name not in employees_distribution["female"]:
                employees_distribution["female"][dept_name] = 0
            if dept_name not in employees_distribution["male"]:
                employees_distribution["male"][dept_name] = 0

        # Debugging output for validations
        total_promotions_by_department = sum(promotions_by_department.values())
        print(f"Promoted Count: {promoted_count}, Unpromoted Count: {unpromoted_count}")
        print(f"Promotions by Department: {promotions_by_department}")
        print(f"Total Promotions by Department: {total_promotions_by_department}")

        # Ensure consistency between total_promoted and promotions_by_department
        if promoted_count != total_promotions_by_department:
            print("Warning: Mismatch between total promoted and promotions by department!")

        # Prepare response data
        stats = {
            "total_employees": total_employees,
            "total_departments": total_departments,
            "total_promoted": promoted_count,
            "promotion_stats": {
                "promoted": promoted_count,
                "unpromoted": unpromoted_count
            },
            "employees_per_department": [
                {"department": dept, "count": count} for dept, count in employees_per_department.items()
            ],
            "promotions_by_department": [
                {"department": dept, "count": count} for dept, count in promotions_by_department.items()
            ],
            "employees_distribution": {
                "female": [employees_distribution["female"].get(dept[0], 0) for dept in all_departments],
                "male": [employees_distribution["male"].get(dept[0], 0) for dept in all_departments]
            }
        }

        return stats

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}
 # End of statistics


# =====================================================================================================================================

# Prediction route
# Start of results
@app.get("/results")
def get_results(db: Session = Depends(get_db)):
    try:
        
        results = db.query(
            Employee.employee_id,
            Employee.first_name,
            Employee.last_name,
            Department.department_name,
            Promotion.education,
            Employee.region,
            Promotion.previous_year_rating,
            Training.avg_training_score,
            Promotion.length_of_service
        ).outerjoin(
            Department, Employee.depart_id == Department.department_id
        ).outerjoin(
            Promotion, Employee.promot_id == Promotion.promotion_id
        ).outerjoin(
            Training, (Employee.depart_id == Training.depart_id) & (Employee.promot_id == Training.promot_id)
        ).all()

        processed_results = []

        for result in results:
            
            department_mapping = {
                "R&D": 0, "Legal": 1, "HR": 2, "Finance": 3, "Analytics": 4,
                "Procurement": 5, "Technology": 6, "Operations": 7, "Sales & Marketing": 8
            }
            department_number = department_mapping.get(result.department_name, 0)

            education_mapping = {
                "Below Secondary": 0, "Bachelor": 1, "Master & above": 2
            }
            education_number = education_mapping.get(result.education, 0)
            
            region_name = region_mapping.get(result.region, "Unknown")

            
            input_data = np.array([[
                department_number,  
                education_number,   
                result.region,
                result.avg_training_score or 0.0,
                result.length_of_service or 0,
                result.previous_year_rating or 0.0
            ]])

           
            feature_names = ['department', 'education', 'region', 'avg_training_score', 'length_of_service', 'previous_year_rating']
            input_data_df = pd.DataFrame(input_data, columns=feature_names)

           
            prediction = model.predict(input_data_df)

            department_name = result.department_name or "Unknown"
            
            if prediction[0] == 1:
                training_name = "-"
            else:
                
                if department_name == "HR":
                   training_name = "Human Resources Analytics"
                elif department_name == "Sales & Marketing":
                 training_name = "Client Management Strategies for Retention & Growth"
                elif department_name == "Finance":
                  training_name = "Finance Courses"
                elif department_name == "Operations":
                  training_name = "Operations Management"
                elif department_name == "Technology":
                   training_name = " ITIL 4 Foundation Training"
                elif department_name == "Procurement":
                    training_name = "Global Procurement and Sourcing Specialization"
                elif department_name == "R&D":
                   training_name = " R&D Management - professional certification"
                elif department_name == "Analytics":
                    training_name = "Business Analytics Specialization"
                else:
                    training_name = "Custom Training for Other Departments"
    

            
            processed_data = {
                "Employee_name": f"{result.first_name or 'Unknown'} {result.last_name or ''}",
                "ID": result.employee_id,
                "Department": result.department_name or "Unknown",
                "Education": result.education or "Unknown",
                "Region": region_name,
                "Avg_Training_Score": result.avg_training_score or 0.0,
                "Length_of_Service": result.length_of_service or 0,
                "Previous_Year_Rating": result.previous_year_rating or 0.0,
                "Is_Promoted": "Yes" if prediction[0] == 1 else "No",
                "Training_Name": training_name
            }
            processed_results.append(processed_data)

        return processed_results

    except Exception as e:
        return {"error": str(e)}
 # End of results

# =====================================================================================================================================

# Start of Backend code for (employee dashboard, new employee)

# Endpoint to get all employees
@app.get("/employees")
def get_employees():
    session = SessionLocal()
    try:
        # Execute the query manually
        sql_query = """
           SELECT
            e.employee_id AS id,
            e.first_name ,
            e.last_name ,
            d.department_name AS department,
            p.education,
            MAX(t.avg_training_score) AS avg_training_score, 
            p.length_of_service,
            p.previous_year_rating,
            e.region,
            e.gender,
            e.recruitment_channel,
            COUNT(t.training_id) AS no_of_trainings, -- عدد التدريبات
            e.age,
            p.awards_won,
            p.is_promoted
        FROM Employee e
        LEFT JOIN Department d ON e.depart_id = d.department_id
        LEFT JOIN Promotion p ON e.promot_id = p.promotion_id
        LEFT JOIN Training t ON e.promot_id = t.promot_id
        GROUP BY
        e.employee_id, e.first_name, d.department_name, p.education, p.length_of_service,
        p.previous_year_rating, e.region, e.gender, e.recruitment_channel, e.age, p.awards_won, p.is_promoted;
        """

        result = session.execute(text(sql_query)).fetchall()

        # Convert results to JSON
        response = [
            {
                "id": row.id,
                "first_name": row.first_name,
                "last_name": row.last_name,
                "department": row.department,
                "education": row.education,
                "avg_training_score": row.avg_training_score,
                "length_of_service": row.length_of_service,
                "previous_year_rating": row.previous_year_rating,
                "region": row.region,
                "gender": row.gender,
                "recruitment_channel": row.recruitment_channel,
                "no_of_trainings": row.no_of_trainings,
                "age": row.age,
                "awards_won": row.awards_won,
                "is_promoted": row.is_promoted,
            }
            for row in result
        ]

        return JSONResponse(content=response)

    finally:
        session.close()



# Endpoint to update an employee by ID
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee_data: dict, db: Session = Depends(get_db)):
    # Search for employee
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update public fields
    general_fields = ["region", "recruitment_channel", "DoB", "age", "gender", "first_name", "last_name"]
    for field in general_fields:
        if field in employee_data:
            setattr(employee, field, employee_data[field])

    # Update the fields associated with the section
    if "department" in employee_data:
        department = db.query(Department).filter_by(department_name=employee_data["department"]).first()
        if not department:
            raise HTTPException(status_code=404, detail="Department not found")
        employee.department = department

    # Update fields associated with the upgrade
    if "promotion" in employee_data:
        promotion_data = employee_data["promotion"]
        if isinstance(promotion_data, dict):
            for field, value in promotion_data.items():
                if hasattr(employee.promotion, field):
                    setattr(employee.promotion, field, value)

    # Save changes
    db.commit()
    db.refresh(employee)

    return {"message": "Employee updated successfully", "employee": employee}


# Endpoint to delete an employee by ID
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    # Find employee using employee_id
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
   # Delete from database
    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}


# Endpoint to add a new employee
@app.post("/employees-add")
def add_employee(employee_data: dict, db: Session = Depends(get_db)):
    try:
        # Check required fields
        if not employee_data.get("employee_id") or not employee_data.get("first_name") or not employee_data.get("last_name"):
            raise HTTPException(status_code=400, detail="Missing required fields: employee_id, first_name, or last_name")

        # 1- Bring or create a record in Promotion
        promot_result = db.execute(text("SELECT MAX(promotion_id) FROM Promotion")).fetchone()
        latest_promotion_id = promot_result[0] if promot_result[0] is not None else 0
        new_promotion_id = latest_promotion_id + 1

        # Add a new record in Promotion
        db.execute(text("""
            INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted)
            VALUES (:promotion_id, :awards_won, :education, :previous_year_rating, :length_of_service, :is_promoted)
        """), {
            "promotion_id": new_promotion_id,
            "awards_won": employee_data.get("awards_won", 0),
            "education": employee_data.get("education", "Not Specified"),
            "previous_year_rating": employee_data.get("previous_year_rating", 0.0),
            "length_of_service": employee_data.get("length_of_service", 0),
            "is_promoted": employee_data.get("is_promoted", 0)
        })

        # 2- Fetch depart_id from Department using department_name
        department_result = db.execute(text("""
            SELECT department_id FROM Department WHERE department_name = :department_name
        """), {"department_name": employee_data["department"]}).fetchone()

        if not department_result:
            raise HTTPException(status_code=400, detail=f"Department {employee_data['department']} does not exist.")
        
        depart_id = department_result[0]

        # 3- Enter the employee in Employee
        employee_query = text("""
            INSERT INTO Employee (
                employee_id, first_name, last_name, region, recruitment_channel, adminId, DoB, age, gender, promot_id, depart_id
            ) VALUES (
                :employee_id, :first_name, :last_name, :region, :recruitment_channel, :adminId, :DoB, :age, :gender, :promot_id, :depart_id
            )
        """)
        db.execute(employee_query, {
            "employee_id": employee_data["employee_id"],
            "first_name": employee_data["first_name"],
            "last_name": employee_data["last_name"],
            "region": employee_data["region"],
            "recruitment_channel": employee_data["recruitment_channel"],
            "adminId": employee_data["adminId"],
            "DoB": employee_data["DoB"],
            "age": employee_data["age"],
            "gender": employee_data["gender"],
            "promot_id": new_promotion_id,
            "depart_id": depart_id
        })

    
        training_result = db.execute(text("SELECT MAX(training_id) FROM Training")).fetchone()
        latest_training_id = training_result[0] if training_result[0] is not None else 0
        new_training_id = latest_training_id + 1

        training_query = text("""
            INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id)
            VALUES (:training_id, :avg_training_score, :no_of_trainings, :depart_id, :promot_id)
        """)
        db.execute(training_query, {
            "training_id": new_training_id,
            "avg_training_score": employee_data.get("avg_training_score", 0),
            "no_of_trainings": employee_data.get("no_of_trainings", 0),
            "depart_id": depart_id,
            "promot_id": new_promotion_id
})

        # Save changes to the database
        db.commit()
        return {
            "message": "Employee and related data added successfully",
            "employee": {
                "employee_id": employee_data["employee_id"],
                "first_name": employee_data["first_name"],
                "last_name": employee_data["last_name"],
                "promotion_id": new_promotion_id,
                "department_id": depart_id
            }
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
# End of Backend code for (employee dashboard, new employee)


 # =====================================================================================================================================

# Start of Admin Profile
@app.get("/profile/data")
def get_admin_data(request: Request):
    # Get the admin_id from the session
    admin_id = request.session.get("admin_id")  # Fetch the admin_id from the session
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="No active session found.")

    # Create a new session to interact with the database
    session = SessionLocal()
    try:
        # SQL query to fetch admin data by admin_id
        sql_query = """
        SELECT
            a.admin_id AS id,
            a.full_name AS full_name,
            a.birth_date AS date_of_birth,
            a.region,
            a.gender,
            a.phone_number,
            a.department
        FROM Admin a
        WHERE a.admin_id = :admin_id;
        """

        # Execute the SQL query and fetch the result
        result = session.execute(text(sql_query), {"admin_id": admin_id}).fetchone()

        if not result:
            # If no data is found for the provided admin_id, return a 404 Not Found response
            raise HTTPException(status_code=404, detail="Admin not found")

        # Convert date_of_birth to ISO format, or set it to "N/A" if not available
        date_of_birth = result.date_of_birth.isoformat() if result.date_of_birth else "N/A"

        # Prepare the response data as a dictionary
        response = {
            "admin_id": result.id,
            "full_name": result.full_name,
            "date_of_birth": date_of_birth,
            "region": result.region,
            "gender": result.gender,
            "phone_number": result.phone_number,
            "department": result.department
        }

        # Return the data as a JSON response
        return JSONResponse(content=response)

    finally:
        # Close the session to free up resources
        session.close()

# End of Admin Profile




# Start of Edit Admin Profile (All Fields)

# Define a request model to validate the profile data for updating
class ProfileUpdateRequest(BaseModel):
    full_name: str  # Admin's full name
    birth_date: str  # Admin's birth date
    region: str  # Admin's region
    gender: str  # Admin's gender
    phone_number: str  # Admin's phone number
    department: str  # Admin's department

# Update the admin's profile based on session data
class ProfileUpdateRequest(BaseModel):
    full_name: str  # Admin's full name
    birth_date: str  # Admin's birth date
    region: str  # Admin's region
    gender: str  # Admin's gender
    phone_number: str  # Admin's phone number
    department: str  # Admin's department

@app.post("/editProfile")
def update_profile(request: Request, profile_data: ProfileUpdateRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")

    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()

    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")

    # Update the admin's profile with the new data
    admin.full_name = profile_data.full_name
    admin.birth_date = profile_data.birth_date
    admin.region = profile_data.region
    admin.gender = profile_data.gender
    admin.phone_number = profile_data.phone_number
    admin.department = profile_data.department

    # Commit the changes to the database
    db.commit()
    # Return a success message after updating the profile
    return {"message": "Profile updated successfully", "status": "success"}

# End of Edit Admin Profile (All Fields)



# Start of Edit Admin (Only Name)

# Define a request model to validate the data for updating the admin's name
class UpdateNameRequest(BaseModel):
    full_name: str  # Admin's full name

@app.post("/editName")
def update_admin_name(request: Request, name_data: UpdateNameRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")
    
    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    
    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Update only the admin's name
    admin.full_name = name_data.full_name
    # Commit the changes to the database
    db.commit()
    
    # Return a success message after updating the name
    return {"message": "Name updated successfully", "status": "success"}

# End of Edit Admin (Only Name)



# Start of Edit Admin (Only Birth Date)

# Define a request model to validate the data for updating the admin's birth date
class UpdateBirthDateRequest(BaseModel):
    birth_date: str  # Admin's birth date

@app.post("/editBirthDate")
def update_admin_birth_date(request: Request, birth_data: UpdateBirthDateRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")
    
    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    
    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Update only the admin's birth date
    admin.birth_date = birth_data.birth_date
    # Commit the changes to the database
    db.commit()
    
    # Return a success message after updating the birth date
    return {"message": "Birth date updated successfully", "status": "success"}

# End of Edit Admin (Only Birth Date)



# start of Edit Admin (Only Region)

# Define a request model to validate the data for updating the admin's region
class UpdateRegionRequest(BaseModel):
    region: str  # Admin's region

@app.post("/editRegion")
def update_admin_region(request: Request, region_data: UpdateRegionRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")
    
    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    
    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Update only the admin's region
    admin.region = region_data.region
    # Commit the changes to the database
    db.commit()
    
    # Return a success message after updating the region
    return {"message": "Region updated successfully", "status": "success"}

# End of Edit Admin (Only Region)




# Start of Edit Admin (Only Gender)

# Define a request model to validate the data for updating the admin's gender
class UpdateGenderRequest(BaseModel):
    gender: str  # Admin's gender

@app.post("/editGender")
def update_admin_gender(request: Request, gender_data: UpdateGenderRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")
    
    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    
    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Update only the admin's gender
    admin.gender = gender_data.gender
    # Commit the changes to the database
    db.commit()
    
    # Return a success message after updating the gender
    return {"message": "Gender updated successfully", "status": "success"}

# End of Edit Admin (Only Gender)




# Start of Edit Admin (Only Phone Number)

# Define a request model to validate the data for updating the admin's phone number
class UpdatePhoneNumberRequest(BaseModel):
    phone_number: str  # Admin's phone number

@app.post("/editPhoneNumber")
def update_admin_phone_number(request: Request, phone_data: UpdatePhoneNumberRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")
    
    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    
    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Update only the admin's phone number
    admin.phone_number = phone_data.phone_number
    # Commit the changes to the database
    db.commit()
    
    # Return a success message after updating the phone number
    return {"message": "Phone number updated successfully", "status": "success"}

# End of Edit Admin (Only Phone Number)




# Start of Edit Admin (Only Departmeent)

# Define a request model to validate the data for updating the admin's department
class UpdateDepartmentRequest(BaseModel):
    department: str  # Admin's department

@app.post("/editDepartment")
def update_admin_department(request: Request, department_data: UpdateDepartmentRequest, db: Session = Depends(get_db)):
    # Fetch the admin_id from the session
    admin_id = request.session.get("admin_id")
    
    if not admin_id:
        # If no admin_id is found, return a 401 Unauthorized response
        raise HTTPException(status_code=401, detail="Unauthorized: No active session found.")
    
    # Search for the admin in the database
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    
    if not admin:
        # If no admin is found, return a 404 Not Found response
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Update only the admin's department
    admin.department = department_data.department
    # Commit the changes to the database
    db.commit()
    
    # Return a success message after updating the department
    return {"message": "Department updated successfully", "status": "success"}

# End of Edit Admin (Only Departmeent)




# Start of change password

class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str

@app.post("/change-password")
def change_password(request: Request, password_request: PasswordChangeRequest, db: Session = Depends(get_db)):
    """Change the password for an authenticated user."""
    # Retrieve admin_id and current password from session
    admin_id = request.session.get("admin_id")
    session_password = request.session.get("password")

    if not admin_id or not session_password:
        raise HTTPException(status_code=401, detail="No active session found.")

    # Verify old password matches current session password
    if password_request.old_password != session_password:
        raise HTTPException(status_code=400, detail="Old password is incorrect.")

    # Verify new password matches confirmation
    if password_request.new_password != password_request.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirm password do not match.")

    # Validate new password format
    password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not re.match(password_pattern, password_request.new_password):
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")

    # Update password in database
    sql_query = """
    UPDATE Admin
    SET password = :new_password
    WHERE admin_id = :admin_id
    """
    try:
        db.execute(text(sql_query), {"new_password": password_request.new_password, "admin_id": admin_id})
        db.commit()

        # Update password in session
        request.session["password"] = password_request.new_password

        return JSONResponse(content={"message": "Password updated successfully."})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update password.")


# End of change password


# =====================================================================================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)