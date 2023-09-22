class Gradebook:
    global self
    def __init__(self):
        # Initialize an empty dictionary to store student data.
        self.gradebook = {}
    
    def add_student(self, student_id, name, grade):
        # Add a new student to the gradebook.
        # Ensure the student ID is unique.
        if student_id not in self.gradebook:
            self.gradebook[student_id] = {'name': name, 'grade': grade}
        else:
            print("Student ID already exists. Use a different ID.")

    def update_grade(self, student_id, new_grade):
        # Update a student's grade by their ID.
        if student_id in self.gradebook:
            self.gradebook[student_id]['grade'] = new_grade
        else:
            print("Student ID not found.")

    def delete_student(self, student_id):
        # Delete a student from the gradebook by their ID.
        if student_id in self.gradebook:
            del self.gradebook[student_id]
        else:
            print("Student ID not found.")

    def lookup_student(self, student_id):
        # Lookup and print a student's name and grade by their ID.
        if student_id in self.gradebook:
            student_info = self.gradebook[student_id]
            print(f"Student ID: {student_id}, Name: {student_info['name']}, Grade: {student_info['grade']}")
        else:
            print("Student ID not found.")

    def list_students(self):
        # List all students in the gradebook.
        print("List of Students:")
        for student_id, student_info in self.gradebook.items():
            print(f"Student ID: {student_id}, Name: {student_info['name']}, Grade: {student_info['grade']}")

class menu:
    def menu():
        print("[1] Add Student")
        print("[2] Delete Student")
        print("[3] Lookup Student")
        print("[4] list Student(s)")
        print("[0] Exit GradeBook")

gb = Gradebook()

while True:
    menu.menu()
    choice = input("Enter your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        gb.add_student(student_id, name, grade)
    elif choice == "2":
        student_id = int(input("Enter student ID to delete: "))
        gb.delete_student(student_id)
    elif choice == "3":
        student_id = int(input("Enter student ID to lookup: "))
        gb.lookup_student(student_id)
    elif choice == "4":
        gb.list_students()

        
