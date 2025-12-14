favorites = ["pizza", "soccer", "minecraft","music", "dogs"]

print("My 5 favorite things: ")
for item in favorites:
    print("I love %s" %item)

useri= input("What is YOUR favorite item? ")
             
favorites.append(useri)

print(favorites)
