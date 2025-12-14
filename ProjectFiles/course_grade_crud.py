from db import db

def pause():
    input("Action complete, press Enter to continue...")
    
# Course CRUD functions
def enter_course_grades():
    while True:
        course_id = input("Enter course ID to enter grades for (or 0 to exit): ")
        if course_id == "0":
            return  # go back to previous menu

        course = db.courses.find_one({"_id": course_id})
        if not course:
            print(f"No course found with ID {course_id}. Try again")
            continue  # loop back to ask again
        else:
            course_name = course.get("name", "Unknown Course")
            break  # valid course found

    while True:
        student_id = input("Enter student ID to enter grade for (or 0 to exit): ")
        if student_id == "0":
            return  # finish entering grades

        student = db.students.find_one({"_id": student_id})
        if not student:
            print(f"No student found with ID {student_id}. Try again")
            continue  # loop back to ask again
        else:
            student_name = student.get("name", "Student missing name")
            break # valid student found

    grade = int(input(f"Enter grade (0-5) for {student_name}({student_id}) in Course: {course_name}({course_id}): "))
    comment = input("Enter any comments for this grade (or leave blank): ")
        
    grade_entry = {
    "student_id": student["_id"],
    "grade": grade,
    "comments": comment 
    }


    result = db.courses.update_one(
            {"_id": course_id},
            {"$push": {"student_grades": grade_entry}}
        )
    if result.modified_count == 1:
        print(f"Grade {grade} entered for {student_name}({student_id}) in Course: {course_name}({course_id}).")
        return
    else:
        print("Failed to enter grade. Please try again.")

def modify_course_grades():
    while True:
        course_id = input("Enter course ID to enter grades for (or 0 to exit): ")
        if course_id == "0":
            return  # go back to previous menu

        course = db.courses.find_one({"_id": course_id})
        if not course:
            print(f"No course found with ID {course_id}. Try again")
            continue  # loop back to ask again
        else:
            course_name = course.get("name", "Unknown Course")
            break  # valid course found
    
    while True:
        student_id = input("Enter student ID to modify grade for (or 0 to exit): ")
        if student_id == "0":
            return  # finish entering grades

        student = db.students.find_one({"_id": student_id})
        if not student:
            print(f"No student found with ID {student_id}. Try again")
            continue  # loop back to ask again
        else:
            student_name = student.get("name", "Student missing name") # valid student found
            break 
    
    # Check if student grade exists in student_grades array
    student_grade = None
    for grade_entry in course.get("student_grades", []):
        if grade_entry["student_id"].lower() == student_id.lower():
            student_grade = grade_entry
            break                                                                                                                                 

    if not student_grade:
        print(f"No grade found for {student_name}({student_id}) in Course: {course_name}({course_id}).")
        return
    
    # Display current grade and comments
    print(f"Student: {student_name}\n Course: {course_name}\n Current grade: {student_grade['grade']}\n comments: {student_grade['comments']}")
    
    # Ask for new values
    new_grade = int(input("Enter new grade: "))
    new_comments = input("Enter new comments: ")
    
    result = db.courses.update_one(
        {"_id": course_id, "student_grades.student_id": student_id},
        {"$set": {"student_grades.$.grade": new_grade, "student_grades.$.comments": new_comments}}
    )

    if result.modified_count == 1:
        print(f"Grade modified for {student_name}({student_id}) in Course: {course_name}({course_id}).")
        return
    else:
        print("Failed to modify grade. Please try again.")

def delete_course_grades():
    while True:
        course_id = input("Enter course ID to delete grades from (or 0 to exit): ")
        if course_id == "0":
            return  # go back to previous menu

        course = db.courses.find_one({"_id": course_id})
        if not course:
            print(f"No course found with ID {course_id}. Try again")
            continue  # loop back to ask again
        else:
            course_name = course.get("name", "Unknown Course")
            break  # valid course found
    
    while True:
        student_id = input("Enter student ID to delete grade for (or 0 to exit): ")
        if student_id == "0":
            return  # finish entering grades
        
        student = db.students.find_one({"_id": student_id})
        if not student:
            print(f"No student found with ID {student_id}. Try again")
            continue  # loop back to ask again
        else:
            student_name = student.get("name", "Student missing name")

        # Check if student grade exists in student_grades array
        student_grade = None
        for grade_entry in course.get("student_grades", []):
            if grade_entry["student_id"] == student_id:
                student_grade = grade_entry
                print(f"Deleting grade for student {student_id} in Course: {course_name}({course_id})...")
                break
        if not student_grade:
            print(f"No grade found for student ID {student_id} in Course: {course_name}({course_id}). Try again")
            return
       
            
    # Use $pull to remove the matching grade entry

        result = db.courses.update_one(
            {"_id": course_id},
            {"$pull": {"student_grades": {"student_id": student_id}}}
        )

        if result.modified_count == 1:
            print(f"Grade deleted for {student_name}({student_id}) in Course: {course_name}({course_id}).")
            return
        else:
            print("Failed to delete grade. Please try again.")
            
def view_course_grades():
    while True:
        course_id = input("Enter course ID to view grades for (or 0 to exit): ")
        if course_id == "0":
            return  # go back to previous menu

        course = db.courses.find_one({"_id": course_id})
        if not course:
            print(f"No course found with ID {course_id}. Try again")
            continue  # loop back to ask again
        else:
            course_name = course.get("name", "Unknown Course")
            break  # valid course found

    print(f"\nGrades for Course: {course_name}({course_id}):\n")
    student_grades = course.get("student_grades", [])
    if not student_grades:
        print("No grades found for this course.")
        return

    print(f"Number of Grades Entered: {len(student_grades)}\n")
    print("Student Grades:")
    
    for grade_entry in student_grades:
        student_id = grade_entry["student_id"]
        grade = grade_entry["grade"]
        comments = grade_entry.get("comments", "")
        
        # Fetch student name
        student = db.students.find_one({"_id": student_id})
        student_name = student.get("name", "Unknown Student") if student else "Unknown Student"
        
        print(f"Student: {student_name}({student_id}) - Grade: {grade} \n Comments: {comments}")