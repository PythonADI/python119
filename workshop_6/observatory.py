"""
EXAMPLE

>>> Start Date: 01/02/2025
>>> Station: Station 1
Enter (Temperature)
>>> 27
Successfully recorded (01/02/2025, 27, Station 1)
>>> 28
Successfully recorded (02/02/2025, 28, Station 1)
>>> -101
Temperature should be in range [-100 - 100]
>>> 9
Successfully recorded (03/02/2025, 9, Station 1)


>>> Bottle of water, 10, 1.5
{
    "title": "Bottle of water",
    "quantity": 10,
    "price": 1.5,
    "total_price": 15
}
"""
from datetime import datetime, timedelta


date_format = "%d/%m/%Y"
start_date = input(f"Start Date ({date_format}): ")
start_date = datetime.strptime(start_date, date_format)
start_date = start_date.date()
last_record_date = start_date

station = input("Station: ")
print("Enter Temperatures (END to finish recording): ")
temperatures = []

while True:
    temperature = input(">>> ")
    if temperature == "END":
        print("Recording Process finished!")
        break
    if not temperature.isdigit():
        print("Please provide correct temperature number")
        continue

    temperature = int(temperature)
    if temperature < -100 or 100 < temperature:
        print("Temperature should be in range [-100 - 100]")
        continue

    temperatures.append({
        "temperature": temperature,
        "station": station,
        "date": last_record_date
    })
    print(f"Successfully recorded ({temperature}, {last_record_date}, {station})")
    last_record_date += timedelta(days=1)


for record in temperatures:
    print(f"[{record['date']}] {record['temperature']} - {record['station']}")
# print(temperatures)
