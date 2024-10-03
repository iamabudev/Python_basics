# #using in dictionrie connect list method (language)
programmers = {
    'ali':{ 'name':'Turdiyev',
            'year':1982,
            'language':['pyhton','c++'],
            'degree':'Bach'
         },

    'alex':{ 'name':'johnson',
            'year':1999,
            'language':['htmml, css, js'],
            'degree':'Bach'
        },

    'lucy': {'name':'jeffer',
            'year':1989,
            'language':['java','json','bootsrap'],
            'degree':'Master'
        }
}

for applicant, info in programmers.items():
    print(f"\nName:{applicant.title()} {info['name'].title()}\n"
          f"Year of birth: {info['year']} \n"
          f"Degree: {info['degree']} \n"
          "specialize on programming language:")
    for til in info['language']:
        print(til.upper())




literary_writers= {
    'Buxoriy':{'name':'Abu Abdulloh ibn Ismoil',
               'city':'Buxoro',
               'birth_year':810,
               'duration_year':60,
    },

    'Abdulloh':{'name':'Qodiriy',
                'city':'Tashkent',
                'birth_year':1894,
                'duration_year':44
    },

    'Erkin':{'name':'Vohidov',
             'city':'Fergana',
             'birth_year':1936,
             'duration_year':80
    },

    'Zahiriddin':{ 'name':'Bobur',
                   'city':'Andijan',
                   'birth_year':1483,
                   'duration_year':47


    }

}



for author, info in literary_writers.items():
    print(f"Name:{author.title()} {info['name'].title()}\n"
          f"City: {info['city']}\n"
          f"Born: {info['birth_year']}\n"
          f"Age lived: {info['duration_year']}years ")


 # persons<<<is list type and put all person in one, output with each dict details
persons= ['Buxoriy','Abdulloh','Erkin','Zahiriddin']
for shaxs in persons:
    name = literary_writers[shaxs]['name']
    shaxar = literary_writers[shaxs]['city']
    t_yil =literary_writers [shaxs]['birth_year']
    t_umur = literary_writers [shaxs]['duration_year']
    print(f"{name} {t_yil}-yilda {shaxar}da tavallud topgan. "
          f"{t_umur} yil umr ko'rgan.")



countrys = {
    'uzbekistan':{'capital':'Tashkent',
                'area':448978,
                'population':35_652_949,
                'currency':"so'm"

                },

    'russia': {'capital': 'Moscow',
                   'area': 170098246,
                   'population': 144_000_909,
                   'currency': "rubl"
                },
    'usa':{'capital': 'Washington',
            'area': 9631418,
            'population': 327_000_000,
            'currency': "dollar"
    },

    'malaysia': {'capital': 'Kuala Lumpur',
                'area': 329750,
                'population': 32_447_385,
                'currency': "rinngit"
            },
}

for country,info in countrys.items():
    print(f"Country: {country.title()} \n"
          f"Capital: {info['capital']}\n"
          f"Area: {info['area']} kv.kmm\n"
          f"Population: {info['population']} million\n"
          f"Currency: {info['currency']}")


#user can write country name and it will output country details to the user.
user = input('Enter country: ').lower()
if user in countrys:
    info = countrys[user]
    print(f"{user.capitalize()}\n"
          f"Capital: {info['capital']}\n"
          f"Area: {info['area']}\n"
          f"Population: {info['population']}\n"
          f"Currency: {info['currency']}")
else:
    print("We don't have any information about it.")
