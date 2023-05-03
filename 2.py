from typing import List
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    gender: str


class Teacher(Person):
    salary: int
    courses: List[str] = []


class Student(Person):
    grade: int
    clss:int
    courses: List[str] = []


class Course(BaseModel):
    name: str
    teacher: str
    students: List[str] = []


class School(BaseModel):
    name: str
    teachers: List[Teacher] = []
    students: List[Student] = []
    courses: List[Course] = []
    
    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)
    
    def add_student(self, student: Student):
        self.students.append(student)
    
    def add_course(self, course: Course):
        self.courses.append(course)
    
    def get_student_grade(self, student_name: str, course_name: str):
        for course in self.courses:
            if course.name == course_name and student_name in course.students:
                for student in self.students:
                    if student.name == student_name:
                        return student.grade
        return None


log ={'users':{"s1": "123","s2":"123"},'staff':{"#10":"123","#11":"123"}}

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in log['users'] and log['users'][username] == password :
        external_data={
            'school':'Xaviers',
            'name':'Joel',
            'age':'23',
            'gender':'M',
            'grade':'05',
            'clss':'12',
            'courses':['Maths','John']
        }
        user=Student(**external_data)
        print(user.dict())
        

    elif username in log['staff'] and log['staff'][username]==password :
        external_data={
            'school':'Xaviers',
            'name':'John',
            'age':'26',
            'gender':'M',
            'salary':'50000',
            'courses':['Maths']
        }
        user=Teacher(**external_data)
        print(user.dict())
       
    else:
        print("Invalid username or password")
        

login()

