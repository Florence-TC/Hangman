for i in range(1, 101):
    if i % 3 != 0:
        if i % 5 != 0:
            print(i)
        else:
            print("Buzz")
    else:
        if i % 5 != 0:
            print("Fizz")
        else:
            print("FizzBuzz")
