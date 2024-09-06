import json

class Student:
    def __init__(self, name, rollNum, scores):
        self.name = name
        self.rollNum = rollNum
        self.scores = scores

    def average_Marks(self):
        secured_marks = sum(int(m) for m in self.scores.values())
        average_marks = secured_marks / len(self.scores)
        return average_marks

    def assign_grade(self):
        average = self.average_Marks()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.rollNum}, Scores: {self.scores}, Grade: {self.assign_grade()}"

class GradeManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                print(student)

    def search_student(self, name, rollnum):
        for student in self.students:
            if student.name.lower() == name.lower() and student.rollNum == rollnum:
                print(student)
                return student
        print("Student not found.")
        return None

    def save_records(self):
        file_name = input("Enter name of file to save: ")
        with open(file_name, "w") as f:
            json.dump([student.__dict__ for student in self.students], f)
        print(f"Records saved to {file_name}.")

    def load_records(self):
        file_name = input("Enter name of file to load: ")
        try:
            with open(file_name, "r") as f:
                student_data_list = json.load(f)
                for student_data in student_data_list:
                    student = Student(student_data["name"], student_data["rollNum"], student_data["scores"])
                    self.add_student(student)
            print(f"Records loaded from {file_name}.")
        except Exception as e:
            print(f"Error loading records: {e}")

def main():
    gms = GradeManagementSystem()
    
    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Save Records\n5. Load Records\n6. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                name = input("Enter student name: ")
                rollNum = int(input("Enter roll number of the student: "))
                
                sub_Marks = {}
                while True:
                    subject = input("Enter the subject or press 'q' to stop adding subjects: ")
                    if subject == 'q':
                        break
                    else:
                        marks = int(input(f"Enter the marks for {subject}: "))
                        sub_Marks[subject] = marks
                
                student = Student(name, rollNum, sub_Marks)
                gms.add_student(student)
                print(f"Student {name} added successfully!")
            
            case 2:
                gms.view_students()

            case 3:
                name = input("Enter the name of the student to search: ")
                rollnum = int(input("Enter the roll number of the student: "))
                gms.search_student(name, rollnum)
            
            case 4:
                gms.save_records()
            
            case 5:
                gms.load_records()
            
            case 6:
                print("Exiting the program.")
                break
            
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
