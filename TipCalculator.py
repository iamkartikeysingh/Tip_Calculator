print("Welcome to the Tip Calculator")
totalBill = float(input("What was the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
totalTip = (totalBill * percent/100)+totalBill
numberOfPersons = int(input("How many people to split the bill? "))
result = round(totalTip/numberOfPersons, 2)
print(f"Each person should pay: {result}")