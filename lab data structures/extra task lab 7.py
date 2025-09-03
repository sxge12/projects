import random
from random import randint

a = open("available_books.txt")
r = open("requests_lists.txt")

visitor_requests = {}
available_books_list = []

EKEY = randint(1,100)

newlineR = r.readline()
newlineA = a.readline()
while newlineR != " ":
    bits = newlineR[ :-1].split(",")
    visitor_requests[bits[0]] = bits[1]
    r.readline()
while newlineA != " ":
    available_books_list = newlineA
    a.readline()
encrypted_requests = {}

if visitor_requests





