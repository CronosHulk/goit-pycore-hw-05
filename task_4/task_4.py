# Завдання 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

# Вимоги до завдання:

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


# Рекомендації для виконання:

# В якості прикладу додамо декоратор input_error для обробки помилки ValueError

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."

#     return inner



# Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

# @input_error
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."



# Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.



# Критерії оцінювання:

# Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
# Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
# Кожна функція для обробки команд має декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
# Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.


# Приклад використання:

# При запуску скрипту діалог з ботом повинен бути схожим на цей.

# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command:

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError) as e:
            return f"Invalid name: {e}."
        except (TypeError) as e:
            print(f"Invalid command: {e}.")
            print("\nGood bye!")

    return inner


def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    command = parts[0].strip().lower()
    args = parts[1:]
    
    return command, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Некоректна кількість аргументів. Використання: add [ім'я] [номер телефону]"
    
    name, phone = args
    contacts[name] = phone

    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Некоректна кількість аргументів. Використання: change [ім'я] [новий номер телефону]"

    name, phone = args
    
    if name not in contacts:
        return f"Помилка: Контакт з ім'ям '{name}' не знайдено."
        
    contacts[name] = phone

    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Некоректна кількість аргументів. Використання: phone [ім'я]"

    name = args[0]

    return contacts[name]

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

@input_error
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
        
        result = handler(args, contacts)
        print(result)


if __name__ == "__main__":
    main()
