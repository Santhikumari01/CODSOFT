def display_menu():
    print("\n=== Contact Book Menu ===")
    print("1. Add a New Contact")
    print("2. View All Contacts")
    print("3. Search for a Contact")
    print("4. Update an Existing Contact")
    print("5. Delete a Contact")
    print("6. Exit the Contact Book")

contacts = {}  # Dictionary to store contacts

def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
    print(f"Contact '{name}' added successfully!")

def view_contact_list():
    if not contacts:
        print("Your contact list is currently empty.")
    else:
        print("\n=== Contact List ===")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["phone_number"]:
            print("\n=== Contact Found ===")
            print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print(f"No contact found with the term '{search_term}'.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact '{name}'. Leave a field blank to keep the current value.")
        phone_number = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        contacts[name]["phone_number"] = phone_number if phone_number else contacts[name]["phone_number"]
        contacts[name]["email"] = email if email else contacts[name]["email"]
        contacts[name]["address"] = address if address else contacts[name]["address"]
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")