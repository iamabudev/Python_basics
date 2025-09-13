# This program demonstrates various Python concepts using multiple functions and examples:
# 1. full_name() and full_name_ic(): Combine names with or without a middle name and return formatted full names.
# 2. auto_info(): Creates car dictionaries containing details like company, model, color, gear type, year, and price.
#The code also shows how to store and display pre-defined and user-input car data interactively.
# 3. middle(): Generates a list of numbers between two values with a customizable step.
# 4. emloyee_details(): Returns a dictionary of employee details including optional fields.
# 5. big_number(): Returns the largest of three given numbers.
# 6. cicle_info(): Calculates and returns radius, diameter, circumference, and area of a circle.
# 7. student_grades(): Takes a list of students, asks for their grades via input, and returns them in a dictionary.
# 8. summa(): Demonstrates multiple implementations of summing numbers and multiplying numbers using *args.
# 9. student_info(): Creates a dictionary of student details with required and optional fields.
# Overall, this script is a practice file showing function creation, dictionary usage, loops, conditionals,
# user input handling, and mathematical computations in Python.
def full_name(name,surname):
    detail=f"{name.title()} {surname.title()}"
    return detail

student=full_name('anna','bob')
student1=full_name('john','wilson')
print(f"Today class attended {student},{student1}")


 
def full_name_ic(name,surname,middle_name=''):
    details=f"{name.title()} {middle_name.title()} {surname.title()}"
    return details

student=full_name_ic('bob','will','jacskon')
student1=full_name_ic('lana','petor','walk')
print(f"Unattended students: {student1} {student}")

def auto_info(company,model,color,type,year,price=None):
    auto={
        'company':company,
        'model':model,
        'color':color,
        'type':type,
        'year':year,
        'price':price
    }
    return auto


auto1=auto_info('honda','city','black','auto',2022,1300)
auto2=auto_info('volvo','x30','silver','manual',2020)
aviable_auto=[auto1,auto2]
print('Welcome to E-auto shop!')
for auto in aviable_auto:
    if auto['price']:
        price=auto['price']
    else:
        price='None'
    print(f"{auto['color']} {auto['company']} {auto['model']} {auto['price']}")
print("Let's create autos list for sale!")
autos=[]
while True:
    print("Enter the showed details")
    company=input("Manufacturer name: ")
    model=input("Model name:")
    color=input("Color: ")
    type=input("Manual/Auto: ")
    year=input("Year: ")
    price=input("Price: ")


    autos.append(auto_info(company,model,color,type,year,price))

    answer=input("Do you want to add more? yes/no ")
    if answer !='yes':
        break
def middle(min,max,step=2):
    numbers=[]
    while min<max:
        numbers.append(min)
        min+=step

    return numbers

print(middle(0,11))
print(middle(10,20,2))


# a function that takes a user’s name, surname, birth year, birthplace, email, and phone (email/phone optional),
# and returns a dictionary including the user’s age.
def emloyee_details(name,surname,dob,b_place,email,address=None,number=None):
    details={
        'name':name,
        'surname':surname,
        'dob':dob,
        'b_place':b_place,
        'email':email,
        'address':address,
        'number':number
    }

    return details

employee01=emloyee_details('john','bob',1999,'washington','jbob19@gmail.com','queenland road',102303)
employee02=emloyee_details('alisa','ann',1998,'michigan','alisa98@gmail.com')
employees=[employee01,employee02]
for stuff in employees:
    if stuff['address']:
        address=stuff['address']
    else:
        address='None'
    print(f"{stuff['name'].title()} {stuff['surname'].title()} {stuff['dob']} {stuff['b_place']} {stuff['email']}")

def big_number(x,y,z):
    max=y
    if y >=max:
        max=y
    if z>=max:
        max=z
    return max

big_number(1,2,3)

# a function that accepts the radius of a circle and returns a dictionary containing its radius, diameter, circumference, and area.
import math
def cicle_info(radius):
    return {
        'radius':radius,
        'diameter':2*radius,
        'circumference':2*math.pi*radius,
        'area':math.pi *radius **2
    }

print(cicle_info(5))


# This function takes a list of student names, asks for their grades as input,
# stores them in a dictionary, and returns it without modifying the original list.
def student_grades(names):
    grade={}
    while names:
        name=names.pop()
        gradee=input(f'Enter the student grade {name.title()}:')
        grade[name]=int(gradee)
    return grade

students=['lana','anna','bob','alex']
grade=student_grades(students[:])
print(grade)
print(students)

# This function takes any number of arguments, sums them up, and returns the total.
def summa(*numbers):
    number=0
    for n in numbers:
        number+=n
    return number

print(summa(1,2,3,4,5))

# This function adds two required numbers and any extra numbers passed as arguments.
def summa(x,y,*numbers):
    return  x+y+sum(numbers)
print(summa(3,3))


# This function builds a dictionary of car information using required and optional details.
def auto_info(company,model, **details):
    details['company']=company
    details['model']=model
    return details

auto1=auto_info('ford','fortune', color='black',year=2012)
auto2=auto_info('bmw','m5',color='silver', year=2022)
print(auto1)
print(auto2)

# function that accepts any number of numbers and returns their product.
def summa(*numbers):
    result=1
    for n in numbers:
        result*=n
    return result

print(summa(2,3,4))
print(summa(2,2))

# Function that returns student information as a dictionary.
# First name and last name are required, other details are optional.
def student_info(first_name,last_name, **details):
    details['firs_name']=first_name
    details['last_name']=last_name

    return details

student1=student_info('Lana','Smith', age=21, major='Computer Science')
student2=student_info('Bob','Johnson',grade='A',country='USA')

print(student1)








