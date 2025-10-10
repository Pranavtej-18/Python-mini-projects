import json
import os

class Contact:
    
    # when we create a obj of a Contact self variable takes the current details and stores!
    
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    # we use this func to_dict() to make the data to convert into dictionary so that it stores that data in json format 
    # return a dictionary
    
    def to_dict(self):
        return {
            'name':self.name,
            'phone':self.phone,
            'email':self.email,
            'address':self.address
        }


# This class manages multiple contacts and handles loading saving

class ContactBook:

    # filename = contact.json - place where contacts are saved

    def __init__(self,filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts() # list(contacts) that stores all contacts in memory and in dictionary format

    def load_contacts(self):
        # checks whether the file exists or not
        if os.path.exists(self.filename):
            # try & catch - used because to avoid JSONDecode error at beginning
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, ValueError):
                return []
        # if there is no data it returns an empty list to contacts
        return []
    
    # saves the current in-memory list of contacts

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            # json.dump() writes python data -> json format
            json.dump(self.contacts,file,indent=4) # indent makes information to store in clean and readable format

    # contact is added to contacts dict at last and saves to contacts.json file permanently 

    def add_contact(self,contact):
        self.contacts.append(contact.to_dict())
        self.save_contacts()
        print(f'✅ contact \'{contact.name}\' added successfully')

    # prints contact details

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return 
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}.{contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")


if __name__=="__main__":
    book = ContactBook()

    while True:
        print("\n📒 Contact Book Menu")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Exit")

        choice = int(input('Enter Choice: '))

        if choice == 1:
            name = input('Name: ')
            phone = input('phone: ')
            email = input('Email: ')
            address = input('Address: ')
            contact = Contact(name,phone,email,address)
            book.add_contact(contact)
        elif choice == 2:
            book.view_contacts()
        elif choice == 3:
            print('Exiting...')
            break
        else:
            print('Invalid choice. Try again')
