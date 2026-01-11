import json
import os

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def to_dict(self):
        return {
            "name"  : self.name,
            "phone" : self.phone
        }
    
    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'])
    
    def __str__(self):
        return f"{self.name.title()} : {self.phone}"
    

class ContactBook:
    
    def __init__(self, filename = "contacts.json"):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for name_key, contact_data in data.items():
                    self.contacts[name_key] = Contact.from_dict(contact_data)

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(
                {k: v.to_dict() for k, v in self.contacts.items()},
                file,
                indent=4
            )       
            

    def add_contact(self, name, phone):
        name_key = name.lower()
        if name_key in self.contacts:
            print("⚠️ Contact already exists.")
            return 
        self.contacts[name_key] = Contact(name, phone)
        self.save_contacts()
        print("✅ Contact saved successfully.")


    def display_contacts(self):
        if not self.contacts:
            print("No contacts available")
            return 
        print("\n📖Contact List: ")
        for contact in self.contacts.values():
            print("-", contact)
    

    def search_contact(self, name):
        name_key = name.lower()
        if name_key not in self.contacts:
            print("❌ contact not found.")
        print("🔍Found: ", self.contacts[name_key])

        
    def update_contact(self, name, new_phone):
        name_key = name.lower()
        if name_key not in self.contacts:
            print("❌ contact not found.")
            return 
        self.contacts[name_key].phone = new_phone
        self.save_contacts()
        print("🔁 updated contact.")
    
    def delete_contact(self, name):
        name_key = name.lower()
        if name_key not in self.contacts:
            print("❌ contact not found.")
            return
        del self.contacts[name_key]
        self.save_contacts()
        print("🗑️ Contact deleted.")
    
    

book = ContactBook()

while True:
    print("\n*** Contact Book ***")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Terminate/Exit")

    choice = int(input("Enter operation number you want to perform: "))

    if choice == 1:
        book.add_contact(
            input("name: "),
            input("phone: ")
        )
    elif choice == 2:
        book.display_contacts()
    elif choice == 3:
        book.search_contact(input("Enter contact name: "))
    elif choice == 4:
        book.update_contact(
            input("Name to update: "),
            input("New phone: ")
        )
    elif choice == 5:
        book.delete_contact(input("Enter contact name: "))
    elif choice == 6:
        print("GoodBye 👋")
        break
    else:
        print("Invalid Choice!!!")