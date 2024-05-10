# admission_process.py

from applicant import Applicant
from course import Course

class AdmissionProcess:
    def __init__(self):
        self.applicants = []
        self.courses = []

    def add_applicant(self, name, email, phone):
        applicant = Applicant(name, email, phone)
        self.applicants.append(applicant)

    def add_course(self, name, code):
        course = Course(name, code)
        self.courses.append(course)

    def display_applicants(self):
        print("List of Applicants:")
        for applicant in self.applicants:
            print(applicant)

    def display_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(course)
