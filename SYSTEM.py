
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

class Teacher:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students_enrolled = []

    def enroll_student(self, student):
        self.students_enrolled.append(student)

student1 = Student("BUSHRA", "123")
course1 = Course("Math", "MATH101")
teacher1 = Teacher("ASMA", "T001")

student1.enroll(course1)
teacher1.assign_course(course1)
course1.enroll_student(student1)

print(student1.name, "is enrolled in", course1.name, "taught by", teacher1.name)

student1 = Student("BUSHRA", "123")
course2 = Course("URDU", "MATH101")
teacher2 = Teacher("LAIBA", "T001")

student1.enroll(course1)
teacher2.assign_course(course1)
course2.enroll_student(student1)

print(student1.name, "is enrolled in", course2.name, "taught by", teacher2.name)


