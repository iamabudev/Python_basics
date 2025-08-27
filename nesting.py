# Dictionary car0 stores information about a  car:
# model, color, year, price, mileage (km), and transmission type.
car0 = {
        'model':'lacetti',
        'color':'white',
        'year':2018,
        'price':13000,
        'km':50000,
        'transmission':'manual'
        }

car1 = {
        'model':'nexia 3',
        'color':'black',
        'year':2015,
        'price':9000,
        'km':89000,
        'transmission':'auto'
        }

car2 = {
        'model':'gentra',
        'color':'red',
        'year':2019,
        'price':15000,
        'km':20000,
        'transmission':'manual'
        }


# Let's put all the cars into a single list and display them one by one on the console
car = car1
print(f"{car['model'].title()},\
  {car['color']} color,\
  {car['year']}-year, {car['price']}$")

car = car1
print(f"{car['model'].title()},\
  {car['color']} color,\
  {car['year']}-year, {car['price']}$")

car = car2
print(f"{car['model'].title()},\
  {car['color']} color,\
  {car['year']}-year, {car['price']}$")


# Let's put all the cars into a single list and display
# them one by one on the console using a for loop
cars=[car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['color']} color,"
          f"{car['year']}-year, {car['price']}$")



# Using a for loop, we can also create a list of empty dictionaries.
malibus=[]

for n in range(10):
    new_car={
        'model':'malibu',
        'color':'None',
        'year':2020,
        'km':0,
        'transmission':'auto'
    }

    malibus.append(new_car)

    for malibu in malibus[:3]:
        malibu['color']='red'



    # for malibu in malibus:
    #     print(malibu)

    for malibu in malibus[3:6]:
        malibu["color"] = "black"

    # for malibu in malibus:
    #     print(malibu)

    for malibu in malibus[6:]:
        malibu["color"] = "black"
        malibu["transmission"] = "manual"

    # for malibu in malibus:
    #     print(malibu)

    for malibu in malibus:
        if malibu["transmission"] == "auto":
            malibu["price"] = 40000
        else:
            malibu["price"] = 35000

    for malibu in malibus:
        print(malibu.values())


developers={
    'ali':['python','c++'],
    'john':['css','html'],
    'alice':['c#','c'],
    'fred':['php','sql']
}

for name, info in developers.items():
    print(f"\n{name.title()} knows these kind of programming language: ")
    for lang  in info:
        print(lang.upper())


for name, info in developers.items():
    print(f"\n{name.title()} knows these kind of programming languages")
    for lang in info:
        print(f'{ lang.upper()  }', end='')


# Dictionary inside a dictionary

workers={
    'ali':{
        'surname':'john',
        'age':21,
        'information':'study',
        'language':['java', 'c']
    },

    'bob':{
        'surname':'gate',
        'age':32,
        'information':'graduated',
        'language':['c++','pyhton','html']
    },

    'alisa':{
        'surname':'wilson',
        'age':25,
        'information':'study',
        'language':['php','css']
    }
}

for name, info in workers.items():
    print(f"{name.title()} {info['surname'].title()}\n"
          f"{info['age']}-years old\n"
          f"Study background: {info['information']}")

    for lang in info['language']:
        print(lang.upper())


# Dictionary 'movies' stores people's favorite movies.
# Each key is a person's name, and each value is a list of movies they like.
movies={
     'lucy':['terminator', 'rambo', 'titanic'],
    'will':['tenat','inception', 'intersteller'],
    'emma':['bomb', 'john wick','joy']
    }

for name, movies in movies.items():
    print(f"\nName:{name.title()}",)

    for film in movies:
        print(film)


# A dictionary called 'countrys' stores information about several countries.
# Each country is a key, and its value is another dictionary containing details
# like capital, land size, population, and currency.
countrys={
    "usa":{
        "capital":"washington",
        "landsize":9_631_418,
        "population":327_000_000,
        "currency":"usd"
    },
    "malaysia":{
        "capital":"kuala lumpur",
        "landsize":329750,
        "population":30_000_000,
        "currency":"ringgit"
    },

    "uzbekistan":{
        "capital":"tashkent",
        "landsize":448978,
        "population":38_000_000,
        "currency":"usz"
    },

    "russia":{
        "capital":"moscow",
        "landsize":17_098_246,
        "population":144_000_000,
        "currency":"rubl"
    }
}
country=input("Enter the country name: ".lower())

if country in countrys:
    info=countrys[country]
    print(f"\n{country.capitalize()} capital is {info['capital'].title()}"
              f"\nTerritory: {info['landsize']} kv.km"
              f"\nPopulation: {info['population']}"
              f"\nCurrency: {info['currency']}")
else:
        print("Don't have any information about the country")

