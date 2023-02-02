#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator.")
total = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
price = (total / people) * (1 + (tip * 0.01))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
price = str(round(price, 2))
#Write your code below this line 👇
print("Each person should pay:" + price)
