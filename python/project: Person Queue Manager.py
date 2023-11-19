import json
import os

FILENAME = os.path.abspath(os.path.join(os.path.dirname(__file__), "persons.json"))

Q = []
f = None
r = None

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def emptyq():
    return not bool(Q)

def insertQ(Que, item):
    global f, r
    Que.append(item)
    if len(Que) == 1:
        f = r = 0
    else:
        r = len(Que) - 1

def deleteQ(Que):
    global f, r
    if emptyq():
        return "underflow"
    else:
        i = Que.pop(0)
        if len(Que) == 0:
            f = r = None
        return i

def peek(Que):
    if emptyq():
        return "underflow"
    else:
        return Que[f]

def search_person(Que, name):
    if emptyq():
        return "Queue is empty"
    else:
        for person in Que:
            if person.name.lower() == name.lower():
                return person
        return "Person not found"

def display(Que):
    if len(Que) == 0:
        print("Queue is empty!")
    elif len(Que) == 1:
        print(Que[0], "<-- this is front and rear ")
    else:
        print(Que[f], "<-- now this is front")
        for x in range(1, r):
            print(Que[x])
        print(Que[r], "this is rear")

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

    ch = int(input("enter a choice 1 to 7: "))

    if ch == 1:
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        gender = input("Enter the gender: ")
        new_person = Person(name, age, gender)
        insertQ(Q, new_person)
        input("press any key to continue......")

    elif ch == 2:
        item = deleteQ(Q)
        if item == "underflow":
            print("Queue is empty")
        else:
            print("%s has been deleted!" % item.name)
            input("press any key to continue......")

    elif ch == 3:
        item = peek(Q)
        if item == "underflow":
            print("Queue is empty")
        else:
            print("Front person is: %s" % item.name)
            input("press any key to continue......")
        
    elif ch == 4:
        list_persons(Q)
        input("press any key to continue......")

    elif ch == 5:
        search_name = input("Enter the name to search: ")
        found_person = search_person(Q, search_name)
        if isinstance(found_person, Person):
            print("Person found:")
            display_person(found_person)
        else:
            print(found_person)
        input("press any key to continue......")

    elif ch == 6:
        display(Q)
        input("press any key to continue......")

    elif ch == 7:
        break

    else:
        print("plz enter a right choice >_<")
