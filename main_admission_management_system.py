# admission_management_system.py

from course_manager import CourseManager
from applicant_manager import ApplicantManager

def main():
    course_manager = CourseManager()
    applicant_manager = ApplicantManager()

    print("Welcome to the Admission Management System!")
    while True:
        print("\n1. Add Applicant")
        print("2. Add Course")
        print("3. Display Applicants")
        print("4. Display Courses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter applicant's name: ")
            email = input("Enter applicant's email: ")
            phone = input("Enter applicant's phone number: ")
            applicant_manager.add_applicant(name, email, phone)
        elif choice == "2":
            name = input("Enter course name: ")
            code = input("Enter course code: ")
            course_manager.add_course(name, code)
        elif choice == "3":
            applicant_manager.display_applicants()
        elif choice == "4":
            course_manager.display_courses()
        elif choice == "5":
            print("Exiting the Admission Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
