income = int(input())

if income <= 15527:
    calculated_tax = 0
elif income <= 42707:
    calculated_tax = income * 0.15
elif income <= 132406:
    calculated_tax = income * 0.25
else:
    calculated_tax = income * 0.28

calculated_tax = round(calculated_tax)

percent = round(calculated_tax / income * 100)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
