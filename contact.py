contacts = []

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
        contacts.append((name, phone_number))
        print("Contact added!")

    elif choice == "2":
        print("All Contacts:")
        for index, (name, phone_number) in enumerate(contacts, start=1):
            print(f"{index}. Name: {name}, Phone: {phone_number}")

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts to delete.")
        else:
            print("Select a contact to delete:")
            for index, (name, _) in enumerate(contacts, start=1):
                print(f"{index}. {name}")
            delete_choice = int(input("Enter the number of the contact to delete: "))
            if 1 <= delete_choice <= len(contacts):
                deleted_contact = contacts.pop(delete_choice - 1)
                print(f"Contact '{deleted_contact[0]}' deleted.")
            else:
                print("Invalid choice.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
