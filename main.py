"""
Entry point for the assistant bot.
Handles command parsing and control loop.
"""

from models.address_book import AddressBook
from commands.utils import parse_input
from commands.handlers import (
    add_contact, change_contact, show_phone,
    show_all, add_birthday, show_birthday, birthdays,
    remove_phone, find_phone, delete_contact
)

def main():
    """Run the command-line assistant bot."""
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case "remove-phone":
                print(remove_phone(args, book))
            case "find-phone":
                print(find_phone(args, book))
            case "delete-contact":
                print(delete_contact(args, book))

            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
