scores = input().split()
# put your python code here
lives = 3
score = 0

for answer in scores:
    if lives > 0:
        if answer == 'C':
            score += 1
        else:
            lives -= 1
    else:
        print("Game over")
        print(score)
        break
else:
    print("You won")
    print(score)
