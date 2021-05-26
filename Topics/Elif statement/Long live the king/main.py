column = int(input())
row = int(input())

if column in (1, 8):
    if row in (1, 8):
        print(3)
    else:
        print(5)
elif row in (1, 8):
    print(5)
else:
    print(8)
