#!/usr/bin/env python3.7

"""23_Classes.py.

Twenty-Third Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
from datetime import date


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_23.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#23_Classes.py RUN / START")


class UserDemo:
    """docstring for User."""

    pass


user1 = UserDemo()
user1.first_name = "Dave"
user1.last_name = "Bowman"

first_name = "Arthur"
last_name = "Clark"

user2 = UserDemo()
user2.first_name = "Frank"
user2.last_name = "Poole"


print(first_name, last_name)
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)

user1.age = 37
user2.favorite_book = "2001 A Space Odyssey"

print(user1.age)
print(user2.favorite_book)

print('''
print(user2.age)
                Traceback (most recent call last):
                File "./23_Classes.py", line 52, in <module>
                    print(user2.age)
                AttributeError: 'User' object has no attribute 'age'

''')


class User:
    """Docstring for User class."""

    def __init__(self, full_name, birthday):
        """Docstring for __init__."""
        self.name = full_name
        self.birthday = birthday
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]

    def age(self):
        """""Return the age of the user in years."""
        today = date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365

        return int(age_in_years)


user = User("Dave Bowman", "19710315")

print("*" * 90)
print(user.name, user.first_name, user.last_name, user.birthday, user.age())
