import json
import os


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        try:
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = list(map(int, input("Enter 3 Marks (space separated): ").split()))

            if len(marks) != 3:
                print("Please enter exactly 3 marks.")
                return

            student = Student(roll_no, name, marks)
            self.students.append(student.to_dict())
            self.save_students()

            print("✅ Student Added Successfully!")

        except ValueError:
            print("❌ Invalid input! Marks must be numbers.")

    def search_student(self):
        roll_no = input("Enter Roll Number to Search: ")
        for student in self.students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found:")
                print(student)
                return
        print("❌ Student Not Found!")

    def show_all_students(self):
        if not self.students:
            print("No records available.")
            return

        for student in self.students:
            print(student)


def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Show All Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.search_student()
        elif choice == "3":
            manager.show_all_students()
        elif choice == "4":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()