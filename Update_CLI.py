
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact doesn`t exist."
        except IndexError:
            return "No contacts found."


    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def username_phone (args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError
        #return "Contact doesn't exist"
@input_error   
def show_all_contacts (contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name} - {phone}")
    else:
        raise IndexError
        #print("No contacts found.")
    
    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input.lower ())

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "username":
            print (username_phone (args, contacts))
        elif command == "all":
            print (show_all_contacts (contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()