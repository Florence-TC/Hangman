total = 0
count = 0

while True:
    n = input()
    if n != ".":
        total += int(n)
        count += 1
    else:
        print(total / count)
        break
