# we use variables to save and then re use data
first_name = "Geogre" # hard-coded value
last_name = "Washington"
age = 23
full_name = f'{first_name} {last_name}' # dynamically set
print(f'Hello {full_name}')

# hello full_name, you are age years old
greeting = f'Hello {full_name}, you are {age} years old!'

print(greeting)
