list_of_floats = []
while True:
    n = input()
    if n != ".":
        list_of_floats.append(float(n))
    else:
        print(min(list_of_floats))
        break
