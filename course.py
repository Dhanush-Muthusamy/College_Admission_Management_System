# course.py

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Name: {self.name}, Code: {self.code}"
