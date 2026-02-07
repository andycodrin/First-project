print("Primul meu proiect pe GitHub!")
print("Second version of the project")

num = input("Enter a number: ")
if num.isdigit():
    if (int(num) % 2 == 0):
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("Invalid input. Please enter a valid number.")    
