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
        },
    {
        "_id": "FIN002AS2AE-3028",
        "name": "Finnish Language and Culture 2",
        "teacher": "t21831",
        "topics": ["Finnish", "Finnish Level 2", "Conversational Finnish"],
        "credit": 5,
        "semester": "fall",
        "year": 2025,
        "student_grades": [
            {
                "student_id": "t54011",
                "grade": 3,
                "comments": "sucks at finnish"
            },
            {
                "student_id": "p45102",
                "grade": 3,
                "comments": "sucks at finnish"
            },
            {
                "student_id": "tn43124",
                "grade": 4,
                "comments": "ok at finnish"
            }
            ]
        },
    {
        "_id": "PLA001HH2AE-3012",
        "name": "Professional Work Placement",
        "teacher": "dr24831",
        "topics": ["Workplace", "Professional Experience"],
        "credit": 5,
        "semester": "fall, spring",
        "year": 2024,
        "student_grades": [
            {
                "student_id": "t54011",
                "grade": 5,
                "comments": "did good job at work"
            },
            {
                "student_id": "p45102",
                "grade": 5,
                "comments": "did good job at work"
            },
            {
                "student_id": "tn43124",
                "grade": 5,
                "comments": "did good job at work"
            }
        ]
    }
]



def populate_database():
    # checks if the teachers collection is empty before inserting data
    if db.teachers.count_documents({}) == 0:
        db.teachers.insert_many(teacher_data)
        print("Inserted initial teacher data.")
    else:
        print("Teacher data already exists. Skipping initial insertion.")
        
    # checks if the students collection is empty before inserting data
    if db.students.count_documents({}) == 0:
        db.students.insert_many(student_data)
        print("Inserted initial student data.")
    else:
        print("Student data already exists. Skipping initial insertion.")
        
    # checks if the courses collection is empty before inserting data
    if db.courses.count_documents({}) == 0:
        db.courses.insert_many(course_data)
        print("Inserted initial course data.")
    else:     
        print("Course data already exists. Skipping initial insertion.")
    
if __name__ == "__main__":
    populate_database()