string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
number_of_vowels = 0

for char in vowels:
    number_of_vowels += string.count(char)

print(number_of_vowels)
