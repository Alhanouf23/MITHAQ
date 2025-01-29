# Leveraging Machine Learning to Optimize Human Resources Management: Employee Promotion and Training Development

# Table of content

**1- Introduction**

**2- Technologies Used**

**3- Installation Procedure**

**4- Performance & Results**

**5- System Design & Architecture**

**6- Conclusion**

**7- Contributors**

**8- References**


# 1- Introduction
This project aims to enhance employee promotion and training development by integrating machine learning (ML), specifically the Random Forest (RF) model, to improve decision-making in HR management. By addressing inefficiencies and biases in traditional HR processes, the system ensures fair, transparent, and data-driven employee evaluations. It also introduces training recommendations for non-promoted employees to support their professional growth.


**Key Features**

	•	Fair Employee Promotion Process – ML-driven predictions ensure unbiased and efficient promotions.
	•	Training Recommendations – Non-promoted employees receive training suggestions based on skill gaps.
	•	High Accuracy (94.23%) – Achieved through hyperparameter tuning, SMOTE, and data preprocessing.
	•	Monthly Reports – HR receives automated insights on employee performance.
	•	User-Friendly Interface – Developed with FastAPI and an interactive web-based frontend.
	•	Security & Authentication – OTP authentication is integrated for enhanced security.

# 2- Technologies Used

**Programming Languages & Libraries**

	•	Python – Core programming language for ML and backend.
	•	Pandas & NumPy – Data processing and analysis.
	•	Scikit-learn – ML model construction, testing, and improvement.
	•	SMOTE – Balancing the dataset by oversampling the minority class.
	•	HTML, CSS, JavaScript – Interactive UI/UX design.
	•	MySQL – Relational database for structured HR data.

**Tools & Technologies**

	•	FastAPI – Web framework for backend and API integration.
	•	GitHub – Version control and repository management.
	•	Kaggle – Dataset source and Jupyter Notebook environment.
	•	Microsoft Office Suite – Report documentation, analysis, and presentations.
	•	Figma – UI/UX prototyping for a seamless user experience.
	•	Lucidchart & Draw.io – Creating system flowcharts and data flow diagrams.
	•	Canva – Visual documentation and presentations.
	•	Google Forms – Collecting feedback and user inputs.
	•	Twilio API – For communication functionalities such as OTP verification.

**System Deployment & Installation**

Requirements

	•	Python 3.7 - 3.11
	•	MySQL Server
	•	Twilio API (for OTP authentication)
	•	Virtual Environment (for dependency isolation)

Database Setup

	1.	Open MySQL and create a database named mangmentDB:

CREATE DATABASE mangmentDB;


	2.	Modify the config.py file by updating the database path and password.


# 3- Installation Procedure

**Step	macOS	Windows**

**Deployment Procedure for macOS**

        1.	Download the Model File
	
https://drive.google.com/file/d/1gg4hZkoZ8YC9p-guBjrcq1nSAj36nO88/view?usp=sharing

        2.	Move the Model File to the Model folder inside the MITHAQ folder

 MITHAQ --> Mdoel --> model file 

	3.	Navigate to the Project Directory
Open the Terminal and run:

cd /your/path/to/the/project


	4.	Create a Virtual Environment
Run the following command to create a virtual environment:

python3 -m venv venv


	5.	Activate the Virtual Environment
Use this command to activate the virtual environment:

source ./venv/bin/activate


	6.	Install Required Dependencies
Install all required dependencies by running:

pip install -r requirements.txt


	7.	Launch the System
Start the application by running:

python -m uvicorn app.main:app --reload

**Deployment Procedure for Windows**


        1.	Download the Model File
	
https://drive.google.com/file/d/1gg4hZkoZ8YC9p-guBjrcq1nSAj36nO88/view?usp=sharing

        2.	Move the Model File to the Model folder inside the MITHAQ folder

  MITHAQ --> Mdoel --> model file 

	3.	Navigate to the Project Directory
Open Command Prompt or PowerShell and run:

cd /your/path/to/the/project


	4.	Create a Virtual Environment
Run the following command to create a virtual environment:

python -m venv venv


	5.	Activate the Virtual Environment
Activate the virtual environment using this command:

.\venv\Scripts\activate


	6.	Install Required Dependencies
Install all required dependencies by running:

pip install -r requirements.txt


	7.	Launch the System
Start the application by running:

python -m uvicorn app.main:app --reload


# 4- Performance & Results

The model achieved 94.23% accuracy, outperforming previous research:
	•	81.15% accuracy in study [1]
	•	91.70% accuracy in study [2]
 
The proposed solution achieved a high accuracy of 94.23% using the same dataset in [3], surpassing previous studies (81.15% [1] and 91.70% [2])

**Confusion Matrix**

![photo_5823247566681273359_x](https://github.com/user-attachments/assets/c7852411-6221-4073-9a55-322dcc0e379a)

This matrix shows the model’s performance in classifying promotion outcomes.


**Key Optimization Techniques**

	•	Hyperparameter tuning (number of trees, max depth, feature selection).
	•	Cross-validation to ensure model consistency.
	•	SMOTE (Synthetic Minority Oversampling Technique) for data balancing.
	•	Robust data preprocessing to improve ML performance.

# 5- System Design & Architecture

To visualize the system’s workflow, below Flowchart:

![Final Flow Chart drawio (1)](https://github.com/user-attachments/assets/f4d22fe9-5b6a-42d6-ba22-2f0e8fed0cd9)


This flowchart represents the logic behind the system.


# 6- Conclusion

This project demonstrates the feasibility of machine learning-driven HR decision-making by:

	•	Enhancing accuracy and fairness in employee promotions.
	•	Providing actionable training recommendations for career development.
	•	Offering a user-friendly system that reduces HR workload.

Through data-driven insights, this system establishes a benchmark for transparent, objective, and optimized HR management.




# 7- Contributors

**Produced by F19**

Alhanouf Hammad Mutiq Alaloey            

Alya Salman Yousef Almallahi                  

Norah Abdulaziz Nasser Alammar           

Wasan Salem Abdullah Bin Owayed      


**Supervied by**

Dr. Alaa Eledeen Mohamed

# 8- References

	[1] M. A. Jafor, M. A. H. Wadud, K. Nur, and M. M. Rahman, “Employee Promotion Prediction Using Improved AdaBoost Machine Learning Approach,” AIUB Journal of Science and Engineering (AJSE), vol. 22, no. 3, pp. 258–266, Dec. 2023, doi: https://doi.org/10.53799/ajse.v22i3.781.

	[2] Muhannad Ilwani, Ghalia Nassreddine, and J. Younis, “Machine Learning Application on Employee ‎Promotion,” Mesopotamian Journal of Computer Science, pp. 106–120, Jun. 2023, doi: https://doi.org/10.58496/mjcsc/2023/013.
	
	[3] "Employees Evaluation for Promotion,” www.kaggle.com. https://www.kaggle.com/datasets/muhammadimran112233/employees-evaluation-for-promotion
