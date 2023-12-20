class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._width= width  
    def area(self):
        self.area = self.length * self.width
        print(self.area)
a1 = Rectangle(5,4)
print(a1.area())



class Car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(self.make)  
        print(self.model)  
        print(self.year)  
        
corolla = Car("Toyota", "rise", 2003)
corolla.display()


class ElectricCar(Car):
    def battery( battery_capacity):
        print(battery_capacity)
        
tesla = ElectricCar("tesla","cybertruck", 2024)
tesla.display()
tesla.battery()


class Student(object):
    def __init__(self, name, age, grade):
       
        self.name = name
        self.age = age
        self.grade = grade
        self.course = []
    def display(self):
        print(f"Name: {self.name} , Age: {self.age}, Grade: {self.grade} , Courses : {self.course}")
        
    def add_course(self, courses):
      self.course.append(courses)  
    def __del__(self):
        pass 

class Courses():
    def __init__(self, course_name, course_code , course_teacher):
        self.course_name = course_code
        self.course_code = course_name
        self.course_teacher = course_teacher
    def __repr__(self) -> str:
        return (f'{self.course_name} , {self.course_code} by {self.course_teacher}')
    def __del__(self):
        pass
class Teacher:
    def __init__(self ,name,subject):
        self.name = name
        self.subject = subject
    def __repr__(self) -> str:
        return f"{self.name} Sub : {self.subject}"
mathTeacher = Teacher("John", "Math")
engTeacher = Teacher("Doe", "Eng101")

math = Courses("Applied", 1202, mathTeacher)
english = Courses("English", 1011, engTeacher)

larry = Student("lar", 20, 4.5)
larry.add_course(english)
larry.add_course(math)
larry.display()       
        
        
        



class Bank(object):
    def __init__(self, balance):
        self._balance = balance


    def get_balance(self):
        return self._balance

    def deposit(self, deposit):
        self._balance += deposit

    def withdraw(self, withdraw):
        self._balance -= withdraw

