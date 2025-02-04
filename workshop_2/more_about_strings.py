# text = "      This has many spaces      " # hard coded
text = input("Enter some text: ") # dynamically set

print(f'"{text}"')
print(f'"{text.strip()}"')
print(f'"{text.lstrip()}"')
print(f'"{text.rstrip()}"')
# assignment operator
text = text.strip()
print(f'"{text}"')

# lower / upper case
print(text.upper())
print(text.lower())
text = text.upper()
print(text)
text = text.capitalize()
print(text)
text = text.title()
print(text)

print(f"{text.startswith('Test') = }")
print(f"{text.endswith('test') = }")
