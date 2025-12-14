from datetime import datetime
from db import db

def pause():
    input("Action complete, press Enter to continue...")

# Teacher CRUD functions

def create_teacher():
    # Ask user for teacher info and insert into collection.
    try:
        _id = input("Enter teacher ID: ")
        name = input("Enter teacher name: ")
        birth_date_str = input("Enter birth date (dd/mm/YYYY): ")
        email = input("Enter teacher email: ")

        teacher = {
            "_id": _id,
            "name": name,
            "birth_date": datetime.strptime(birth_date_str, "%d/%m/%Y"),
            "email": email
        }

        db.teachers.insert_one(teacher)
        print(f"Teacher {_id} created successfully.")
    except Exception as e:
        print(f"Error inserting teacher: {e}")


def update_teacher():

    # Find and validate teacher ID before updating."""
    while True:
        teacher_id = input("Enter teacher ID to update (or 0 to return): ")
        if teacher_id == "0":
            return  # go back to main menu

        teacher = db.teachers.find_one({"_id": teacher_id})
        if not teacher:
            print(f"No teacher found with ID {teacher_id}. Try again or enter 0 to return.")
            continue  # loop back to ask again
        else:
            break  # valid teacher found

    # Update an existing teacher's information prompt.
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
                update_fields["birth_date"] = datetime.strptime(new_birth_date, "%d/%m/%Y")
            except ValueError:
                print("\nInvalid date format. Use dd/mm/YYYY.")
                continue  # loop back to ask again
            
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            
            update_fields["name"] = new_name
            update_fields["email"] = new_email

        else:
            print("\nInvalid choice.")
            continue  # loop back to ask again

        # Perform update
        result = db.teachers.update_one({"_id": teacher_id}, {"$set": update_fields})
        if result.modified_count > 0:
            print(f'\n{result.modified_count} document(s) updated.')
            print(f"\nTeacher {teacher_id} updated successfully.")
            print("Updated field(s):")
            for field, value in update_fields.items():
                print(f" - {field}: {value}")
            return
        else: 
            print(f"No changes made to teacher {teacher_id}.")
            return
            
def delete_teacher():
    # Delete a teacher by ID after validation.
    while True:
        teacher_id = input("Enter teacher ID to delete (or 0 to return): ")
        if teacher_id == "0":
            return  # go back to main menu

        teacher = db.teachers.find_one({"_id": teacher_id})
        if not teacher:
            print(f"No teacher found with ID {teacher_id}. Try again or enter 0 to return.")
            continue  # loop back to ask again
        else:
            confirm = input(f"Are you sure you want to delete teacher {teacher_id}? (y/n): ")
            if confirm.lower() == 'y':
                result = db.teachers.delete_one({"_id": teacher_id})
                if result.deleted_count > 0:
                    print(f"Teacher {teacher_id} deleted successfully.")
                else:
                    print(f"Failed to delete teacher {teacher_id}.")
                return
            else:
                print("Deletion cancelled.")
                return
                    
def search_teacher():
    """Ask user how they want to search for teachers by"""
    myquery = {}
    while True:     
        print("\nWhat would you like search for teacher(s) by?")
        print("1 - _id")
        print("2 - Name")
        print("3 - Email")
        print("4 - Birth Date")
        print("5 - A combination of All Fields (AND search)")
        print("0 - Return to previous menu\n")
        
        choice = input("Enter your choice (0-5): ")
        if choice == "0":
            return
        
        elif choice == "1":
            # Implement search by _id
            teacher_id = input("Enter teacher ID to search: ")
            myquery.clear()
            myquery = {"_id": teacher_id}
            
            teacher_doc = db.teachers.find(myquery)
            teacher_doc_count = db.teachers.count_documents(myquery)
            
            if teacher_doc_count == 0:
                print(f"No teacher found with ID \"{teacher_id}\". Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                for doc in teacher_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                pause()
                continue  # loop back to ask again  
                
        elif choice == "2":
            # Implement search by Name
            teacher_name = input("Enter teacher name to search: ")
            myquery.clear()
            myquery = {"name": teacher_name}
            teacher_doc = db.teachers.find(myquery)
            
            if not teacher_doc:
                print(f"No teacher found with name {teacher_name}. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                print()
                for doc in teacher_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again
                    
        elif choice == "3":
            # Implement search by Email
            teacher_email = input("Enter teacher email to search: ")
            myquery.clear()
            myquery = {"email": teacher_email}
            teacher_doc = db.teachers.find(myquery)
            
            if not teacher_doc:
                print(f"No teacher found with email {teacher_email}. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                print()
                for doc in teacher_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again
                    
        elif choice == "4":
            # Implement search by Birth Date
            teacher_dob_str = input("Enter teacher birth date (dd/mm/YYYY) to search: ")
            try:
                teacher_dob = datetime.strptime(teacher_dob_str, "%d/%m/%Y")
                myquery.clear()
                myquery = {"birth_date": teacher_dob}
                teacher_doc = db.teachers.find(myquery)
                
                if not teacher_doc:
                    print(f"No teacher found with birth date {teacher_dob_str}. Try again or enter 0 to return.")
                    continue  # loop back to ask again
                else:
                    print()
                    for doc in teacher_doc:
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
            teacher_id = input("Enter teacher ID to search (or leave blank to skip): ")
            teacher_name = input("Enter teacher name to search (or leave blank to skip): ") 
            teacher_email = input("Enter teacher email to search (or leave blank to skip): ")
            teacher_dob_str = input("Enter teacher birth date (dd/mm/YYYY) to search (or leave blank to skip): ")
            myquery.clear()
            if teacher_id:
                myquery["_id"] = teacher_id
            if teacher_name:
                myquery["name"] = teacher_name
            if teacher_email:
                myquery["email"] = teacher_email
            if teacher_dob_str:
                try:
                    teacher_dob = datetime.strptime(teacher_dob_str, "%d/%m/%Y")
                    myquery["birth_date"] = teacher_dob
                except ValueError:
                    print("\nInvalid date format. Use dd/mm/YYYY.")
                    continue  # loop back to ask again
            teacher_doc = db.teachers.find(myquery)
            if not teacher_doc:
                print("No teacher found matching the given criteria. Try again or enter 0 to return.")
                continue  # loop back to ask again
            else:
                print()
                for doc in teacher_doc:
                    for key, value in doc.items():
                        print(f"{key}: {value}")
                    print("\n")
                    
                pause()
                continue  # loop back to ask again
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    pass
