class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        print(f"Students name is {self.name}")

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.minimum_gpa = 3.2

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print('Student added')
        else:
            print('Course full, student not added')

    def get_course_students(self):
        for i in range(len(self.students)):
            print(self.students[i].name)

    def get_average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        print(value/len(self.students))


students_array = ['Alfred', 'Anthony', 'Victor']

s1 = Students('Anthony', 12, 90)
s2 = Students('Alfred', 15, 91)
s3 = Students('Victor', 13, 82)

s1.get_details()


# COURSE
science = Course('Science', 2)
science.add_student(s1)
science.add_student(s2)
science.add_student(s3)
science.get_course_students()
science.get_average()
