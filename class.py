x=19
print(type(x))

world="Hello World"
print(type(world))



# Define a class called Student
class Student():
# Constructor method (__init__) to initialize a new student object with name, last name, and age (actually birth year)
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age
# Method to return the student's first name
    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age


    def full_name(self):
        return f"{self.name} {self.last_name}"

# Second definition of get_age (this overrides the first one)
# This calculates the age based on the given year and birth year
    def get_age(self,year):
        return year-self.age
    def introduce(self):
        print(f"My name is:{self.name} \nLast name is:{self.last_name} \nage:{self.age}")
student1=Student('Anna'.title(),'Mork',2000)
student2=Student('john'.title(),'will'.title(), 1998)
student3=Student('rebecca','lana',2005)
# Print the full name of student2
print(student2.full_name())
# Print the calculated age of student1 in the year 2025
print(student1.get_age(2025))



class Employee:
    def __init__(self,name,batch_id, b_year):
        self.name=name
        self.batch_id=batch_id
        self.b_year=b_year
        self.experience=2

    def set_experience(self,experience):
        self.experience = experience

    def update_experience(self):
        self.experience+=1

    def get_info(self):
        return f"Manager name:{self.name} emp_id:{self.batch_id} birth year:{self.b_year} experience:{self.experience}years"


manager=Employee('mark','0091',2000)
print(manager.get_info())


class Fan:
    def __init__(self,department):
        self.department=department
        self.employee_quantity=0
        self.candidate=[]

    def add_employee(self,manager):
        self.candidate.append(manager)
        self.employee_quantity+=1





maths=Fan("Math")
manager2=Employee('Ann','00123',1999)
manager3=Employee('Lana','001222',2002)

maths.add_employee(manager2)
maths.add_employee(manager3)

print(maths.employee_quantity)

# The Auto class represents a car, storing its model, color, engine type, price, and mileage.
# It includes methods to get and set its attributes, update mileage, and return formatted information.
# The see_methods static method lists all public methods of the class.
# The Autoshop class represents a shop that holds mult
class Auto:
    def __init__(self,model,color,engine,price,km=0):
        self.model=model
        self.color=color
        self.engine=engine
        self.price=price
        self.milage=1

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_engine(self):
        return self.engine

    def get_price(self):
        return self.price

    def set_milage(self,milage):
        self.set_milage=milage

    def update_milage(self):
         self.milage+=1

    def get_info(self):
        return f"Auto name: {self.model}\n Color: {self.color}\n Engine: {self.engine}\n Price:{self.price}\n Km:{self.milage}\n "


    def get_autos(self):
        return [x.get_info for x in self.get_autos()]

    def see_methods(klass):
        return [method for method in dir(klass) if not method.startswith('__')]

print(Auto.see_methods(Auto))


auto1=Auto('bmw','black','manual',12000)
auto2=Auto('audio', 'white','auto',1500,600)
# print(auto1.get_info())
class Autoshop:
    def __init__(self,name,address,autos):
        self.name=name
        self.address=address
        self.autos=autos


    def get_name(self):
        return self.get_name

    def get_address(self):
        return self.address

    def get_autos(self):
        return self.autos


shop=Autoshop("Autodeals",'Main Street', [auto1,auto2])

print(auto1.get_info())
print(auto2.get_info())
print(shop.get_name())
print([auto.get_info() for auto in shop.get_autos()])
print(Auto.see_methods(Auto))


# This program demonstrates object-oriented programming with inheritance and composition.
# The base class Citizen stores common attributes like name, last name, passport number, and birth year.
# The Student class inherits from Citizen, adds student-specific attributes (ID, level, address, subjects),
# and provides methods to add/remove subjects and display student info.
# Address and Subject are separate classes to represent a student's address and enrolled subjects.
# Additional classes (Proffessor, User, Admin) inherit from Citizen and override get_info() with their own details.
# The Admin class includes a special ban_user() method to block a user.
# The program creates instances of these classes, adds/removes subjects for a student,
# and demonstrates inheritance, method overriding, and interaction between objects.
class Citizen:
    def __init__(self,name, last_name,passport,b_year):
        self.name=name
        self.last_name=last_name
        self.passport=passport
        self.b_year=b_year

    def get_age(self,year):
        return year-self.b_year

person=Citizen("Anna", 'Wilson' ," AB000123", 2000)
# print(f"{person.get_info()} {person.get_age(2025)} years old")

class Student(Citizen):
    def __init__(self,name,last_name,passport,b_year,idnumber,address):
        super().__init__(name,last_name,passport,b_year)
        self.idnumber=idnumber
        self.level=1
        self.address=address
        self.subjects=[]

    def get_id(self):
        return self.idnumber

    def get_level(self):
        return self.level

    def add_subject(self,subject):
        self.subjects.append(subject)

    def remove_subject(self,subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
        else:
            print("You are not in list!")

    def get_info(self):
        info = f"Name:{self.name} \nLast name:{self.last_name}\n"
        info += f"{self.get_level()}-course \nID number {self.idnumber} passport number:{self.passport} \nBirth year:{self.b_year}"
        info+=f"Subjects: {[subject.name for subject in self.subjects]}"
        return info

class Address:

    def __init__(self,house,street,village,city):
        self.house=house
        self.street=street
        self.village=village
        self.city=city

    def get_address(self):
        address=f"{self.city}city, {self.village} village"
        address+=f"{self.street}st, {self.house}house"
        return address

class Subject:
    def __init__(self,name):
        self.name=name



student_address=Address(12,'one south','West','Birmingam',)
student=Student("Ben",'Walker',' AD00212',1998,'002202',student_address)

maths=Subject("Math")
chemistry=Subject("Chemistry")
biology=Subject("Subject")


student.add_subject(maths)
student.add_subject(biology)


student.remove_subject(chemistry)
student.add_subject(chemistry)
student.remove_subject(chemistry)

print(student.get_info())
print(student_address.get_address())


class Proffessor(Citizen):
    def __init__(self,name,last_name,passport,b_year,department):
        super().__init__(name, last_name,passport,b_year)
        self.department=department

    def get_info(self):
        return f"Proffessor: {self.name}, {self.last_name}, Department: {self.department}"


class User(Citizen):
    def __init__(self,name,last_name,passport,b_year,username):
        super().__init__(name,last_name,passport,b_year)
        self.username=username

    def get_info(self):
        return f"User: {self.username}, {self.name} {self.last_name}, Year:{self.b_year} Passport {self.passport} "


class Admin(Citizen):
    def __init__(self, name, last_name,passport,b_year,username):
        super().__init__(name,last_name,passport,b_year)
        self.username=username

    def ban_user(self,user):
        print(f"User {user.username} has been blocked")

prof=Proffessor("John", "Smith","EA0092",1978,'School of Technology')
user1=User("Abu","Hulk","PP999",2000,"abu11")
admin1=Admin("Lucy","Lee", 'FB2211',2002,'lucyadmin')

print(prof.get_info())
admin1.ban_user(user1)






