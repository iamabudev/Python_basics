# This program repeatedly asks the user to enter a number and prints its square, stopping only when the user types 'exit'.
print("A program that calculates the square of a number!")
question="Enter number"
question+="(for exit the program write (exit)): "
sign=True
while sign:
     value=input(question)
     if value=='exit':
         sign=False

     else:
         print(float(value)**2)

print("Program stopped")


# This program keeps asking the user to enter a number and prints its square.
# The loop runs forever (while True) until the user types 'exit',
# at which point the break statement immediately stops the loop and ends the program.
print("A program that calculate the square of number!")
question="Enter number"
question+="(for exit the program write (exit)): "
while True:
     value=input(question)
     if value=='exit':
         break
     else:
         print(float(value)**2)
print("Program stopped!")


# This program prints the square of numbers from 1 to 10, skipping the number 5.
numbers=list(range(1,11))
for number in numbers:
     if number==5:
         continue
     print(f"{number} calculate the square {number**2} is equal")


# This program prints even numbers from 1 to 10 using a while loop and continue.
number=0
while number<10:
     number+=1
     if number%2!=0:
         continue
     else:
         print(number)


# infinite loop
number=0
while number <10:
     if number%2!=0:
        continue
     print(number)

# This loop prints even numbers from 2 to 10
number=0
while number<10:
     number+=1
     if number%2!=0:
         continue
     print(number)


# Program keeps asking for movie names, prints them, and stops when user types "stop"
print("Welcome! Add to cart your favorite movie's name")
question="Enter the name"
question+=" (for stop the program write(stop): "
sign=True
while sign:
     value=input(question)
     if value=='stop':
         sign=False

     else:
         print(f"Your favorite movie list: {value}")

print('Program stopped')

# Program calculates square roots of positive numbers until user types "exit"
question = "A program that returns the square root of the entered number.\n"
question += "Enter a positive number "
question += "(to stop the program type 'exit'): "

while True:
     value = input(question)
     if value.lower() == 'exit':
         break
     elif float(value) < 0:
         continue
     else:
         root = float(value) ** 0.5
         print(f"The square root of {value} is {root}")


# Program calculates square roots of positive numbers until user types "exit"
question="A program that returns the square root of the entered number. \n"
question+="Enter a positive number"
question+="(to stop the program type 'exit'): "

while True:
     value=input(question)
     if value.lower() =='exit':
         break
     elif float(value)<0:
         continue
     else:
         root=float(value)**0.5
         print(f"The square root of {value} is {root}")

print("Program finished!")


# Program asks for age and prints museum ticket price until user types "exit" or "quit"
question="Enter your age: "

while True:
     value=input(question)
     if value=='exit' or value=='quit':
         break
     age=int(value)

     if age<7:
         price=5
     elif age<7<18:
         price=9
     elif age<18<65:
         price=12
     else: price=0

     if price==0:
         print("Free tickets!")
     else:
         print(f"Ticket {price} usd")



# WHILE, Lists and dictionary

# Filling a list using a while loop
names=[]
print("Let's create your best friends list!")
n=1
while True:
     question=f"{n} Enter your best friend names: "
     name=input(question)
     names.append(name)
     answer=input("Do you want  add more? (yes/no)\n")
     if answer=='yes':
         n+=1
         continue
     else:
         break
print("Your best friend list")
for name in names:
     print(name.title())


# Program collects friends' names and ages, then prints the list
# print("Enter your best friend name!")
friends={}
sign=True
while sign:
     name=input("Enter your friend name: ")
     age=input(f"{name.title()} age: ")
     friends[name]=int(age) #name is key, age is value

     answer=input("Do you want enter more? (yes/no)\n")
     if answer =='no':
         sign=False

for name, age in friends.items():
     print(f"{name.title()} {age} y/o")


# Program removes all 'bmw' entries from the cars list
cars=['bmw','honda','rols&royce','chevrolet','kia', 'bmw']
car='bmw'
while 'bmw' in cars:
     cars.remove('bmw')
print(cars)


students = ['joh', 'alice', 'mark', 'wilson']
graded_students = {}
while students:
     student = students.pop()
     grade = input(f"{student.title()} enter grade: ")
     print(f"{student.title()} graded")
     graded_students[student] = grade


# Write a program that creates a dictionary of products and their prices for an e-market.
# Ask the user to enter several elements (a product and its price) into the dictionary.
products={}
while True:
     product=input("Enter the product name: ")
     price=input(f"{product.title()} enter the price: ")
     products[product]=price
     answer=input("Do you want to add more? yes/no\n")
     if answer!= 'yes':
         break
orders=['apple','water','grape','bread']
products={
        'apple':8,
        'water':4,
        'grape':10,
        'bread':5
}


while orders:
     order=orders.pop()
     if order in products.keys():
         price=products[order]
         print(f"{order.title()}- {price} usd")
     else:
        print(f"We don' have {order}")


#This program builds an e-market dictionary of products with prices and
# then checks a customer’s order list, showing the price if available or saying “We don’t have it” if not.
products = {}

while True:
    product=input("Enter the product name: ").lower()
    price=float(input(f"{product.title()} enter the price: "))
    products[product]=price

    answer=input("Do you want add  more? yes/no\n")
    if answer !='yes':
        break

print("\nE market products and price: ")

for p,pr in products.items():
    print(f"{p.title()} {pr} usd")

orders=["apple","grapes","melon","cherry"]

print("\n Check out the products: ")
for item in orders:
    if item in products:
        print(f"{item.title()} price {products[item]}usd")
    else:
        print(f"Not in stock {item.title()}")
