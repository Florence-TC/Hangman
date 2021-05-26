camel_case = input()
new_name = camel_case[0].lower()

for char in camel_case[1:]:
    if char.isupper():
        char = "_" + char.lower()
    new_name += char
print(new_name)
