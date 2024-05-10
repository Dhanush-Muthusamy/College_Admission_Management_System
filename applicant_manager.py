# applicant_manager.py

class ApplicantManager:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, name, email, phone):
        self.applicants.append({"name": name, "email": email, "phone": phone})

    def display_applicants(self):
        print("List of Applicants:")
        for applicant in self.applicants:
            print(f"Name: {applicant['name']}, Email: {applicant['email']}, Phone: {applicant['phone']}")
