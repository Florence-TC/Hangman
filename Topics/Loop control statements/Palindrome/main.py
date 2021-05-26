word = input()
for i in range(len(word) // 2):
    palindrome = word[i] == word[len(word) - 1 - i]
    if not palindrome:
        print("Not palindrome")
        break
else:
    print("Palindrome")
