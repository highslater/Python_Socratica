#!/usr/bin/env python3.7

"""15_Dictionaries.py.

Fifteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

post = {"user_id": 209,
        "message": "D5 E5 C5 C4 G4",
        "language": "English",
        "datetime": "20230215T124231Z",
        "location": (44.590533, -104.715556)
        }

post2 = dict(message="SS Cotopaxi", language="English")
post2["user_id"] = 209
post2["datetime"] = "19771116t093001Z"

for p in [post, post2]:
    print("\n", p, "\n")
    for i in p:
        print(i + "=", p[i])

print(post["message"])
print(post2["message"])
"""
print(post2["location"])

            Traceback (most recent call last):
            File "./15_Dictionaries.py", line 33, in <module>
                print(post2["location"])
            KeyError: 'location'

"""
if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value")


try:
    print(post2['location'])
except KeyError:
    print("The post does not have a location")

loc = post2.get('location', None)
print(loc)


for key in post.keys():
    value = post[key]
    print(key, "=", value)

for key, value in post.items():
    print(key, "=", value)
