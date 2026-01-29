#Salina Perez
#Final Q1

name = input("Enter your name:")

print("Menu")
print("----------------------")
print("option 1")
print ("option 2")
print("option 3")
print("---------------------")

option = int(input("Hello "+name+",enter a number to choose an option:"))

if option == 1:
    print(name+", what is Forest Gump's password?")
    print("1Forest1")
elif option ==2:
    food = input("Enter your favorite food:")
    for i in range(20):
        print(name+" loves "+food+"!")
elif option == 3:
    number = 1
    while number != 0:
        number = int(input("Enter a number:"))
        if number != 0:
            print ("I can confirm you're not a mind reader, try again")

    
