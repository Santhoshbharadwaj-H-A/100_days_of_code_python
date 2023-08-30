'''It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#12 months are there in a year
#52 weeks in a year
#365 days for there in a year 

age_in_integer = int(age)

age_remaining = 90 - age_in_integer
age_in_days = age_remaining * 365
age_in_weeks = age_remaining * 52
age_in_months = age_remaining * 12

print(f"you have days {age_in_days}, {age_in_weeks} weeks,and {age_in_months} months left.")


