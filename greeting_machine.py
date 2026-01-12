def get_name():
    name = input("Enter your name: ")
    return name

def get_age():
    age = int(input("Enter your age: "))
    return age

def make_greeting(name, age):
    return "Hi " + name + "! You are " + str(age) + " years old."

user_name = get_name()
user_age = get_age()
final_message = make_greeting(user_name, user_age)

print(final_message)
