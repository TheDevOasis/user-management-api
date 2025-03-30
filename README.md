# user-management-api  
User Management API Project (Flask + MySQL + Docker)  

Description:  
Create an API REST with Flask that allows us to create, empty, update and eliminate problems (CRUD).   
The API is connected to a base of data MySQL using SQLAlchemy like ORM, and the project is dockerized    
to facilitate the design.
It includes:  
✅ Project Structure  
✅ Flask App with RESTful Endpoints  
✅ MySQL Database Integration  
✅ Dockerization (Dockerfile + Docker Compose)  
✅ Environment Variables  
✅ JWT Authentication  
✅ Basic CRUD Operations  
__________________________________________________________________________________________________
📂 Project Structure  
├── user-management-api/       # Root directory  
│   ├── venv/                  # Virtual environment (optional but recommended)  
│   ├── app/                               
│   │   ├── __init__.py        # Initialize Flask App  
│   │   ├── config.py          # Configuration file(database, secret keys, etc.)  
│   │   ├── models.py          # Database models   
│   │   ├── routes.py          # Create routes for API  
│   │   ├── auth.py            # Authentication  
│   │   ├── db.py              # Create Database  
│   ├── requirements.txt       # Dependencies  
│   ├── Dockerfile             # Create & configure Docker image   
│   ├── docker-compose.yml     # Run Docker Container  
│   ├── .env                   # Environment variables (optional)  
│   ├── run.py                 # Main Flask application  
│   ├── README.md              # Project documentation   
___________________________________________________________________________________________________
🚀 Development Step by Step  

Step 1️⃣: Update the System and Install Python  
Before installing Flask, ensure Python and pip are up to date (Terminal Linux):   
sudo apt update && sudo apt upgrade -y  
sudo apt install python3 python3-pip -y  

Step 2️⃣: Create a Virtual Environment (Recommended)  
Using a virtual environment helps avoid conflicts between dependencies:  

mkdir user-management-api  
cd user-management-api  
python3 -m venv venv  
python3 -m venv venv      # For Linux/Mac  
venv\Scripts\activate     # For Windows  

Step 3️⃣: Install Flask, SQLAlchemy, and MySQL Connector  

Inside the virtual environment (Linux), install the required packages:  

pip install Flask Flask-SQLAlchemy Flask-JWT-Extended PyMySQL  

Step 4️⃣:  Set Up app/config.py Configuration the Datebase  in VS and navigate to your Project directory  

code .

Step 5️⃣:  Create the User Model for Database app/models.py  
Step 6️⃣:  Initialize Flask App in VS Code app/__init__.py    
Step 7️⃣:  Create Database app/db.py  
Step 8️⃣:  Create routes for API app/routes.py (Define API Routes)  
Step 9️⃣:  Create Authentication app/auth.py   
Step 9️⃣:  Create Entry Point to Tun the App run.py  
Step 10:  Dockerize the Project  Dockerfile (Use the official Python image as base)  
Step 11: Create docker-compose.yml  
Step 12:  Set up the dependencies requirements.txt   
Step 13:  Create and set the Environment Variables .env       
Step 14: Build & Run Project with Docker

Run  docker-compose ip –-build  
1.	Open http://127.0.0.1:5000  from Browser & check the JSON message:   
2.	From Terminal Ubuntu curl -X GET http://127.0.0.1:5000
     
Step 15: Test API with Postman or Curl    

🔹 Summary  
✅ Flask is used to create the REST API.  
✅ SQLAlchemy connects to MySQL.  
✅ Virtual environment keeps dependencies organized.  
✅ Docker allows containerized deployment.  
