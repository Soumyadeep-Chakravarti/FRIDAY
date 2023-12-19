import important_items
import TTS
import pickle

class PhoneBook:
    def __init__(self):
        phonebook_address = important_items.phonebook_address
        self.load_phone_book()
        

    def load_phone_book(self):
        try:
            with open(self.phonebook_address, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_phone_book(self):
        with open(self.phonebook_address, 'wb') as file:
            pickle.dump(self.contacts, file)

    def add_contact(self, name, number):
        if name in self.contacts:
            self.contacts[name].append((name, number))
        else:
            self.contacts[name] = [(name, number)]
        print(f"Contact {name} added successfully.")
        self.save_phone_book()

    def view_contacts(self):
        if not self.contacts:
            print("Phone book is empty.")
        else:
            print("Contacts:")
            for name, entries in self.contacts.items():
                for entry in entries:
                    print(f"{entry[0]}: {entry[1]}")

    def search_contact(self, name):
        if name in self.contacts:
            entries = self.contacts[name]
            for entry in entries:
                print(f"Contact: {entry[0]}, Number: {entry[1]}")
        else:
            print(f"Contact {name} not found.")

    def edit_contact(self, name):
        if name in self.contacts:
            entries = self.contacts[name]
            print(f"Current contact information for {name}:")
            for i, entry in enumerate(entries, start=1):
                print(f"{i}. Contact: {entry[0]}, Number: {entry[1]}")

            index = int(input("Enter the index of the contact you want to edit: ")) - 1

            if 0 <= index < len(entries):
                new_number = input("Enter the new contact number: ")
                self.contacts[name][index] = (name, new_number)
                print(f"Contact {name} edited successfully.")
                self.save_phone_book()
            else:
                print("Invalid index. No contact edited.")
        else:
            print(f"Contact {name} not found.")

def main_phonebook(choice:int):
    phone_book = PhoneBook()
    speech_processor = TTS.SpeechProcessor()

    while True:
        '''print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
'''
        speech_processor.text_to_speech('Opened phonebook')
        
        if choice == "1":
            speech_processor.text_to_speech("Adding new contact entry!")
            name = speech_processor.listen_to_microphone("contact name: ")
            number = speech_processor.listen_to_microphone("contact number: ")
            phone_book.add_contact(name, number)
        elif choice == "2":
            speech_processor.text_to_speech("Viewing contacts")
            phone_book.view_contacts()
        elif choice == "3":
            name = speech_processor.listen_to_microphone("contact name to search: ")
            phone_book.search_contact(name)
        elif choice == "4":
            name = speech_processor.listen_to_microphone("contact name to edit: ")
            phone_book.edit_contact(name)
        elif choice == "5":
            speech_processor.text_to_speech("Exiting phone book. Goodbye!")
            break
        