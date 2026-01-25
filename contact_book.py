contact = {
    "name": "Alex",
    "phone": "555-1234",
    "email": "alex@example.com"
}

print("Contact: " + str(contact))
print("Phone: " + contact["phone"])

contact["email"] = "alex.new@email.com"
print(contact)
