create database mangmentDB;
use mangmentDB;

-- Create Tables
CREATE TABLE Employee (
    employee_id INT(6) ZEROFILL NOT NULL PRIMARY KEY,
    region INT(2) ,
    recruitment_channel VARCHAR(30),
    adminId INT(6),
    DoB DATE ,
    age INT(3),
    gender VARCHAR(6) ,
    first_name VARCHAR(25) ,
    last_name VARCHAR(25) ,
    promot_id INT(3) ZEROFILL,
    depart_id INT(3) ZEROFILL 
);

CREATE TABLE Department (
    department_id INT(3) ZEROFILL NOT NULL PRIMARY KEY,
    department_name VARCHAR(20) 
);

CREATE TABLE Admin (
    admin_id INT(6) NOT NULL PRIMARY KEY,
    region VARCHAR (50),
    gender VARCHAR(6),
    full_name VARCHAR(50),
    birth_date DATE,
    age INT(3),
    phone_number VARCHAR(25),
   department VARCHAR(20),
    password VARCHAR(50)
);

CREATE TABLE Promotion (
    promotion_id INT(3) ZEROFILL NOT NULL PRIMARY KEY,
    awards_won INT(2),
    education VARCHAR(20),
    previous_year_rating FLOAT(3),
    length_of_service INT(3),
    is_promoted INT(1) DEFAULT 0
);

CREATE TABLE Training (
    training_id INT(3) ZEROFILL NOT NULL PRIMARY KEY,
    avg_training_score INT(3),
    no_of_trainings INT(3),
    depart_id INT(3) ZEROFILL,
    promot_id INT(3) ZEROFILL 
);


 ALTER TABLE Employee ADD FOREIGN KEY (adminId) REFERENCES Admin(admin_id);

ALTER TABLE Employee ADD FOREIGN KEY (promot_id) REFERENCES Promotion(promotion_id);

ALTER TABLE Employee ADD FOREIGN KEY (depart_id) REFERENCES Department(department_id);

ALTER TABLE Training ADD FOREIGN KEY (depart_id) REFERENCES
Department(department_id);

ALTER TABLE Training ADD FOREIGN KEY (promot_id) REFERENCES Promotion(promotion_id);


-- Insert Data for Departments
INSERT INTO Department VALUES 
(1, 'HR'),
(2, 'Sales & Marketing'),
(3, 'Finance'),
(4, 'Operations'),
(5, 'Technology'),
(6, 'Procurement'),
(7, 'R&D'),
(8, 'Analytics');

-- Insert Data 

INSERT INTO Admin VALUES (134819, 1, 'Female', 'Susann Schaaf', '1980-01-01', 44, 'whatsapp:+966508219195','Human Resource', 'Admin@123456');

INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (1, 0, 'Master & above', 5.0, 8, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (2, 0, 'Bachelor', 5.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (3, 0, 'Bachelor', 3.0, 7, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (4, 0, 'Bachelor', 1.0, 10, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (5, 0, 'Bachelor', 3.0, 2, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (6, 0, 'Bachelor', 3.0, 7, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (7, 0, 'Bachelor', 3.0, 5, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (8, 0, 'Master & above', 3.0, 6, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (9, 0, 'Bachelor', 4.0, 5, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (10, 0, 'Master & above', 5.0, 5, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (11, 0, 'Bachelor', 5.0, 3, 1);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (12, 0, 'Bachelor', 5.0, 5, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (13, 0, 'Master & above', 3.0, 16, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (14, 0, 'Master & above', 3.0, 7, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (15, 0, 'Bachelor', 1.0, 10, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (16, 0, 'Bachelor', 3.0, 5, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (17, 0, 'Bachelor', 1.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (18, 0, 'Bachelor', 5.0, 8, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (19, 0, 'Bachelor', 3.0, 9, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (20, 0, 'Bachelor', 3.0, 7, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (21, 0, 'Bachelor', 4.0, 11, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (22, 0, 'Bachelor', 3.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (23, 0, 'Master & above', 5.0, 7, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (24, 0, 'Bachelor', 5.0, 3, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (25, 0, 'Bachelor', 5.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (26, 0, 'Bachelor', 4.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (27, 0, 'Bachelor', 5.0, 3, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (28, 0, 'Bachelor', 5.0, 10, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (29, 0, 'Bachelor', 1.0, 2, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (30, 0, 'Bachelor', 1.0, 2, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (31, 0, 'Bachelor', 4.0, 6, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (32, 0, 'Bachelor', 5.0, 3, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (33, 0, 'Bachelor', 2.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (34, 0, 'Bachelor', 4.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (35, 0, 'Bachelor', 5.0, 3, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (36, 0, 'Master & above', 5.0, 5, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (37, 0, 'Bachelor', 5.0, 6, 1);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (38, 0, 'Bachelor', 3.0, 10, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (39, 0, 'Bachelor', 4.0, 2, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (40, 0, 'Bachelor', 4.0, 26, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (41, 0, 'Bachelor', 2.0, 2, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (42, 0, 'Bachelor', 5.0, 12, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (43, 0, 'Bachelor', 5.0, 11, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (44, 0, 'Master & above', 4.0, 4, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (45, 0, 'Bachelor', 3.0, 11, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (46, 0, 'Bachelor', 3.0, 3, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (47, 0, 'Master & above', 3.0, 12, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (48, 0, 'Bachelor', 4.0, 2, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (49, 0, 'Bachelor', 3.0, 8, 0);
INSERT INTO Promotion (promotion_id, awards_won, education, previous_year_rating, length_of_service, is_promoted) VALUES (50, 0, 'Bachelor', 3.0, 12, 0);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (764532, 7, 'sourcing', 134819, '1990-01-29', 35, 'Female', 'Betty', 'Anderson', 1, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (755117, 22, 'other', 134819, '1995-01-28', 30, 'Male', 'Patricia', 'Evans', 2, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (788520, 19, 'sourcing', 134819, '1991-01-29', 34, 'Male', 'Paul', 'White', 3, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (153752, 23, 'other', 134819, '1986-01-30', 39, 'Male', 'Kenneth', 'Baker', 4, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (379104, 26, 'other', 134819, '1980-02-01', 45, 'Male', 'Michael', 'Bailey', 5, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (248986, 2, 'sourcing', 134819, '1994-01-28', 31, 'Male', 'Patricia', 'Collins', 6, 8);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (853554, 20, 'other', 134819, '1994-01-28', 31, 'Female', 'Kimberly', 'Bell', 7, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (847701, 34, 'sourcing', 134819, '1992-01-29', 33, 'Male', 'Michelle', 'Turner', 8, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (667079, 20, 'other', 134819, '1997-01-27', 28, 'Male', 'Paul', 'Baker', 9, 8);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (876325, 1, 'sourcing', 134819, '1993-01-28', 32, 'Male', 'Edward', 'Robinson', 10, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (725667, 7, 'sourcing', 134819, '1990-01-29', 35, 'Female', 'Michelle', 'Scott', 11, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (752816, 4, 'sourcing', 134819, '1976-02-02', 49, 'Male', 'Jason', 'Adams', 12, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (241148, 29, 'other', 134819, '1986-01-30', 39, 'Male', 'Paul', 'Adams', 13, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (874120, 2, 'sourcing', 134819, '1988-01-30', 37, 'Male', 'John', 'Thomas', 14, 7);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (216728, 7, 'other', 134819, '1988-01-30', 37, 'Male', 'Alice', 'Scott', 15, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (419315, 2, 'other', 134819, '1987-01-30', 38, 'Male', 'Paul', 'Thomas', 16, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (248553, 31, 'other', 134819, '1991-01-29', 34, 'Male', 'David', 'Reed', 17, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (763443, 31, 'other', 134819, '1991-01-29', 34, 'Male', 'Joseph', 'Collins', 18, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (240445, 15, 'other', 134819, '1988-01-30', 37, 'Male', 'Sarah', 'Lee', 19, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (133429, 14, 'other', 134819, '1990-01-29', 35, 'Male', 'William', 'Harris', 20, 6);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (341084, 15, 'sourcing', 134819, '1984-01-31', 41, 'Male', 'William', 'Young', 21, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (778564, 11, 'other', 134819, '1997-01-27', 28, 'Female', 'Laura', 'Nelson', 22, 3);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (820980, 22, 'sourcing', 134819, '1986-01-30', 39, 'Male', 'Margaret', 'King', 23, 3);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (859476, 22, 'other', 134819, '1998-01-27', 27, 'Male', 'Sarah', 'Perez', 24, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (503749, 26, 'other', 134819, '1994-01-28', 31, 'Male', 'John', 'Carter', 25, 6);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (395612, 26, 'other', 134819, '1992-01-29', 33, 'Male', 'Sharon', 'White', 26, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (329513, 5, 'other', 134819, '1996-01-28', 29, 'Male', 'Susan', 'Anderson', 27, 8);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (250518, 15, 'sourcing', 134819, '1988-01-30', 37, 'Male', 'Edward', 'Baker', 28, 6);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (305687, 31, 'other', 134819, '1999-01-27', 26, 'Male', 'Dorothy', 'Harris', 29, 3);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (333260, 7, 'sourcing', 134819, '2001-01-26', 24, 'Female', 'Karen', 'Clark', 30, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (454178, 2, 'sourcing', 134819, '1968-02-04', 57, 'Male', 'Carol', 'Parker', 31, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (790869, 22, 'other', 134819, '1998-01-27', 27, 'Male', 'Charles', 'Jackson', 32, 8);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (635204, 22, 'other', 134819, '1985-01-30', 40, 'Male', 'Sharon', 'Anderson', 33, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (103689, 28, 'sourcing', 134819, '1992-01-29', 33, 'Male', 'Robert', 'White', 34, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (304408, 7, 'sourcing', 134819, '1985-01-30', 40, 'Female', 'Donna', 'Smith', 35, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (610753, 1, 'other', 134819, '1983-01-31', 42, 'Male', 'Brian', 'Harris', 36, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (586591, 28, 'sourcing', 134819, '1992-01-29', 33, 'Male', 'Alice', 'Parker', 37, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (541587, 15, 'other', 134819, '1991-01-29', 34, 'Male', 'Laura', 'Evans', 38, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (834948, 2, 'other', 134819, '2002-01-26', 23, 'Female', 'Alice', 'Taylor', 39, 4);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (578924, 2, 'sourcing', 134819, '1966-02-04', 59, 'Male', 'Michelle', 'Sanchez', 40, 1);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (748376, 2, 'other', 134819, '2001-01-26', 24, 'Male', 'Anthony', 'Reed', 41, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (499754, 2, 'other', 134819, '1981-01-31', 44, 'Male', 'Alice', 'Martinez', 42, 8);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (734314, 17, 'sourcing', 134819, '1975-02-02', 50, 'Female', 'James', 'Roberts', 43, 6);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (855683, 13, 'other', 134819, '1988-01-30', 37, 'Female', 'Joseph', 'Robinson', 44, 6);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (141226, 16, 'sourcing', 134819, '1985-01-30', 40, 'Male', 'George', 'Rodriguez', 45, 5);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (530257, 20, 'sourcing', 134819, '1995-01-28', 30, 'Male', 'Steven', 'Robinson', 46, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (627198, 2, 'sourcing', 134819, '1969-02-03', 56, 'Female', 'Dorothy', 'Allen', 47, 6);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (541348, 2, 'sourcing', 134819, '2005-01-25', 20, 'Male', 'Ruth', 'Adams', 48, 3);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (269769, 25, 'sourcing', 134819, '1994-01-28', 31, 'Female', 'Robert', 'Sanchez', 49, 2);
INSERT INTO Employee (employee_id, region, recruitment_channel, adminId, DoB, age, gender, first_name, last_name, promot_id, depart_id) VALUES (630556, 15, 'sourcing', 134819, '1985-01-30', 40, 'Male', 'Dorothy', 'Murphy', 50, 6);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (101, 49.0, 1, 2, 1);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (102, 60.0, 1, 4, 2);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (103, 50.0, 1, 2, 3);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (104, 50.0, 2, 2, 4);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (105, 73.0, 1, 5, 5);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (106, 85.0, 2, 8, 6);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (107, 59.0, 1, 4, 7);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (108, 63.0, 1, 4, 8);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (109, 83.0, 1, 8, 9);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (110, 54.0, 1, 2, 10);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (111, 50.0, 1, 2, 11);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (112, 49.0, 1, 2, 12);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (113, 80.0, 2, 5, 13);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (114, 84.0, 1, 7, 14);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (115, 60.0, 1, 4, 15);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (116, 77.0, 1, 5, 16);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (117, 51.0, 1, 2, 17);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (118, 46.0, 1, 2, 18);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (119, 59.0, 1, 4, 19);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (120, 75.0, 1, 6, 20);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (121, 57.0, 1, 4, 21);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (122, 63.0, 1, 3, 22);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (123, 59.0, 2, 3, 23);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (124, 83.0, 1, 5, 24);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (125, 68.0, 1, 6, 25);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (126, 79.0, 1, 5, 26);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (127, 80.0, 1, 8, 27);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (128, 72.0, 1, 6, 28);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (129, 60.0, 2, 3, 29);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (130, 48.0, 1, 2, 30);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (131, 58.0, 2, 4, 31);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (132, 87.0, 2, 8, 32);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (133, 47.0, 1, 2, 33);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (134, 75.0, 1, 5, 34);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (135, 47.0, 1, 2, 35);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (136, 51.0, 1, 2, 36);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (137, 51.0, 1, 2, 37);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (138, 80.0, 1, 5, 38);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (139, 57.0, 2, 4, 39);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (140, 52.0, 1, 1, 40);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (141, 48.0, 3, 2, 41);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (142, 88.0, 1, 8, 42);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (143, 71.0, 1, 6, 43);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (144, 71.0, 1, 6, 44);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (145, 80.0, 1, 5, 45);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (146, 49.0, 1, 2, 46);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (147, 73.0, 1, 6, 47);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (148, 60.0, 1, 3, 48);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (149, 48.0, 1, 2, 49);
INSERT INTO Training (training_id, avg_training_score, no_of_trainings, depart_id, promot_id) VALUES (150, 65.0, 1, 6, 50);

INSERT INTO Promotion VALUES (62, 3, 'Bachelor', 3.9, 6, 0);
INSERT INTO Promotion VALUES (74, 5, 'Bachelor', 2.6, 16, 0);
INSERT INTO Promotion VALUES (87, 7, 'Bachelor', 2.1, 17, 0);
INSERT INTO Promotion VALUES (66, 10, 'Bachelor', 2.8, 5, 0);
INSERT INTO Promotion VALUES (86, 4, 'Bachelor', 2.7, 29, 0);
INSERT INTO Promotion VALUES (64, 6,  'Master & above', 3.1, 15, 0);
INSERT INTO Promotion VALUES (69, 9,  'Master & above', 4.4, 2, 0);
INSERT INTO Promotion VALUES (95, 8,  'Bachelor', 2.5, 4, 0);
INSERT INTO Promotion VALUES (58, 0,  'Bachelor', 3.5, 30, 0);
INSERT INTO Promotion VALUES (90, 0,  'Master & above', 1.7, 5, 0);
INSERT INTO Promotion VALUES (92, 8, 'Bachelor', 4.8, 19, 0);
INSERT INTO Promotion VALUES (59, 8,  'Master & above', 4.7, 22, 0);
INSERT INTO Promotion VALUES (77, 7,  'Bachelor', 1.8, 5, 1);
INSERT INTO Promotion VALUES (54, 10,  'Master & above', 2.2, 23, 0);

INSERT INTO Employee VALUES (284213, 19, 'sourcing', 134819, '1998-12-20', 27, 'Male', 'Charlotte', 'Harris', 62, 8);
INSERT INTO Employee VALUES (860005, 15, 'other', 134819, '1989-04-07', 36, 'Male', 'Daniel', 'Lewis', 74, 7);
INSERT INTO Employee VALUES (111462, 29, 'other', 134819, '2004-11-13', 21, 'Female', 'Daniel', 'Garcia', 87, 4);
INSERT INTO Employee VALUES (219465, 27, 'sourcing', 134819, '1983-12-06', 42, 'Female', 'Alex', 'Anderson', 66, 2);
INSERT INTO Employee VALUES (304510, 2, 'sourcing', 134819, '1983-12-08', 42, 'Female', 'Emily', 'Clark', 86, 8);
INSERT INTO Employee VALUES (473845, 26, 'sourcing', 134819, '1987-03-10', 38, 'Female', 'Alex', 'Thomas', 64, 5);
INSERT INTO Employee VALUES (319771, 2, 'other', 134819, '1988-09-18', 37, 'Male', 'Alex', 'Thompson', 69, 4);
INSERT INTO Employee VALUES (299066, 16, 'other', 134819, '2002-08-17', 23, 'Female', 'Isabella', 'White', 95, 5);
INSERT INTO Employee VALUES (867911, 16, 'other', 134819, '2008-01-27', 17, 'Male', 'Matthew', 'Johnson', 58, 1);
INSERT INTO Employee VALUES (359766, 29, 'other', 134819, '1999-04-07', 26, 'Female', 'Andrew', 'Robinson', 90, 1);
INSERT INTO Employee VALUES (141901, 2, 'other', 134819, '2002-07-26', 23, 'Female', 'Jane', 'Jackson', 92, 4);
INSERT INTO Employee VALUES (954513, 2, 'other', 134819, '1983-08-09', 42, 'Female', 'Emily', 'Garcia', 59, 5);
INSERT INTO Employee VALUES (127344, 25, 'other', 134819, '1989-11-09', 36, 'Male', 'Daniel', 'Jackson', 77, 3);
INSERT INTO Employee VALUES (820396, 20, 'other', 134819, '2010-09-12', 15, 'Male', 'Michael', 'Hall', 54, 6);

INSERT INTO Training VALUES (194, 98, 3, 8, 62);
INSERT INTO Training VALUES (172, 95, 4, 7, 74);
INSERT INTO Training VALUES (166, 94, 1, 4, 87);
INSERT INTO Training VALUES (174, 93, 5, 2, 66);
INSERT INTO Training VALUES (168, 59, 3, 8, 86);
INSERT INTO Training VALUES (181, 61, 5, 5, 64);
INSERT INTO Training VALUES (173, 79, 1, 4, 69);
INSERT INTO Training VALUES (175, 61, 3, 5, 95);
INSERT INTO Training VALUES (191, 77, 9, 1, 58);
INSERT INTO Training VALUES (169, 93, 4, 1, 90);
INSERT INTO Training VALUES (164, 55, 1, 4, 92);
INSERT INTO Training VALUES (156, 73, 3, 5, 59);
INSERT INTO Training VALUES (165, 85, 4, 3, 77);
INSERT INTO Training VALUES (187, 53, 4, 6, 54);






