# Data Structure - Dictionary
from datetime import datetime

print(datetime.now().timestamp())
day_1 = {
    # key: value
    "temperature": 27,
    "date": datetime.now(),
    "location": "Station 1",
    "scientist": {
        "first_name": "Nick",
        "last_name": "Washington",
        "age": 35,
        "pet": {
            "type": "dog",
            "name": "doggo",
            "age": 3
        }
    },
}


print(day_1["temperature"])
print(day_1["date"])

print(day_1["scientist"]["first_name"])
print(day_1["scientist"]["pet"]["name"])
