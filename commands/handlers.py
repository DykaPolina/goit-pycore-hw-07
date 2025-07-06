"""
Handlers for each bot command.
"""

from .utils import input_error


@input_error
def add_contact(args, book):
    """
    Add a new contact or phone to an existing one.
    """
    from models.record import Record
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    """
    Change a phone number for an existing contact.
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    success = record.edit_phone(old_phone, new_phone)
    return "Phone updated." if success else "Old phone number not found."



@input_error
def show_phone(args, book):
    """
    Show all phone numbers of a contact.
    """
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_phones()


def show_all(book):
    """
    Show all records in the address book.
    """
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.values())


@input_error
def add_birthday(args, book):
    """
    Add a birthday to an existing contact.
    """
    name, bday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(bday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    """
    Show the birthday of a contact.
    """
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_birthday() or "No birthday set."


@input_error
def birthdays(args, book):
    """
    Call the address book method to get upcoming birthdays.
    """
    return book.get_upcoming_birthdays()

@input_error
def remove_phone(args, book):
    """
    Remove a phone number from a contact.
    Usage: remove-phone [name] [phone]
    """
    name, phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.find_phone(phone):
        return "Phone number not found."
    record.remove_phone(phone)
    return "Phone removed."


@input_error
def find_phone(args, book):
    """
    Find a phone number in a contact.
    Usage: find-phone [name] [phone]
    """
    name, phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    found = record.find_phone(phone)
    return f"Phone found: {found.value}" if found else "Phone not found."


@input_error
def delete_contact(args, book):
    """
    Delete a contact completely.
    Usage: delete-contact [name]
    """
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    book.delete(name)
    return "Contact deleted."
