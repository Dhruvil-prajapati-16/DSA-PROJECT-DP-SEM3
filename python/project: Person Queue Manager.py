import json
import os

FILENAME = os.path.abspath(os.path.join(os.path.dirname(__file__), "persons.json"))

Q = []

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def emptyq():
    return not bool(Q)

def insertQ(Que, item):
    Que.append(item)

def deleteQ(Que):
    if emptyq():
        return "underflow"
    else:
        return Que.pop(0)

def peek(Que):
    if emptyq():
        return "underflow"
    else:
        return Que[0].name

def search_person(Que, name):
    if emptyq():
        return "Queue is empty"
    else:
        for person in Que:
            if person.name.lower() == name.lower():
                return person
        return "Person not found"

def display(Que):
    if emptyq():
        print("Queue is empty!")
    else:
        print("Queue:")
        for person in Que:
            display_person(person)

def display_person(person):
    print(f"Name: {person.name}, Age: {person.age}, Gender: {person.gender}")

def list_persons(Que):
    if emptyq():
        print("Queue is empty!")
    else:
        print("List of Persons:")
        for person in Que:
            display_person(person)

def save_to_file(queue):
    with open(FILENAME, "w") as file:
        for person in queue:
            file.write(json.dumps(vars(person)) + '\n')

def load_from_file():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            if not lines:
                return []
            return [Person(**json.loads(line.strip())) for line in lines]
    except FileNotFoundError:
        return []

# Load existing data from file when the program starts
Q = load_from_file()
print("Previous data loaded.")

import atexit

# Register atexit function to save data on program exit
@atexit.register
def save_on_exit():
    save_to_file(Q)
    print("Data saved on program exit.")

while True:
    print("--this is implementation of queue--")
    print("Enter 1 for insert")
    print("Enter 2 for delete")
    print("Enter 3 for see queue (peek)")
    print("Enter 4 for list of person in queue")
    print("Enter 5 for search person")
    print("Enter 6 for display")
    print("Enter 7 for exit")

    ch = int(input("Enter a choice (1 to 7): "))

    if ch == 1:
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        gender = input("Enter the gender: ")
        new_person = Person(name, age, gender)
        insertQ(Q, new_person)
        input("Press any key to continue......")

    elif ch == 2:
        item = deleteQ(Q)
        if item == "underflow":
            print("Queue is empty")
        else:
            print("%s has been deleted!" % item.name)
            input("Press any key to continue......")

    elif ch == 3:
        item = peek(Q)
        if item == "underflow":
            print("Queue is empty")
        else:
            print("Front person is: %s" % item)
            input("Press any key to continue......")
        
    elif ch == 4:
        list_persons(Q)
        input("Press any key to continue......")

    elif ch == 5:
        search_name = input("Enter the name to search: ")
        found_person = search_person(Q, search_name)
        if isinstance(found_person, Person):
            print("Person found:")
            display_person(found_person)
        else:
            print(found_person)
        input("Press any key to continue......")

    elif ch == 6:
        display(Q)
        input("Press any key to continue......")

    elif ch == 7:
        break

    else:
        print("Please enter a valid choice.")
