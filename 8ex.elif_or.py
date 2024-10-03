
"""Code about price for depends on age"""
yosh = int(input('Enter your age?  '))
if yosh<=4:
     print('Entrance free.')
elif yosh<=12:
     print('For you entrance fee 5000 so\'m')
else:
     print('For you entrance fee 10000 so\'m')



"""SEQUENTIAL CHECK OF TERMS, write code with arrange boolen operotor and if method"""

price = 5
tea= True
bread = False
rice= True
salad=True
desert = False
if tea:
    print("Costumer order tea")
    price = price + 1
if bread:
     print("Costumer order bread")
     price = price + 2.5
if rice:
     print("Costumer order rice")
     price = price + 1.5
if salad:
     print("Costumer order salad")
     price = price + 3
if desert:
     print("Costumer order desert")
     price = price + 5

print(f"Total: {price}$")

# """Ask the user to enter an even number. Print "Thank you!" if the user enters an even number,
#  "This number is not even" if the user enters an odd number."""
son = float(input("Enter even numbers: "))
if son%2:# % this operation can divide numbers
     print('This number is not even.')
else:
     print("Thank you!")

# """Ask the user's age, and calculate the price of the museum admission ticket as follows"""
print("Online ticket")
age= int(input("Enter your age>>>"))
if age >=60:
   print("Free entrance.")
elif age >=18:
     print("For you 20RM")
else:
     print("For you 10RM")


# """Ask the user to enter two numbers, compare the numbers and report whether
# they are equal or greater/less than"""

number1=float(input("Enter 1st number>>>"))
number2=float(input("Enter 2nd number>>>"))


if number1 == number2 :
    print(f"{number2}={number2}")
elif number1<number2:
     print(f"{number1}<{number2}")
elif number1>number2:
    print(f"{number1}>{number2}")



# """First take all products from costumer and collect to bucket and show him at the end.
#  What we have what we don't"""
products= ['rice', 'apple', 'peach','bread','milk']
bucket = []
for n in range(5):
     bucket.append(input(f" Add to cart {n+1} : "))

for product in bucket:
    if product in products:
         print(f"In our shop {product}")
    else:
      print(f"In our shop don't have {product}")

