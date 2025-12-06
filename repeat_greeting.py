name = input("Enter your name: ")

while True:
    answer = input("Say hi to " + name + "? (yes/no): ")

    if answer == "yes":
        print("Hi, " + name + "!")
    elif answer == "no":
        print("Goodbye!")
        break
    else:
        print("Please say yes or no.")
    
    
