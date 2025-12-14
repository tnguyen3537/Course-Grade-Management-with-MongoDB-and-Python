from db import db

def pause():
    input("Action complete, press Enter to continue...")

# Course CRUD functions

def create_course():
    # Ask user for course info and insert into collection.
    while True: 
        # Find and validate teacher ID before adding new course.
        teacher_id = input("Enter teacher ID to add course for (or 0 to return): ")
        if teacher_id == "0":
            return  # go back to previous menu

        teacher = db.teachers.find_one({"_id": teacher_id})
        if not teacher:
            print(f"No teacher found with ID {teacher_id}. Try again or enter 0 to return.")
            continue  # loop back to ask again
        else:
            break  # valid teacher found
    # Gather course details
    while True:
        try:
            _id = input("Enter new course ID: ")
            name = input("Enter new course name: ")
            topics = input("Enter course topics (comma-separated): ").split(",")
            credits = int(input("Enter course credits: "))
            semester = input("Enter semester (e.g., Fall): ")
            year = int(input("Enter year (e.g., 2025): "))

            course = {
                    "_id": _id,
                    "name": name,
                    "teacher_id": teacher_id,
                    "topics": [topic.strip() for topic in topics],
                    "credits": credits,
                    "semester": semester,
                    "year": year
                }

            db.courses.insert_one(course)
            print(f"Course {_id} created successfully.")
            return # course created, exit function
        except Exception as e:
            print(f"Error inserting course: {e}")
            continue  # loop back to try again

def update_course():
    # Find and validate course ID before updating.
    while True:
        course_id = input("Enter course ID to update (or 0 to return): ")
        if course_id == "0":
            return  # go back to previous menu

        course = db.courses.find_one({"_id": course_id})
        if not course:
            print(f"No course found with ID {course_id}. Try again")
            continue  # loop back to ask again
        else:
            break  # valid course found

    # Update an existing course's information prompt.
    while True:
        update_fields = {}
        # Show update options
        print("\nSelect fields to update:")
        print("1 - Name")
        print("2 - Topics")
        print("3 - Credits")
        print("4 - Semester")
        print("5 - Year")
        print("6 - Update all fields (will prompt for each, leaving unchanged if blank)")
        print("0 - Return to previous menu\n")
        
        update_fields.clear()
        
        try:
            choice = input("Enter your choice (0-5): ")
            if choice == "0":
                return  # go back to main menu
            elif choice == "1":
                new_name = input("Enter new course name: ")
                update_fields["name"] = new_name
            elif choice == "2":
                new_topics = input("Enter new topics (comma-separated): ").split(",")
                update_fields["topics"] = [topic.strip() for topic in new_topics]
            elif choice == "3":
                new_credits = int(input("Enter new credits: "))
                update_fields["credits"] = new_credits
            elif choice == "4":
                new_semester = input("Enter new semester: ")
                update_fields["semester"] = new_semester
            elif choice == "5":
                new_year = int(input("Enter new year: "))
                update_fields["year"] = new_year
            elif choice == "6":
                new_name = input("Enter new course name (leave blank to keep current): ")
                if new_name:
                    update_fields["name"] = new_name

                new_topics = input("Enter new topics (comma-separated, leave blank to keep current): ")
                if new_topics:
                    update_fields["topics"] = [topic.strip() for topic in new_topics.split(",")]

                new_credits = input("Enter new credits (leave blank to keep current): ")
                if new_credits:
                    update_fields["credits"] = int(new_credits)

                new_semester = input("Enter new semester (leave blank to keep current): ")
                if new_semester:
                    update_fields["semester"] = new_semester

                new_year = input("Enter new year (leave blank to keep current): ")
                if new_year:
                    update_fields["year"] = int(new_year)
            else:
                print("Invalid choice, please try again.")
                continue  # loop back to show again
            
            # Perform update if there are fields to update
            if update_fields:
                db.courses.update_one({"_id": course_id}, {"$set": update_fields})
                print(f"Course {course_id} updated successfully.")
                print("Updated field(s):")
                for field, value in update_fields.items():
                    print(f"- {field}: {value}")
            else:
                print(f"No changes made to course {course_id}.")
            return  # exit function after update
                
        except Exception as e:
            print(f"Error inserting course: {e}")
            continue  # loop back to try again

def delete_course():
    # Delete a course by ID after validation.
    while True:
        course_id = input("Enter course ID to delete (or 0 to return): ")
        if course_id == "0":
            return  # go back to previous menu

        course = db.courses.find_one({"_id": course_id})
        if not course:
            print(f"No course found with ID {course_id}. Try again or enter 0 to return.")
            continue  # loop back to ask again
        else:
            break  # valid course found

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete course {course_id}? (y/n): ")
    if confirm.lower() == "y":
        db.courses.delete_one({"_id": course_id})
        print(f"Course {course_id} deleted successfully.")
    else:
        print(f"Deletion of course {course_id} cancelled.")

def search_courses():
    # Search for courses by name or teacher ID.
    while True:
        print("\nSearch Courses by:")
        print("1 - Course ID")
        print("2 - Course Name")
        print("3 - Teacher ID")
        print("0 - Return to previous menu\n")

        myquery = {}
        
        choice = input("Enter your choice (0-3): ")
        if choice == "0":
            return  # go back to previous menu
        elif choice == "1":
            course_id = input("Enter course ID to search for: ")
            myquery = {"_id": course_id}
            results = db.courses.find(myquery)
            result_count = db.courses.count_documents(myquery)
        elif choice == "2":
            course_name = input("Enter course name to search for: ")
            myquery = {"name": {"$regex": course_name, "$options": "i"}}
            results = db.courses.find(myquery)
            result_count = db.courses.count_documents(myquery)
        elif choice == "3":
            teacher_id = input("Enter teacher ID to search for: ")
            myquery = {"teacher_id": teacher_id}
            results = db.courses.find(myquery)
            result_count = db.courses.count_documents(myquery)
        else:
            print("Invalid choice, please try again.")
            continue  # loop back to show again

        # Display results
        print()
        if result_count == 0:
            print("No courses found matching the criteria.")
        else:
            print(f"\nFound {result_count} course(s):")
            for course in results:
                for key, value in course.items():
                    if key == "topics":
                        print(f"{key}: {', '.join(value)}")
                    else:
                        print(f"{key}: {value}")
                    print("-" * 20)
        pause()

            
if __name__ == "__main__":
    pass