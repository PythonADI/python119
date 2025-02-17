student = {
    "first_name": "Nick",
    "age": 21
}

# access
print(student["first_name"])

# modify
# student["age"] = student["age"] + 1
student["age"] += 1
print(student["age"])

# removing item
# del student["age"]
student.pop("age")
print(student)


# adding new items (key value pair)
student["university"] = "Stanford"
print(student)
