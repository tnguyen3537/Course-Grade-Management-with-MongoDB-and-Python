import teacher_crud
import student_crud
import course_crud
import course_grade_crud
import initializer
        
def pause():
    input("Press Enter to continue...")
    
def teacher_menu():
    while True:
        print("\nTeacher Menu:")
        print("1 - Search for Teacher(s)")
        print("2 - Create Teacher")
        print("3 - Update Teacher")
        print("4 - Delete Teacher")
        print("0 - Return to Main Menu\n")
        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            teacher_crud.search_teacher()
            pause()
        elif choice == "2":
            teacher_crud.create_teacher()
            pause()
        elif choice == "3":
            teacher_crud.update_teacher()
            pause()
        elif choice == "4":
            teacher_crud.delete_teacher()
            pause()
        elif choice == "0":
            break
        else:
            print("Invalid choice, please try again.")

def student_menu():
    while True:
        print("\nStudent Menu.\n")
        print("1 - Search for Student(s)")
        print("2 - Create Student")
        print("3 - Update Student")
        print("4 - Delete Student")
        print("0 - Return to Main Menu\n")
        choice = input("Enter your choice (0-4): ")
        
        if choice == "1":
            student_crud.search_student()
            pause()
        elif choice == "2":
            student_crud.create_student()
            pause()
        elif choice == "3":
            student_crud.update_student()
            pause()
        elif choice == "4":
            student_crud.delete_student()
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice, please try again.")
            
def course_menu():
    while True:
        print("\nCourse Menu.\n")
        print("1 - Search for Course(s)")
        print("2 - Create Course")
        print("3 - Update Course")
        print("4 - Delete Course")
        print("5 - Enter Course Grade")
        print("6 - Modify Course Grade")
        print("7 - Delete Course Grade")
        print("8 - View Course Grades")
        print("0 - Return to Main Menu\n")
        choice = input("Enter your choice (0-4): ")
        
        if choice == "1":
            course_crud.search_courses()
            pause()
        elif choice == "2":
            course_crud.create_course()
            pause()
        elif choice == "3":
            course_crud.update_course()
            pause()
        elif choice == "4":
            course_crud.delete_course()
            pause()
        elif choice == "5":
            course_grade_crud.enter_course_grade()
            pause()
        elif choice == "6":
            course_grade_crud.modify_course_grade()
            pause()
        elif choice == "7":
            course_grade_crud.delete_course_grade()
            pause()
        elif choice == "8":
            course_grade_crud.view_course_grades()
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice, please try again.")
    
    
def main_menu():
    print("\nPlease choose an action:")
    print("1 - Teacher Menu")
    print("2 - Student Menu")
    print("3 - Course Menu")
    print("0 - Exit Application\n")

def main():
    # Dictionary mapping choices to functions
    actions = {
        "1": teacher_menu,
        "2": student_menu,
        "3": course_menu
    }

    initializer.populate_database()

    while True:
        main_menu()
        choice = input("Enter your choice (0-3): ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()   # Call the corresponding function
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()