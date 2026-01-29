#Salina Perez
#GitHub test comment

def tempconversion(f):
    celsius = (f-32) * (5/9)
    return celsius
name = input("Enter your name:")

print("Menu")
print("______________________")
print("option 1")
print("option 2")
print("option 3")
print("option 4")
print("option 5")
print("______________________")

option = int(input("Hello "+name+",enter a number to choose an option:"))

if option == 1:
    print("Why was Cinderella so bad at soccer?")
    print("She kept running away from the ball!")
elif option == 2:
    for i in range(15):
        print(name)
elif option ==3:
    number = int(input("Enter a number:"))
    for i in range(number):
        print("Always remember that you are absolutely unique.Just like everyone else.")
elif option == 4:
    number = 0
    while (number != 21):
        number = int(input("Guess a number between 0 to 100:"))
        if (number > 100) or (number < 0):
             print("Please guess a number within the range of 0 to 100")
        elif (number > 21):
             print ("Your guess is too high")
        elif (number < 21):
            print ("You're guess is too low")
        elif (number == 21):
             print("Congratulations, you won! You are one smart cookie!")
elif option == 5:
    f = float(input("Enter the current temperature in farenheit:"))
    output = tempconversion (f)
    print("The temperature in celsius is", output)

