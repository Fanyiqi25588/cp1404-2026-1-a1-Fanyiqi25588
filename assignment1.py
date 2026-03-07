"""
CP1404 Assignment 1 - Travel Tracker
Name: FAN YIQI
GitHub: https://github.com/Fanyiqi25588/cp1404-2026-1-a1-Fanyiqi25588.git
"""

FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0")

    places = load_places(FILENAME)

    choice = ""
    while choice != "Q":
        display_menu()
        choice = input(">>> ").upper()

        if choice == "D":
            print("Display places")

        elif choice == "R":
            print("Recommend place")

        elif choice == "A":
            print("Add place")

        elif choice == "M":
            print("Mark visited")

        elif choice == "Q":
            save_places(FILENAME, places)
            print("Have a nice day :)")

        else:
            print("Invalid menu choice")


def display_menu():
    print("Menu:")
    print("D - Display all places")
    print("R - Recommend a random place")
    print("A - Add a new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def load_places(filename):
    places = []

    in_file = open(filename, "r")

    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        country = parts[1]
        priority = int(parts[2])
        visited = parts[3]

        place = [name, country, priority, visited]
        places.append(place)

    in_file.close()

    print(f"{len(places)} places loaded from {filename}")

    return places


def save_places(filename, places):
    pass


main()