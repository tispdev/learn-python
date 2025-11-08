#first 'for' loop (Print 5 times)

for i in range(5):
    print("I love coding!")



#second 'for' loop (Count from 1 to 10)

for i in range(1, 11):
    print(i)

    

#third 'for' loop (Countdown with Step = -1)

for i in range(5, 0, -1):
    print(i)
print("Go!")



#fourth 'while' loop (Repeat until "no")

answer = ""
while answer !="no": # "yes" is not equal to "no" -> true
    answer = input("Again? (yes/no): ").lower()
    if answer == "yes":
        print("Keep going!")
print("Done!")
