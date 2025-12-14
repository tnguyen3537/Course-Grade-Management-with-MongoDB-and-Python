from datetime import datetime
import db

def pause():
    input("Action complete, press Enter to continue...")
    
# Student CRUD functions would go here (create_student, update_student, search_student, delete_student)
def create_student():
    # Ask user for student info and insert into collection.
    try:
        _id = input("Enter student ID: ")
        name = input("Enter student name: ")
        birth_date_str = input("Enter birth date (dd/mm/YYYY): ")
        email = input("Enter student email: ")

        student = {
            "_id": _id,
            "name": name,
            "birth_date": datetime.strptime(birth_date_str, "%d/%m/%Y"),
            "email": email
        }

        db.students.insert_one(student)
        print(f"Student {_id} created successfully.")
    except Exception as e:
        print(f"Error inserting student: {e}")

def update_student():
    
    # Find and validate student ID before updating.
    while True:
        student_id = input("Enter student ID to update (or 0 to return): ")
        if student_id == "0":
            return  # go back to main menu

        student = db.students.find_one({"_id": student_id})
        if not student:
            print(f"No student found with ID {student_id}. Try again or enter 0 to return.")
            continue  # loop back to ask again
        else:
            break  # valid student found

    # Update an existing student's information prompt.
    while True:
        update_fields = {}
        # Show update options
        print("\nWhat would you like to update?")
        print("1 - Name")
        print("2 - Email")
        print("3 - Birth Date")
        print("4 - All Fields")
        print("0 - Return to previous menu\n")
        choice = input("Enter your choice (0-4): ")

        if choice == "0":
            return

        if choice == "1":
            new_name = input("Enter new name: ")
            update_fields["name"] = new_name

        elif choice == "2":
            new_email = input("Enter new email: ")
            update_fields["email"] = new_email

        elif choice == "3":
            new_birth_date = input("Enter new birth date (dd/mm/YYYY): ")
            try:
                update_fields["birth_date"] = datetime.strptime(new_birth_date, "%d/%m/%Y")
            except ValueError:
                print("\nInvalid date format. Use dd/mm/YYYY.")
                continue  # loop back to ask again

        elif choice == "4":
            try:
                new_birth_date = input("Enter new birth date (dd/mm/YYYY): ")
            except ValueError:
                print("\nInvalid date format. Use dd/mm/YYYY.")
                continue  # loop back to ask again
            
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            
            update_fields["name"] = new_name 
            update_fields["birth_date"] = datetime.strptime(new_birth_date, "%d/%m/%Y")
            update_fields["email"] = new_email

        else:
            print("\nInvalid choice.")
            continue  # loop back to ask again

        # Perform update
        result = db.students.update_one({"_id": student_id}, {"$set": update_fields})
        if result.modified_count > 0:
            print(f'\n{result.modified_count} document(s) updated.')
            print(f"\nStudent {student_id} updated successfully.")
            print("Updated field(s):")
            for field, value in update_fields.items():
                print(f" - {field}: {value}")
            return
        else: 
            print(f"No changes made to student {student_id}.")
    
def delete_student():
    # Delete a student by ID after validation.
    while True:
        student_id = input("Enter student ID to delete (or 0 to return): ")
        if student_id == "0":
            return  # go back to main menu

        student = db.students.find_one({"_id": student_id})
        if not student:
            print(f"No student found with ID {student_id}. Try again or enter 0 to return.")
            continue  # loop back to ask again
        else:
            confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ")
            if confirm.lower() == 'y':
                result = db.students.delete_one({"_id": student_id})
                if result.deleted_count > 0:
                    print(f"Student {student_id} deleted successfully.")
                else:
                    print(f"Failed to delete student {student_id}.")
                return
            else:
                print("Deletion cancelled.")
                return

def search_student():
    
    myquery = {}
    
    while True:     
        print("\nWhat would you like search for student(s) by?")
        print("1 - Student ID")
        print("2 - Student Name")
        print("3 - Student Email")
        print("4 - Student DOB")
        print("5 - A combination of All Fields (AND search)")
        print("0 - Return to Student Menu")

        choice = input("Enter your choice (0-5): ")
        if choice == "0":
            return
        
        elif choice == "1":
            # Implement search by _id
            student_id = input("Enter student ID to search: ")
            myquery.clear()
            myquery = {"_id": student_id}
            
            student_doc = db.students.find(myquery)
            
            if not student_doc:
                print(f"No student found with ID {student_id}. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                for doc in student_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again  
                
        elif choice == "2":
            # Implement search by Name
            student_name = input("Enter student name to search: ")
            myquery.clear()
            myquery = {"name": student_name}
            student_doc = db.students.find(myquery)
            
            if not student_doc:
                print(f"No student found with name {student_name}. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                for doc in student_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again
                    
        elif choice == "3":
            # Implement search by Email
            student_email = input("Enter student email to search: ")
            myquery.clear()
            myquery = {"email": student_email}
            student_doc = db.students.find(myquery)
            
            if not student_doc:
                print(f"No student found with email {student_email}. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                for doc in student_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again
                    
        elif choice == "4":
            # Implement search by Birth Date
            student_dob_str = input("Enter student birth date (dd/mm/YYYY) to search: ")
            try:
                student_dob = datetime.strptime(student_dob_str, "%d/%m/%Y")
                myquery.clear()
                myquery = {"birth_date": student_dob}
                student_doc = db.students.find(myquery)

                if not student_doc:
                    print(f"No student found with birth date {student_dob_str}. Try again or enter 0 to return.")
                    continue  # loop back to ask again
                else:
                    for doc in student_doc:
                        for key, value in doc.items():
                            print(f"{key}: {value}")
                        print("\n")
                        
                    pause()
                    continue  # loop back to ask again
            except ValueError:
                print("\nInvalid date format. Use dd/mm/YYYY.")
                continue  # loop back to ask again
            
        elif choice == "5":
            # Implement search by combination of all fields
            student_id = input("Enter student ID to search (or leave blank to skip): ")
            student_name = input("Enter student name to search (or leave blank to skip): ") 
            student_email = input("Enter student email to search (or leave blank to skip): ")
            student_dob_str = input("Enter student birth date (dd/mm/YYYY) to search (or leave blank to skip): ")
            myquery.clear()
            if student_id:
                myquery["_id"] = student_id
            if student_name:
                myquery["name"] = student_name
            if student_email:
                myquery["email"] = student_email
            if student_dob_str:
                try:
                    student_dob = datetime.strptime(student_dob_str, "%d/%m/%Y")
                    myquery["birth_date"] = student_dob
                except ValueError:
                    print("\nInvalid date format. Use dd/mm/YYYY.")
                    continue  # loop back to ask again
            student_doc = db.students.find(myquery)
            if not student_doc:
                print("No student found matching the given criteria. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                for doc in student_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again
        else:
            print("Invalid choice, please try again.")

             
if __name__ == "__main__":
    pass