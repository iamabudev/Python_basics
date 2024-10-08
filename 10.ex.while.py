#using while is also a repetition operator, unlike for, which repeats the code until a certain condition is true.
numb = 1 # we assign the value 1 to the number
while numb<=5: # as long as the number is less than or equal to 5...
    print(numb, end=' ') # output the number to the console,
    numb = numb+1 #  add 1 to the number.





#user enter any number and output to console square of a number
#break statement we can stop the loop even if the while condition is true
print("Enter any numbers,program that returns the square of a number")
savol = "Enter the number"
savol+="(If you need stop write 'exit'): "
symbol = True
while symbol:
  qiymat = input(savol)
  if qiymat == 'exit':
    break
  else:
    print(float(qiymat)**2)

print('Program done!')


#use continue and we can stop the current iteration, and continue with the next:
numbers = list(range(1,11))
for numb1 in numbers:
  if numb1 == 5: #Note that number 5 is missing in the result
    continue
  print(f"{numb1} square of is equal to {numb1**2}")

son = 0
while son<11:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)

#ask the user to enter their favorite books. Stop the program as soon as the user types 'stop'
print("Favourite books list")
savol = "Write your favourite book"
savol+="(if you want to stop code type 'stop'): "
while True:
    qiymat = input(savol)
    if qiymat == 'stop':
        break
    else:
        print(f"{qiymat}")


#this code based on user input age it will output price follow by age
while True:
    age = input("Enter your age (or 'exit'/'quit' type for stop): ")

    if age.lower() in ['exit', 'quit']:
        print("Programme done!")
        break

    yosh = int(age)

    if yosh < 7:
        print("Ticket price: 2000 so'm")#for youger than 7 years
    elif 7 <= yosh < 18:
        print("Ticket price: 3000 so'm")# for  younger than 18 years
    elif 18 <= yosh < 65:
        print("Ticket price: 10000 so'm") # below than 65 years
    else:
        print("Ticket is free.")# older than 65 years


#in this code recieve number from user and calculate square root
savol ="A program that returns the square root of an input number\n"
savol += "Enter positive number"
savol += "(enter 'exit' for stop code): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break # use break once type 'exit' it will stop
    elif float(qiymat)<0:
        continue # if user enter negative number loop still work
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} root of {ildiz} equal ")




#use remove()method delete all given  items in list
cars =  ['bmw','volvo','bmw','mazda','mitsubishi','volvo','bmw']
while 'volvo' in cars:
    cars.remove('volvo')
print(cars)




#empthy list products() input several types of items and output all product list
products= []
print("Welcome to Grocery storey")
print("Pick your products name: ")
n=1
while True:
    question = f"{n}-enter the product:  "
    products_cart = input(question)
    products.append(products_cart)
    answer = input("Add extra? (yes/no): ")
    if answer == 'yes':
        n += 1
        continue
    else:
        break

print("Products list")
for favourite_list in products:
    print(favourite_list)

orders = ["apple", "banana", "grapes", "melon"]
products = {"apple": 200, "peach": 250, "melon": 180, "grapes": 220}

while orders:
    buyurtma = orders.pop()
    if buyurtma in products.keys():
        narh = products[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Don't have {buyurtma} ")