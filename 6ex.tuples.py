"""use sort() for make it step-by-step  with alphabet(a-z)"""
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)



"""it may be necessary to sort the list without disturbing the order of the elements within the original list. For this
sorted()
we use the function:"""
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)



"""this program used  two kind of list form 1-orginal list and arranged, 2-the same list but max numbers come first"""
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))


"""Use len()method for count the amount"""
fruits = ['pear','banana','apple','watermelon','lemon']
print("Elements quantity:",len(fruits)) # len(fruits) shows lenth



"""range()
 we can also give the step using:"""
even_numbers = list(range(0,20,2)) # 0 to 20 between with 2  step
odd_numbers = list(range(1,20,2))  # 1 to 20 between with 2 step
print("Even numbers: ", even_numbers )
print("Odd numbers: ", odd_numbers)



"""Use min(), max(), sum() methods"""
prices = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
cheap = min(prices)
expensive = max(prices)
total = sum(prices)
print("Cheap price ", cheap, ". Most expensive ", expensive, ". Total: ", total)


"""GET A COPY OF THE list"""
numbers = [1, 2, 3, 4, 5] # create numbers list
numbers2 = numbers # We set the list numbers2 to numbers
numbers2.append(6) # We add 6 to numbers2
numbers2.append(7) # add 7 to numbers2
print("This is list:", numbers)
print("This is 2nd list:", numbers2)



"""how can we copy the list? We just leave both indices in square brackets blank:"""
numbers = [1, 2, 3, 4, 5] # create list
numbers2 = numbers[:] # [:] copies the entire list
numbers2.append(6) # We add 6 to numbers2
numbers2.append(7) # add 7 to numbers2
print("This is numbers list:", numbers)
print("This is numbers2 list:", numbers2)



"""Tuples-The values in the tuple are assigned once,
 at the beginning of the program, and cannot be changed afterwards"""
tomonlar = (20, 30, 55.2)
print(tomonlar)



"""Additonal  exercises"""

"""List the states you know and output the list to the console"""
country= ['Singapore', 'Malaysia', 'UAE', 'China', 'Saudia Arabia', 'Algeria']
quantity=len(country)
arrange= sorted(country)
non_arrange=sorted(country)
print(country)
print(quantity)
print(arrange)
print(sorted(non_arrange, reverse=True))



"""Make a list of even numbers from 120 to 1200"""
even_numbers=list(range(120,1200,2))
print(even_numbers)
total_numbers=sum(even_numbers) #use sum()that calculate all index
print(total_numbers)
big_number=max(even_numbers)#use max()that shows highest number
small_numbers=min(even_numbers)#use min() that shows lowest number
print(f"Max number: {big_number}\nMin number: {small_numbers}", )
count_numbers= len(even_numbers)# use len() that is height
print(f"Counted: {count_numbers}")
pop_element=even_numbers[0:20]# that code show 0 to 20 only
pop_element2=even_numbers[20:]
pop_element3=even_numbers[:20]# last 20 index
print(pop_element)
print(pop_element2)
print(pop_element3)



taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
#Copy the foods to a new list called #breakfast
nonushta = taomlar[:]

#In the new list, leave only breakfast foods, and add 2 additional foods
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

# Output both lists (meals and breakfast) to the console
print(taomlar)
print(nonushta)

#Convert the breakfast list above to an immutable list and set the value breakfast[0] = "cream and bread".
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
