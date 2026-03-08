"""
CP1404 Assignment 1 - Travel Tracker
Name: FAN YIQI
GitHub: https://github.com/Fanyiqi25588/cp1404-2026-1-a1-Fanyiqi25588.git
"""

import random

FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0")

    places = load_places(FILENAME)

    choice = ""
    while choice != "Q":
        display_menu()
        choice = input(">>> ").upper()

        if choice == "D":
            display_places(places)

        elif choice == "R":
            recommend_place(places)

        elif choice == "A":
            add_place(places)

        elif choice == "M":
            mark_visited(places)

        elif choice == "Q":
            save_places(FILENAME, places)
            print("Have a nice day :)")

        else:
            print("Invalid menu choice")


def display_menu():
    print("\nMenu:")
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
    out_file = open(filename, "w")

    for place in places:
        line = f"{place[0]},{place[1]},{place[2]},{place[3]}\n"
        out_file.write(line)

    out_file.close()


def display_places(places):
    places.sort(key=lambda place: (place[3], place[2]))

    unvisited_count = 0

    for i, place in enumerate(places, start=1):
        name = place[0]
        country = place[1]
        priority = place[2]
        visited = place[3]

        if visited == "n":
            symbol = "*"
            unvisited_count += 1
        else:
            symbol = " "

        print(f"{symbol}{i}. {name} in {country} priority {priority}")

    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")


def add_place(places):
    name = get_non_blank_input("Name: ")
    country = get_non_blank_input("Country: ")
    priority = get_valid_number("Priority: ")

    place = [name, country, priority, "n"]
    places.append(place)

    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def recommend_place(places):
    unvisited_places = []

    for place in places:
        if place[3] == "n":
            unvisited_places.append(place)

    if len(unvisited_places) == 0:
        print("No unvisited places left.")
        return

    place = random.choice(unvisited_places)

    print(f"Why not visit {place[0]} in {place[1]}?")


def mark_visited(places):
    display_places(places)

    number = get_valid_number("Enter the number of a place to mark as visited: ")

    if number < 1 or number > len(places):
        print("Invalid place number")
        return

    place = places[number - 1]

    if place[3] == "v":
        print(f"You have already visited {place[0]}")
    else:
        place[3] = "v"
        print(f"{place[0]} in {place[1]} marked as visited")


def get_non_blank_input(prompt):
    text = input(prompt).strip()

    while text == "":
        print("Input cannot be blank")
        text = input(prompt).strip()

    return text


def get_valid_number(prompt):
    number = input(prompt)

    while not number.isdigit() or int(number) <= 0:
        print("Number must be > 0")
        number = input(prompt)

    return int(number)


main()