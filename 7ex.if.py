avtos = ['audi','bmw','volvo','kia','hyundai']
for avto in avtos: # cars are inside for each car
    if avto == 'bmw':  # ... if a car is equal to a bmw ...
        print(avto.upper()) # write the name of the car in all capital letters.
    else: # otherwise...
        print(avto.title()) # Capitalize only the first letter of the car name.



"""Code will calculae the age and allow to enter if you <18"""
year = int(input("Enter your birth year: "))
if 2020-year<18: # we calculate the user's age
    print(f"Your age {2020-year}.")
    print("Unable to enter!")
else:
    print("Welcome!")


"""Create a new list cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'], print the first letter of the list elements to the console.
 Capitalize both letters for GM."""

# used !=
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

# used ==
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())


"""Ask for a user login name. If the login is admin, "Welcome, Admin. See the list of users?" output the message to the console. Otherwise, "Welcome,
{user_name}!
" output to the console."""

users = input("Please enter your user name: ")
if users.lower() == 'admin':
     print(f"Welcome back, {users.title()} Do you want check users list?")
else:
    print(f"{users.title()}, Welcome! ")



"""Ask the user to enter 2 numbers. If the two numbers are equal, print "Numbers are equal" to the console."""
number1=float(input("Enter 1st number: "))
number2=float(input("Enter 2nd number: "))
if number1 == number2: print(f"Numbers equal {number1}-{number2}")



"""Ask the user to enter any number. If the number is negative, print "Negative number" to the console,
if positive,
"Positive number"""
numbers = float(input("Enter number:"))
print("The number is negative") \
    if numbers<0 \
    else print("The number is positive")


"""Ask the user to enter a number, if the number is positive, calculate its root and output it to the console.
 If the number is negative, output the message
"Enter a positive number"."""
numbers = float(input('Enter any numbers: '))
print(numbers**(1/2)) if numbers>0 else print('Enter a positive number')