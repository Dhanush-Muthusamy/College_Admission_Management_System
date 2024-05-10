# course_manager.py

class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, name, code):
        self.courses[code] = name

    def display_courses(self):
        print("List of Courses:")
        for code, name in self.courses.items():
            print(f"{code}: {name}")
