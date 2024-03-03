
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        
class Phone(Field):
    def __init__(self, phone):
        
        if len (phone) == 10:
            super().__init__(phone)
        else: 
            print ("Enter 10 characters.") 
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone (self, phone):
        phone = Phone (phone)
        self.phones.append (phone)

    def remove_phone (self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove (p)
                return self.phones
        
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
        return self.phones

    def find_phone (self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return "The phone doesn't exist."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record (self, record):
        self.data.update ({record.name.value: record})

    def find (self, name):
        if name in self.data:
            return self.data [name]
        else: 
            return "Error"

    def delete (self, name):
        del self.data [name]
        print ("Done")
            

# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
john.remove_phone ("5555555555")

print(john)  # Виведення: Contact name: John, phones: 1112223333

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: The phone doesn't exist.
jane = book.find ("Jane")
found_phone = jane.find_phone ("9876543210")
print(f"{jane.name}: {found_phone}")
    # Видалення запису Jane
book.delete("Jane") # Виведення: Done
    # Виведення записів у книзі після видалення
for name, record in book.data.items():
    print(record)