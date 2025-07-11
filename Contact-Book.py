contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nAll Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name} - Phone No: {details['Phone']}")
    print()

def search_contact():
    key = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if key.lower() in name.lower() or key in details['Phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave a field empty to keep current value.")
        phone = input(f"New phone (current: {contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"New email (current: {contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"New address (current: {contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
