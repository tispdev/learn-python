from datetime import datetime

# extract the current date
current_date = datetime.now()

# extract current year from the current date
currentyear = current_date.year

name = input("Enter your name: ")
birthyear = int(input("Enter your birth year: "))
hometown = input("Enter your hometown: ")
age = currentyear - birthyear

print("%s from %s is approximately %d years old."%(name,hometown,age))
