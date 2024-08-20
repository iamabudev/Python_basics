

"""Using f-string and sorted codes"""
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} street, {mahalla} district, {tuman} village,  {viloyat} region")



"""Use input method and ask user to enter information"""
information = input("Please provide your home adress! (street,district,village,region): ")
print("Your home adress:" + information)



"""(\n)use this method can settle each data to row"""
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"\n{kocha} street \n{mahalla} district \n{tuman} village  \n{viloyat} region")



"""Use 3 method upper(), lower(), caoitalize()"""
kocha="bog'bon"
mahalla="sog'bon"
tuman="bodomzor"
viloyat="Samarqand"
manzil="uzbekistan"
print(f"{kocha} street, {mahalla} district, {tuman.upper()} village,  {viloyat.lower()} region, {manzil.capitalize()} country")


