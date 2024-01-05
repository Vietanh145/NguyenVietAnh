def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student Date of Birth (dd/mm/yy): ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob, 'marks': {}}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {'id': course_id, 'name': course_name}

def input_student_marks(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    for student in students:
        if student['id'] == student_id:
            for course in courses:
                if course['id'] == course_id:
                    marks = float(input(f"Enter marks for {student['name']} in {course['name']}: "))
                    student['marks'][course_id] = marks
                    print("Marks added successfully.")
                    return
    print("Student or course not found.")

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"{student['id']}: {student['name']}")

def show_student_marks(students):
    student_id = input("Enter student ID: ")
    for student in students:
        if student['id'] == student_id:
            print("\nStudent Marks:")
            for course_id, marks in student.get('marks', {}).items():
                print(f"Course ID: {course_id}, Marks: {marks}")
            return
    print("Student not found.")

def main():
    students = [input_student_information() for _ in range(input_number_of_students())]
    courses = [input_course_information() for _ in range(input_number_of_courses())]

    while True:
        print("\nMenu:")
        print("1. Input student marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            input_student_marks(students, courses)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks(students)
        elif choice == '5':
            print("Exit the program!")
            break
        else:
            print("Invalid choice. Please enter another ones.")

if __name__ == "__main__":
    main()
