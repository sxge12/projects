from datetime import datetime


def load_rooms(file_name, dictionary):
    # this has been implemented for your
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            room_id, details_str = line.split(":")
            details = details_str.split(",")
            dictionary[room_id] = {"type": details[0], "cost": details[1], "details": details[2]}
    return dictionary


def load_reservations(file_name, dictionary):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            room_id, details_str = line.split(":")
            details = details_str.split(",")
            newdict = {"name": details[0], "check in": details[1], "check out": details[2]}
            if room_id in dictionary:
                dictionary[room_id].append(newdict)
            else:
                dictionary[room_id] = [newdict]
    return dictionary

def display_rooms(dictionary):
    print(dictionary)


def compareDates(check_in, check_out, res_check_in, res_check_out):
    # this has been implemented for you
    # Compares the dates of a new reservation (check_in, check_out) with an existing reservation (res_check_in, res_check_out) to determine if there is a conflict.
    # If there is any overlap between the two date ranges, the function returns True (indicating a conflict).
    # Otherwise, it returns False (indicating no conflict).

    check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
    check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
    res_check_in_date = datetime.strptime(res_check_in, "%Y-%m-%d")
    res_check_out_date = datetime.strptime(res_check_out, "%Y-%m-%d")
    return not (check_out_date <= res_check_in_date or check_in_date >= res_check_out_date)


def check_availability(rooms, reservations, check_in, check_out):
    available_rooms = []

    for room in rooms:
        if room in reservations:
            conflict = False
            for res in reservations[room]:
                if compareDates(check_in, check_out, res["check in"], res["check out"]):
                    conflict = True
                    break
            if not conflict:
                available_rooms.append(room)
        else:
            available_rooms.append(room)

    if available_rooms:
        print("Here are the rooms available within that timeframe:")
        for r in available_rooms:
            print(r, rooms[r])
    else:
        print("No rooms available for these dates.")








def make_reservation(rooms, reservations):
    room_num = input("Enter room number you want to book: ")
    if room_num not in rooms:
        print("Room does not exist.")
        return

    guest_name = input("Enter guest name: ")
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    # Check availability
    if room_num in reservations:
        for res in reservations[room_num]:
            if compareDates(check_in, check_out, res["check in"], res["check out"]):
                print("Room is not available for these dates.")
                return

    # Add reservation
    new_res = {"name": guest_name, "check in": check_in, "check out": check_out}
    if room_num in reservations:
        reservations[room_num].append(new_res)
    else:
        reservations[room_num] = [new_res]

    print(f"Reservation confirmed for room {room_num} from {check_in} to {check_out}.")







def view_reservations(reservations):
    if not reservations:
        print("No reservations yet.")
        return

    for room, res_list in reservations.items():
        print(f"\nRoom {room}:")
        for res in res_list:
            print(f"  Guest: {res['name']}, Check-in: {res['check in']}, Check-out: {res['check out']}")


# write your code here


rooms = {}
reservations = {}

load_rooms("Rooms.txt", rooms)
load_reservations("Reservations.txt", reservations)

while True:
    print("\nWelcome to the Hotel Booking Assistant!")
    print("1. View All Rooms")
    print("2. Check Availability (with Dates)")
    print("3. Make a Reservation")
    print("4. View Current Reservations")
    print("5. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        display_rooms(rooms)
    elif choice == "2":
        check_in = input("Enter check-in date (YYYY-MM-DD): ")
        check_out = input("Enter check-out date (YYYY-MM-DD): ")
        check_availability(rooms, reservations, check_in, check_out)
    elif choice == "3":
        make_reservation(rooms, reservations)
    elif choice == "4":
        view_reservations(reservations)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

    # continue here

