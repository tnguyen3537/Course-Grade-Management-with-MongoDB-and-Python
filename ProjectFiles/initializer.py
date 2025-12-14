from db import db
from datetime import datetime

# Initial data for teachers, students, and courses

# Sample Teachers
teacher_data = [
    {
        "_id": "j38101",
        "name": "Meady Johson",
        "birth_date": datetime(1972, 10, 10),
        "email": "mj10101982@gmail.com"
    },
    {
        "_id": "t21831",
        "name": "Tina Beaker",
        "birth_date": datetime(1981, 6, 27),
        "email": "tn0672@gmail.com"
    },
    {
        "_id": "dr24831",
        "name": "Dexter Russelburge",
        "birth_date": datetime(1967, 10, 29),
        "email": "dexrus1029@gmail.com"
    }
]

# Sample Students
student_data = [
    {
        "_id": "t54011",
        "name": "Toan Nguyen",
        "birth_date": datetime(1998, 9, 11),
        "email": "tnguyen3537@gmail.com"
    },
    {
        "_id": "p45102",
        "name": "Phuong Nguyen",
        "birth_date": datetime(1998, 10, 10),
        "email": "pnguyen45101@gmail.com"
    },
    {
        "_id": "tn43124",
        "name": "Tin Nguyen",
        "birth_date": datetime(2006, 3, 2),
        "email": "tin1967@gmail.com"
    }
]

# Sample Courses
course_data = [
    {
        "_id": "ICB004AS3AE-3009",
        "name": "Robotic Process Automation",
        "teacher": "j38101",
        "topics": ["Power Automate Cloud", "Power Automate Cloud", "Microsoft", "Robotic Automation"],
        "credit": 5,
        "semester": "fall",
        "year": 2025,
        "student_grades": [
            {
                "student_id": "t54011",  
                "grade": 4,
                "comments": "did ok, nothing exceptional"
            },
            {
                "student_id": "p45102", 
                "grade": 5,
                "comments": "excellent, did everything on point"
            }
        ]
    },
    {
            "_id": "SOF012AS2AE-3002",
            "name": "Introduction to NoSQL Databases",
            "teacher": "dr24831",
            "topics": ["NoSQL", "Python"],
            "credit": 3,
            "semester": "fall",
            "year": 2025,
            "student_grades": [
                {
                    "student_id": "t54011",  
                    "grade": 5,
                    "comments": "Exceptional"
                }
            ]
        }
    ]



def populate_database():
    db.teachers.insert_many(teacher_data)
    db.students.insert_many(student_data)
    db.courses.insert_many(course_data)

    print("Sample data inserted successfully into 'school' database.")
    
if __name__ == "__main__":
    populate_database()