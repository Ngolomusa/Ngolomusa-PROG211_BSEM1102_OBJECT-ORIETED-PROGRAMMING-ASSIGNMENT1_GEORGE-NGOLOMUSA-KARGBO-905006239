# Student Learning Portal 


class Student:
    total_students = 0                     
    University = "Limkokwing University of Creative Technology"

    def __init__(self, student_id, level, faculty):
        self.student_id = student_id
        self.level = level
        self.faculty = faculty
        Student.total_students += 1         

    def display_info(self):
        print(f"STUDENT_ID: {self.student_id} | LEVEL: {self.level} | "
              f"FACULTY: {self.faculty} | UNIVERSITY: {self.University}")

    @classmethod
    def get_total_students(cls):           
        return cls.total_students


class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def display_course(self):
        print(f"COURSE_ID: {self.course_id} | COURSE_NAME: {self.course_name} "
              f"| CREDITS: {self.credits}")


class Result:
    GRADE_SCALE = ((90, "A"), (80, "B"), (70, "C"), (50, "D"), (0, "F")) 
    def __init__(self, student, course, score): 
        self.student = student
        self.course = course
        self.score = score
        self.grade = Result.calculate_grade(score)

    @staticmethod
    def calculate_grade(score):                  
        for minimum, letter in Result.GRADE_SCALE:
            if score >= minimum:
                return letter

    def display_result(self):
        print(f"Student: {self.student.student_id} | {self.course.course_name} "
              f"| Score: {self.score} | Grade: {self.grade}")



def add_student(registry, student):
    registry[student.student_id] = student


def display_students(registry):
    for student in registry.values():
        student.display_info()


def main():
    students = {}

    print("===== STUDENT LEARNING PORTAL =====")
    print("\n--- Registered Students ---")

    s1 = Student(6789, "Year 2", "F.I.C.T - Software Engineering")
    s2 = Student(9800, "Year 1", "D.M.A.B - Photo Theory")
    s3 = Student(9090, "Year 3", "F.I.C.T - OOP")
    s4 = Student(6239, "Year 1", "B.A.B.J - Architectural Studies")
    for student in (s1, s2, s3, s4):
        add_student(students, student)

    display_students(students)
    print("Total students:", Student.get_total_students())

    print("\n--- Courses Offered ---")
    c1 = Course(34, "Computer Systems", 3)
    c2 = Course(17, "Software Engineering", 3)
    c3 = Course(5, "Photo Theory", 3)
    c1.display_course()
    c2.display_course()
    c3.display_course()

    print("\n--- Results ---")
    r1 = Result(s1, c1, 92)
    r2 = Result(s2, c2, 84)
    r3 = Result(s3, c3, 73)
    r4 = Result(s4, c1, 60)
    r5 = Result(s1, c2, 23)

    r1.display_result()
    r2.display_result()
    r3.display_result()
    r4.display_result()
    r5.display_result()


if __name__ == "__main__":
    main()
