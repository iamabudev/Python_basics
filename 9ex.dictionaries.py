### introduction to python Dictionary
car_0 = {'model':'ferari','color':'red','year':'2023','price':'$23,000'}
print(car_0)

#create empty dictionary and put sevral items
student_1={}
student_1['name']= 'Alex'
student_1['surname']='Lincoln'
student_1['age']=24
print(f"{student_1['name']}  \n{student_1['age']}years old") #output name and age


#This code creates a `father` dictionary, extracts `name`, `b_year`, `city`, and prints them using `print()`
father={'name':'Fred', 'b_year':1982,'city':'Chicogo,US'}
father_name=father['name']
birth_year=father['b_year']
place_birth=father['city']
print(f"His name:{father_name}, Year birth: {birth_year}, City: {place_birth}")


#use get() returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
 }
model = car.get("model")
print(model)

#the code creates a family_foods dictionary that stores the favorite foods of four family members
family_foods={
    'John':'Sphagetti',
    'Rose':'Burger',
    'Alex':'Hot-Dog',
    'Rone':'Chicken'
}

print(f"John loves {family_foods['John']}")
print(f"Rose loves {family_foods['Rose']}")
print(f"Alex loves {family_foods['Alex']}")
print(f"Rone loves {family_foods['Rone']}")


# use python elements and translate the meaning to Uzbek
python_dict_keys={
    'integer':'butun son',
    'list':'royxat',
    'string':'matn',
    'for':'uchun',
    'if':'agar',
    'or':'yokida',
    'get':'olmoq'
}

key = input("Enter any keys: ").lower()
translate= python_dict_keys.get(key)
print(python_dict_keys.get(key))
if python_dict_keys==None:
    print('There is no words')
else:
    print(f"{key.title()} word translate to Uzbek-{translate}")

# this code involve items() methods
phones = {
     'John':'Iphone 7',
     'Rose':'Oppo 50',
     'Alex':'Samsung 10',
     'Rone':'Xiomi 10pro'
}

for key, value in phones.items():
    print(f"{key.title()} use {value.lower()} ")

#use values() method for output each values
print("Users phones model")
for tel in phones.values():
    print(tel)

#use keys() method for output each keys
print("Users name")
for name in phones.keys():
    print(name)


# set() method in Python is used to create a set, which is an unordered collection of unique elements. Sets are mutable, but their elements must be immutable
international_students={
    'Luka':'Brasil',
    'Andrea':'Vietnam',
    'Aziz':'Uzbekistan',
    'Losha':'Russia',
    'Bandar':'Indonesia',
    'Lucy':'England',
    'Sasha':'Russia',
    'Alisa':'Uzbekistan',
    'Lucy':'Algeria'
}

print('Welcome to International Student Club')
for arrange in set(international_students.keys()):
    print(arrange)


# Use a for loop to output each key and value in the dictionary, in alphabetical order, to the console.
python_methods = {
    'boolean':'boolean value',
    'float':'dozen',
    'for':'repeating an action',
    'close':'closes the file',
    'if':'condition check operator',
    'append':'adds an element at the end of the list'
}
print('Here is Python Methods')
for key, value in sorted(python_methods.items()):
    print(f"{key.title()}-{value}")




# the user can find out the capital of any country in the list
country_capital={
    'Usa':'Washington D.C',
    'Italy':'Rome',
    'Malaysia':'Kuala Lumpur',
    'Uzbekistan':'Tashkent',
    'Kazakhistan':'Nursultan',
    'Kyrgystan':'Bishkek',
    'Singapure':'Singapure',
    'Russia':'Moscow',
    'China':'SHanghai'
}
print('World country')
for country in sorted(country_capital):
    print(country.upper())

print('Country capital')
for city in sorted(country_capital.values()):
    print(city.title())

user=input("What country do you want to know the capital of: ").title()
capital = country_capital.get(user)
if capital == None:
    print("Sorry we don't have country on list")
else:
    print(f"{user.upper()} capital is {capital.title()}")


# Compare user-entered dishes with the menu, if the dish is on the menu,
# display the price, otherwise display the message "we don't have".
menu = {
    'plov':2500,
    'soup':2000,
    'rice':6000,
    'cake':5500,
    'salad':7000,
    'nan':3000,
    'tea':1500,
    'coffee':3500,
    'soda':1200
}

print('You can order 3 foods')
busket=[]
for n in range(3):
    busket.append(input(f"{n+1}-food: "))

for order in busket:
    if order in menu:
        print(f"{order.title()} {menu[order]} so'm")
    else:
        print(f"Sorry we don't have {order}")

