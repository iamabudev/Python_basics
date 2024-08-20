
"""Sevral type of list; letter, numbers, number and alphabets"""
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # list of fruits (texts)
print(mevalar)
narhlar = [12000, 18000, 10900, 22000] # price list (numbers)
print(narhlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # mixed list of numbers and text
print(sonlar)
ismlar = [] # empty list
print(ismlar)



"""Change the element"""
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # We change the value 1 to 13000
narhlar[2] = 11000 #We change the 3rd value to 11000
narhlar[3] = narhlar[3]+2000 #We add 2000 to the 4th value
print(narhlar)



"""Add a new element by using append()"""
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # Add tarvuz to fruits
print(mevalar)




"""Make a empthy list and add details by using append() method """
cars = [] # make empthy code
cars.append('Lacetti') # to emphty add Lacceti
cars.append('Nexia 3') # to emthy list add Nexia 3
cars.append('Cobalt')  # to  emthy list add  Cobalt
print(cars)


""" To add a new item anywhere in the list .insert() we use the method """
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-place add a new detail
print(cars)
cars.insert(2, 'Damas') # 3-place add a new detail
print(cars)


"""To remove using inedks Del we use the operator:"""
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) will delate from list
print(mevalar)


"""And to delete by element value .remove(value) we use the method. To do this, we write the value to be deleted in parentheses"""
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # from list remove 'shaftoli'
print(mevalar)



"""Sometimes it may be necessary to pull an item from the list and use it instead of deleting it completely. For this in Python
.pop(index)
 we use the method.
"""
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # from list pull 'banana'
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)


