class Student:
    def __init__(self, student_id, student_name, student_dob):
        self._id = student_id
        self._name = student_name
        self._dob = student_dob
        self._marks = {}

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def get_marks(self):
        return self._marks

    def add_marks(self, course_id, marks):
        self._marks[course_id] = marks


class Course:
    def __init__(self, course_id, course_name):
        self._id = course_id
        self._name = course_name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class StudentManagement:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth (dd/mm/yy): ")
        return Student(student_id, student_name, student_dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

    def input_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        for student in self._students:
            if student.get_id() == student_id:
                for course in self._courses:
                    if course.get_id() == course_id:
                        marks = float(input(f"Enter marks for {student.get_name()} in {course.get_name()}: "))
                        student.add_marks(course_id, marks)
                        print("Marks added successfully.")
                        return
        print("Student or course not found.")

    def list_courses(self):
        print("\nList of Courses:")
        for course in self._courses:
            print(f"{course.get_id()}: {course.get_name()}")

    def list_students(self):
        print("\nList of Students:")
        for student in self._students:
            print(f"{student.get_id()}: {student.get_name()}")

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        for student in self._students:
            if student.get_id() == student_id:
                print("\nStudent Marks:")
                for course_id, marks in student.get_marks().items():
                    print(f"Course ID: {course_id}, Marks: {marks}")
                return
        print("Student not found.")

    def main(self):
        num_students = self.input_number_of_students()
        self._students = [self.input_student_information() for _ in range(num_students)]

        num_courses = self.input_number_of_courses()
        self._courses = [self.input_course_information() for _ in range(num_courses)]

        while True:
            print("\nMenu:")
            print("1. Input student marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a given course")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.input_student_marks()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                print("Exit the program!")
                break
            else:
                print("Invalid choice. Please enter another one.")


if __name__ == "__main__":
    student_management = StudentManagement()
    student_management.main()
