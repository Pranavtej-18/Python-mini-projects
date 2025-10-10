class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name.title()} : {self.phone}"
    
class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        name_key = name.lower()
        if name_key in self.contacts:
            print(f"⚠️ Contact '{name}' already exists.")
        else:
            self.contacts[name_key] = Contact(name, phone)
            print(f"✅ contact '{name}' added successfully")

    def display_contacts(self):
        if not self.contacts:
            print('No contact found')
            return
        else:
            print('\n📖 Contact List:')
            for contact in self.contacts.values():
                print("-", contact)

    def search_contact(self, name):
        name_key = name.lower()
        if name_key in self.contacts:
            print("🔍 Found:",self.contacts[name_key])
        else:
            print(f"❌ No contact found with name '{name}'.")
    
    def update_contact(self, name,new_phone):
        name_key = name.lower()
        if name_key in self.contacts:
            self.contacts[name_key].phone = new_phone
            print(f"🔁 contact '{name}' updated successfully.")
        else:
            print(f"❌ No contact found with name '{name}'.")

    def delete_contact(self, name):
        name_key = name.lower()
        if name_key in self.contacts:
            del self.contacts[name_key]
            print(f"🗑️ Contact '{name}' deleted.")
        else:
            print(f"❌ No contact found with name '{name}'.")
    

book = ContactBook()

while True:
    print('\n📒 Contact Book Menu')
    print('1. Add Contact')
    print('2. View Contacts')
    print('3. Search Contact')
    print('4. Update Contact')
    print('5. Delete Contact')
    print('6. Exit')

    choice = int(input('Enter choice: '))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Phone: ")
        book.add_contact(name, phone)
    elif choice == 2:
        book.display_contacts()
    elif choice == 3:
        name = input('Enter contact name: ')
        book.search_contact(name)
    elif choice == 4:
        name = input('Enter contact name: ')
        phone = input('Enter phone no: ')
        book.update_contact(name,phone)
    elif choice == 5:
        name = input('Enter contact name: ')
        book.delete_contact(name)
    elif choice == 6:
        print('Exiting..') 
        break
    else:
        print('Invalid choice, enter again!!')