# 🥗 Daily Diet API

RESTful API for daily diet control built with **Flask**, allowing full meal management with database persistence and organized route structure.

This project is part of a Rocketseat challenge and aims to practice advanced concepts of API development with Flask.

---

## 🎯 Project 

The system allows users to track their daily meals by registering important details for each one, such as:

- **Meal name**
- **Description**
- **Date and time**
- **Indicator whether it is within the diet or not**

The idea is to deliver a functional, well-structured API ready to be consumed by any client (web, mobile, etc.).

---

## ✅ Features


1. **Meal creation**
   - Create a new meal with:
     - `name` – meal name  
     - `description` – detailed description  
     - `datetime` – date and time of the meal  
     - `is_on_diet` – boolean indicating whether the meal is within the diet  

2. **Meal update**
   - Allow updating **all fields** of an existing meal.

3. **Meal deletion**
   - Remove a specific meal from the system.

4. **List meals**
   - List **all** meals registered for a user.

5. **View single meal**
   - Fetch and display data for **a single meal** from its identifier.

6. **Database persistence**
   - All information is stored in a MySQL database with the help of a ORM

---

## 🧱 Data Model 

`meals` table:

- `id` – integer, primary key  
- `name` – string  
- `description` – string/text  
- `created_at` – datetime  
- `is_on_diet` – boolean  


---


## 🛣️ Routes

- `POST /meals` – create a meal  
- `GET /meals/all` – list all meals  
- `GET /meals/<id>` – get a specific meal  
- `PUT /meals/<id>` – update a meal  
- `DELETE /meals/<id>` – delete a meal  



---

## 🧰 Tech Stack

- **Python** 3.12.12
- **Flask**
- **ORM** SQLAlchemy
- **Database** MySQL

---

## 🐳 Docker Requirement

You can run this project using Docker:

- Make sure **Docker** is **installed** on your machine.  
- Ensure the **Docker daemon is running** (Docker Desktop opened on Windows/macOS, or the Docker service started on Linux).  
- If a `Dockerfile` and/or `docker-compose.yml` is provided, you’ll be able to build and run the API inside a container.

---



## 🚀 How to Run 

```bash
# Clone the repository
git clone https://github.com/gabrieldborges/Daily-Diet-API
cd Daily-Diet-API

# Create and activate virtual environment (example using venv)
python3.12 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run de docker on the terminal
docker compose up

# Run the application (adjust according to your app entrypoint)
flask run
# or
python app.py
