def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    command = parts[0].strip().lower()
    args = parts[1:]

    return command, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(args, contacts):
    if contacts:
        output = "All contacts:\n"
        sorted_contacts = sorted(contacts.items())
        for name, phone in sorted_contacts:
            output += f"{name}: {phone}\n"
        return output.strip()
    else:
        return "Жодних контактів не збережено."


def handle_hello(args, contacts):
    return "How can I help you?"


def main():
    contacts = {}

    handlers = {
        "hello": handle_hello,
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
    }

    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
        except EOFError:
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        handler = handlers.get(command)

        if handler:
            result = handler(args, contacts)
            print(result)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
