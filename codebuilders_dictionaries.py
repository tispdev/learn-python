#create and print a dictionary.

student = {
    "name": "Allen",
    "age": 16,
    "grade": "11"
}
print(student)


#Access by key

print(student["name"])
print(student["age"])


#modify a dictionary

student["age"] = 17
student["subject"] = "Computer Science"
print(student)


#loop through Keys and Values
    #first way
for key in student:
    print(key, "->", student[key])

   #second way
print("\nUsing .items():")
for k, v in student.items():
    print(f"{k}: {v}")
#first value is the key, the second is the value (key:value)
