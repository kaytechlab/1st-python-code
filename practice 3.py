def create_contact(name, phone):
    contact = {
        "name": name,
        "phone": phone
    }
    return contact
contact_info = create_contact("Kay", "08101806793")
print(contact_info)
