# put your python code here
a = int(input())
b = int(input())
numbers = []

for x in range(a, b + 1):
    if x % 3 == 0:
        numbers.append(x)

print(sum(numbers) / len(numbers))
