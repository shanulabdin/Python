# Student Course Registration System
# Author: Your Name
# Description: This program allows students to register for courses, view available courses, and see their registration details.
# Using basic Python concepts: if-else, loops, functions, and classes.

# -----------------------------
# Step 1: Define the Course class
# -----------------------------
class Course:
    def __init__(self, course_id, name, seats):
        self.course_id = course_id
        self.name = name
        self.seats = seats  # Total seats
        self.registered_students = []  # List of student IDs

    def is_available(self):
        return len(self.registered_students) < self.seats

    def register_student(self, student_id):
        if self.is_available():
            self.registered_students.append(student_id)
            return True
        else:
            return False

# -----------------------------
# Step 2: Define the Student class
# -----------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []  # List of course IDs

    def register_course(self, course):
        if course.register_student(self.student_id):
            self.courses.append(course.course_id)
            print(f"Successfully registered for {course.name}")
        else:
            print(f"Sorry, {course.name} is full!")

    def view_courses(self, course_list):
        print(f"\n{self.name}'s Registered Courses:")
        if not self.courses:
            print("No courses registered yet.")
        else:
            for cid in self.courses:
                print(f"- {course_list[cid].name}")

# -----------------------------
# Step 3: Create sample courses
# -----------------------------
courses = {
    "CS101": Course("CS101", "Introduction to Programming", 3),
    "MATH101": Course("MATH101", "Calculus I", 2),
    "PHY101": Course("PHY101", "Physics I", 2),
    "ENG101": Course("ENG101", "English Literature", 2)
}

# -----------------------------
# Step 4: Main program loop
# -----------------------------
students = {}  # Store all students

def main_menu():
    print("\n--- Student Course Registration System ---")
    print("1. Register New Student")
    print("2. Register Course for Student")
    print("3. View Student Courses")
    print("4. View Available Courses")
    print("5. Exit")

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        if student_id in students:
            print("Student ID already exists!")
        else:
            students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")

    elif choice == "2":
        student_id = input("Enter Student ID: ")
        if student_id not in students:
            print("Student not found! Register first.")
            continue
        print("\nAvailable Courses:")
        for cid, course in courses.items():
            print(f"{cid}: {course.name} (Seats left: {course.seats - len(course.registered_students)})")
        course_id = input("Enter Course ID to register: ").upper()
        if course_id in courses:
            students[student_id].register_course(courses[course_id])
        else:
            print("Invalid Course ID!")

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        if student_id in students:
            students[student_id].view_courses(courses)
        else:
            print("Student not found!")

    elif choice == "4":
        print("\nAvailable Courses:")
        for cid, course in courses.items():
            seats_left = course.seats - len(course.registered_students)
            print(f"{cid}: {course.name} (Seats left: {seats_left})")

    elif choice == "5":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")