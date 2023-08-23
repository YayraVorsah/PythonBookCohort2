contacts = {}

while True:
    print("Contact Book")
    print("1. Add a new contact")
    print("2. Display all contacts")
    print("3. Delete a contact")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        contacts[name] = phone_number
        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts to display.")
        else:
            print("All Contacts:")
            for name, phone_number in contacts.items():
                print(f"Name: {name}, Phone: {phone_number}")

    elif choice == "3":
        if not contacts:
            print("No contacts to delete.")
        else:
            name_to_delete = input("Enter the name of the contact to delete: ")
            if name_to_delete in contacts:
                del contacts[name_to_delete]
                print(f"Contact '{name_to_delete}' deleted.")
            else:
                print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
