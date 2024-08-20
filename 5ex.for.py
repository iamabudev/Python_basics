
"""Let's see the following example. We have a list of guests, we want to extract each guest's name from a new row."""
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)



"""For method is help to us write code more easier and fast """
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")



"""WORKING WITH NUMBERED LISTS WITH for """
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")



"""A new list can also be created using for:"""
sonlar = list(range(11)) # to  1 until 10 numbers
sonlar_kvadrati =[] # emphty list
for son in sonlar:  # for each number in numbers
    sonlar_kvadrati.append(son**2) #calculate its square and upload it to numbers_squared


print(sonlar)
print(sonlar_kvadrati)



"""input() and for, this code automacilly ask 5times your friend name and output with list"""
dostlar = [] # emthy list
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n from this 0 to Takes up to 4 values
    dostlar.append(input(f"{n+1}-enter your friend's name: "))
print(dostlar)