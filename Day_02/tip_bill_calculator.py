#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator")
total_bill = float(input("what was the total bill ?"))
tip_percentage = float(input("what is the percentage of the tip wold you like to give? "))
number_person = int(input("how many people wolud you like to spilt the bill"))

final = ((total_bill * (1 + tip_percentage/100)) / number_person )

# print(round(final,2))






