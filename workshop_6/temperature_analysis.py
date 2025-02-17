from datetime import datetime, timedelta
# temperatures = [27, 29]

temperatures = [
    {
        "temperature": 27,
        "date": datetime.now() - timedelta(days=1),
        "location": "Station 1",
    },
    {
        "temperature": 27,
        "date": datetime.now(),
        "location": "Station 1",
    },
    {
        "temperature": 28,
        "date": datetime.now() + timedelta(days=1),
        "location": "Station 1",
    },
    {
        "temperature": 30,
        "date": datetime.now() + timedelta(days=2),
        "location": "Station 1",
    },
    {
        "temperature": -2,
        "date": datetime.now(),
        "location": "Station 2",
    },
]


total_temp = 0
for record in temperatures:
    if record["location"] != "Station 1":
        continue
    print(record)
    total_temp += record["temperature"]

print(total_temp / len(temperatures))
