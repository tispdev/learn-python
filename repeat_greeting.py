name = input("Enter your name: ")

while True:
    answer = input("Say hi to " + name + "? (yes/no): ").strip().lower()

    if answer == "yes":
        print("Hi, " + name + "!")
    elif answer == "no":
        print("Goodbye!")
        break
    else:
        print("Please say yes or no.")
    
    
