# Address Book Assistant Bot

This is a command-line assistant bot for managing contacts using object-oriented programming in Python.

## Project Structure

```
goit-pycore-hw-07/
├── main.py
├── models/
│   ├── __init__.py
│   ├── address_book.py
│   ├── fields.py
│   └── record.py
├── commands/
│   ├── __init__.py
│   ├── handlers.py
│   └── utils.py
```

## Features

- Add, change, remove, and find phone numbers
- Add multiple phone numbers at once
- Add and show birthdays
- Show upcoming birthdays within the next 7 days
- Delete entire contacts
- Display all saved contacts
- Built-in help command
- Handle invalid input with error messages

## Supported Commands

- `add [name] [phone1] [phone2] ...`
- `change [name] [old_phone] [new_phone]`
- `remove-phone [name] [phone]`
- `find-phone [name] [phone]`
- `delete-contact [name]`
- `phone [name]`
- `all`
- `add-birthday [name] [DD.MM.YYYY]`
- `show-birthday [name]`
- `birthdays`
- `help`
- `hello`
- `exit` or `close`

## Requirements

- Python 3.10 or higher

## How to Run

```bash
python main.py
```

