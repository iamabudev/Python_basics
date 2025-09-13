# This program simulates a simple car shop inventory system.
# The auto_info() function creates a dictionary to store car details like company, model, color, gear, year, and price.
# The enter_auto() function first displays two pre-defined cars, then allows the user to input new car details interactively
# and stores them in a list until the user decides to stop.
# The info_print() function displays a car's information in a formatted way with proper capitalization.
# Together, these functions demonstrate how to collect, store, and display information for multiple cars dynamically.

def auto_info(company, model, color, gear, year, price=None):
    auto = {
        'company': company,
        'model': model,
        'color': color,
        'gear': gear,
        'year': year,
        'price': price
    }
    return auto


def enter_auto():
    auto1 = auto_info('honda', 'city', 'black', 'auto', 2022, 1300)
    auto2 = auto_info('volvo', 'x30', 'silver', 'manual', 2020)
    available_auto = [auto1, auto2]

    print('Welcome to E-auto shop!')
    for auto in available_auto:
        price = auto['price'] if auto['price'] else 'None'
        print(f"{auto['color']} {auto['company']} {auto['model']} {price}")

    print("Let's create autos list for sale!")
    autos = []
    while True:
        print("Enter the details below:")
        company = input("Manufacturer name: ")
        model = input("Model name: ")
        color = input("Color: ")
        gear = input("Manual/Auto: ")
        year = input("Year: ")
        price = input("Price (press Enter if unknown): ")

        price = price if price else None
        autos.append(auto_info(company, model, color, gear, year, price))

        answer = input("Do you want to add more? yes/no: ")
        if answer.lower() != 'yes':
            break

    return autos


def info_print(auto):
    print(f"{auto['color'].title()} {auto['company'].upper()} "
          f"{auto['model'].upper()}, {auto['gear']} gearbox, "
          f"{auto['year']}-year, {auto['price']}$")
