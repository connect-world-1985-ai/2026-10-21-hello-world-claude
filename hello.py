import sys

from greetings import greet


def menu():
    while True:
        print("1) Greet World\n2) Greet a name\n3) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            greet()
        elif choice == "2":
            name = input("Name: ").strip() or "World"
            greet(name)
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")


if "--menu" in sys.argv:
    menu()
else:
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    greet(name)
