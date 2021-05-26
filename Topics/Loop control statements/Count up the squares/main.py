# put your python code here
the_sum = int(input())
sum_of_squares = the_sum ** 2

while the_sum != 0:
    n = int(input())
    the_sum += n
    sum_of_squares += n ** 2

print(sum_of_squares)
