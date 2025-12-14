# Academic Course Grade Management using MongoDB database

## 📌 Overview

This application connects to a local **MongoDB database** and manages three collections:

- **Teachers**
- **Students**
- **Courses**

It provides full **CRUD (Create, Read, Update, Delete)** functionality through a simple **command-line user interface**.  
The program is **menu-driven**, allowing users to interactively manage records.  
The goal is to illustrate how to work with **NoSQL data** in Python using **PyMongo**.

---

## 🗂️ ER Diagram

![ER Diagram](ProjectFiles\ERD.jpg)

---

## ⚙️ Features

- **Teacher Collection**

  - Add new teacher records with ID, name, birth date, and email
  - Search and view teacher details
  - Update teacher information (name, email, birth date, or all fields)
  - Delete teacher records with validation

- **Student Collection**

  - Insert new student with ID, name, birth date, and email
  - Search and view student details
  - Update student records interactively
  - Delete student records with validation

- **Course Collection**

  - Add course grade entries linked to teachers and students
  - Search and view course and course grade records
  - Update grades or course details
  - Delete course records with validation

- **Technical Details and Intruction**
  - First, install the PyMongo package by running the follwoing command:
    ```bash
    python -m pip install pymongo
    ```
  - Next, open and run the main_program.py file
  - Once executed, the program will initalize by populating sample data into MongoClient("mongodb://localhost:27017/"), creating a database named "school" and 3 collections: teachers, students, and courses
  - Sample data specifications can be found in [initializer.py](ProjectFiles/initializer.py)

---
