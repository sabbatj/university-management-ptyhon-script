class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return f"Person(ID: {self.id}, Name: {self.name}, Age: {self.age})"


class Student(Person):
    def __init__(self, name, age, id, major):
        super().__init__(name, age, id)
        self.major = major
        self.enrolled_courses = []

    def enroll(self, course):
        if course.add_student(self):
            self.enrolled_courses.append(course)

    def drop(self, course):
        if course.remove_student(self):
            self.enrolled_courses.remove(course)

    def __str__(self):
        courses = ', '.join([course.course_code for course in self.enrolled_courses])
        return f"Student(ID: {self.id}, Name: {self.name}, Major: {self.major}, Enrolled Courses: {courses})"


class Professor(Person):
    def __init__(self, name, age, id, department):
        super().__init__(name, age, id)
        self.department = department
        self.courses_teaching = []

    def assign_course(self, course):
        course.professor = self
        self.courses_teaching.append(course)

    def __str__(self):
        courses = ', '.join([course.course_code for course in self.courses_teaching])
        return f"Professor(ID: {self.id}, Name: {self.name}, Department: {self.department}, Courses Teaching: {courses})"


class Course:
    def __init__(self, course_code, name, max_capacity):
        self.course_code = course_code
        self.name = name
        self.max_capacity = max_capacity
        self.professor = None
        self.enrolled_students = []

    def add_student(self, student):
        if len(self.enrolled_students) < self.max_capacity:
            self.enrolled_students.append(student)
            return True
        return False

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            return True
        return False

    def __str__(self):
        students = ', '.join([student.name for student in self.enrolled_students])
        professor = self.professor.name if self.professor else "None"
        return f"Course(Code: {self.course_code}, Name: {self.name}, Capacity: {self.max_capacity}, Professor: {professor}, Enrolled Students: {students})"


class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        self.professors = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def get_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course
        return None

    def __str__(self):
        courses = '\n'.join([str(course) for course in self.courses])
        students = '\n'.join([str(student) for student in self.students])
        professors = '\n'.join([str(professor) for professor in self.professors])
        return f"University: {self.name}\nCourses:\n{courses}\nStudents:\n{students}\nProfessors:\n{professors}"


# Demo script
if __name__ == "__main__":
    # Create a University instance
    my_university = University("Tech University")

    # Create courses
    course1 = Course("CS101", "Introduction to Computer Science", 30)
    course2 = Course("MATH101", "Calculus I", 40)
    course3 = Course("PHYS101", "General Physics I", 35)

    # Add courses to the university
    my_university.add_course(course1)
    my_university.add_course(course2)
    my_university.add_course(course3)

    # Create students
    student1 = Student("Alice", 20, "S001", "Computer Science")
    student2 = Student("Bob", 22, "S002", "Mathematics")
    student3 = Student("Charlie", 19, "S003", "Physics")

    # Add students to the university
    my_university.add_student(student1)
    my_university.add_student(student2)
    my_university.add_student(student3)

    # Create professors
    professor1 = Professor("Dr. Smith", 45, "P001", "Computer Science")
    professor2 = Professor("Dr. Johnson", 50, "P002", "Mathematics")

    # Add professors to the university
    my_university.add_professor(professor1)
    my_university.add_professor(professor2)

    # Assign courses to professors
    professor1.assign_course(course1)
    professor2.assign_course(course2)

    # Enroll students in courses
    student1.enroll(course1)
    student2.enroll(course2)
    student3.enroll(course3)

    # Drop a student from a course
    student3.drop(course3)

    # Print the state of the university
    print(my_university)
