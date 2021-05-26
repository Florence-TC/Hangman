cat_cafe = ""
chosen_cafe = ""
cat_number = 0
max_cat_number = 0

while True:
    string = input()
    if "MEOW" in string:
        break
    else:
        i = string.find(" ")
        cat_cafe = string[:i]
        cat_number = int(string[i + 1:])
        if cat_number > max_cat_number:
            max_cat_number = cat_number
            chosen_cafe = cat_cafe

print(chosen_cafe)
