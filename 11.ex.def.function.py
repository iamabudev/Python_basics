#1 Introduction function
def greetings():
    """Greeting function at function"""
    print("Hello Function")

greetings()



#2
def user(name):
    """passing value to function
    and value start with upper case letter"""
    print(f"Welcome {name.title()}")

user('john')
user('mickey')


#3
def family(name,surname,age):
    """family members list function accept name,surname,age"""
    print(f"Family member name: {name.title()}\n"
          f"Family member surname: {surname.title()}\n"
          f"Family member age:{age}")

family('bob', 'morley', 55)
family('leila', 'morley', 40)
family('alex', 'morley', 19)



#4
def calculate_age(birth_year, current_year=2024):
    """Calculate your age with current year"""
    print(f"You're {current_year-birth_year} years old")

calculate_age(birth_year=2005)
calculate_age(2000)



#5
def calculate_birth(name,age):
    """Enter age  it will calculate birth of year """
    print(f"{name.title()} was born in {2024-age}.")

calculate_birth('anna', 15)


#6
def enter_number(number1):
    """A function that consoles the square and cube of an input number"""
    print(f"calculate square= {number1**2}, calculate cube ={number1**3}")

enter_number(2)


#7
def even_numb(number):
    """A function that checks whether the input number is even or odd"""
    if number % 2:
        print(f"{number} odd number")
    else:
        print(f"{number} even number")


even_numb(11)
even_numb(123)


#Write a function that takes two numbers from the user and consoles the larger of them
def compare_numbers(number1,number2):
    if number1 < number2:
        print(f"{number2} is large numbe")
    elif number1 > number2:
        print(f"{number1} large number")
    else:
        print(f"Numbers equal")

number1 =float(input("Enter first number: "))
number2= float(input("Enter second number: "))

compare_numbers(number1, number2)

#Taking the numbers x and y from the us x**y, write a function that consoles .
def multiple_numbers(x,y):
    print(f"{x} ** {y}-amount equal {x**y}")

multiple_numbers(2,2)
multiple_numbers(1, 1)



#In the  function, give a default value of 2 for y.
def multiple_numbers(x,y=2):
    print(f"{x} ** {y}-amount equal {x**y}")

multiple_numbers(4,2)
multiple_numbers(6, 8)


# this function takes number and number is divisible by 2 to 10.
def divison_numbers(number):
    """Write a function that takes a number from the user and checks whether the number is divisible by 2 to 10 without a remainder.
     Output the results to the console."""
    for n in range(2,11):
        if not number %n:
            print(f"{n} number without residue")


divison_numbers(20)




