# ask in this lab is to implement a Hotel Booking Assistant App with the following features:
# # 1. View Available Rooms
# # o Displays all available rooms and their details (room type, price, and amenities).
# 2. Make a Reservation
# o Allows users to book a room based on availability.
# 3. View Current Reservations
# o Displays all reservations made by guests.
# The program uses the following two files (Rooms.txt, Reservations.txt), with examples of their format
# provided below:
# Rooms.txt
# Room101:Single,50,Includes free Wi-Fi and breakfast.
# Room102:Double,75, Includes free Wi-Fi, breakfast, and ocean view.
# Room201:Suite,120,Includes free Wi-Fi, breakfast, and a jacuzzi.
# Reservations.txt
# Room101:John Doe,2024-11-25,2024-11-28.
# Room102:Jane Smith,2024-11-30,2024-12-03.
# Develop a program that enables users to interact with this hotel booking system, manage reservations,
# and check room availability.
# Steps to Follow:
# a. Create Empty Dictionaries
# Create two empty dictionaries: one for room details (“rooms”), and one for reservations
# (“reservations”).
# The rooms dictionary stores the details of all hotel rooms. Each key is the room number (e.g.,
# "Room101"), and the value is another dictionary containing the following attributes:
# • "type": The type of the room (e.g., "Single", "Double", "Suite").
# • "cost": The cost per night of the room (e.g., "50").
# • "details": Additional details or amenities for the room (e.g., "Includes free Wi-Fi and
# breakfast").
# The reservations dictionary keeps track of all current reservations. Each key is the room number (e.g.,
# "Room101"), and the value is a list of dictionaries. Each inner dictionary in the list contains:
# • "name": The name of the guest who made the reservation.
# • "check-in": The check-in date (YYYY-MM-DD format).
# • "check-out": The check-out date (YYYY-MM-DD format).
# b. Define the Function load_rooms
# Write a function called load_rooms that accepts two parameters:
# • A string representing a file name.
# • A dictionary which represents the room's dictionary.
# This function should:
# • Open the specified file.
# • Populate the dictionary with key-value pairs based on the file's contents.
# b. Define the Function load_reservations
# Write a function called load_reservations that accepts two parameters:
# • A string representing a file name.
# • A dictionary which represents the reservation’s dictionary.
# Function Requirements:
# • Open and read the specified file line by line.
# • For each line, extract the room number (key) and reservation details (value).
# • The reservation details should include:
# o Guest name.
# o Check-in date.
# o Check-out date.
# Note: Be cautious when handling multiple lines that reference the same room. Instead of overwriting
# the existing key, ensure the reservation list for that room is updated correctly.
# • If a room already exists in the dictionary, append the new reservation to the list of
# reservations for that room.
# • If a room does not exist in the dictionary, create a new key with the room number and
# initialise its value as a list containing the reservation details.
# c. Define the Function display_rooms
# Write a function that accepts the room dictionary as a parameter and prints all room detail.
# d. Define the Function display_reservations
# Write a function that accepts the reservations dictionary as a parameter and prints all reservations.
# e. Define the Function check_availability
# Write a function named check_availability that takes the following parameters:
# • A dictionary representing the room’s dictionary
# • A dictionary representing the reservations
# • Two strings representing the desired check-in and check-out dates in the format YYYY-MM-
# DD.
# Function Requirements:
# - Iterate through all the rooms in the rooms dictionary.
# - For each room:
# ▪ Check if it exists in the reservations dictionary.
# ▪ If the room is reserved, compare the requested check-in and check-
# out dates with the existing reservations. A room is not available if the
# requested dates overlap with any existing reservation.
# ▪ If no overlap is found or the room has no reservations, it is considered
# available.
# - Print the details of all available rooms, including the room number, type, cost, and
# additional details.
# f. Define the Function make_reservation
# Write a function named make_reservation that takes the following parameters:
# 1. A dictionary representing the rooms
# 2. A dictionary representing the reservations
# Function Requirements:
# • Prompt the user to enter the following details:
# o Name: The guest's name.
# o Check-in date: The desired check-in date in the format YYYY-MM-DD.
# o Check-out date: The desired check-out date in the format YYYY-MM-DD.
# • Use the check_availability function to display a list of all available rooms for the specified
# dates.
# • Prompt the user to choose a room number from the available options.
# • Validate the room choice:
# o If the selected room exists and is available:
# ▪ Add the reservation to the reservations dictionary:
# ▪ If the room already has reservations, append the new reservation to
# its list.
# ▪ If the room has no existing reservations, create a new list and add the
# reservation.
# ▪ Save the reservation to the reservations file (Reservations.txt) in the
# appropriate format
# g. Create the Interactive Menu: Display the following menu to the user:
# Welcome to the Hotel Booking Assistant!
# Choose an option:
# 1. View All Rooms
# 2. Check Availability
# 3. Make a Reservation
# 4. View Current Reservations
# 5. Exit

