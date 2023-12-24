names_string = "abcde"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# who pays the bill project
# 🚨 Don't change the code above 👆


import random

num_item = len(names)
print(num_item)

random_choice = random.randint(0, num_item-1)
print(random_choice)

person_who_will_pay_the_bill = names[random_choice] 

print(person_who_will_pay_the_bill + "is the persion who will pay the bill")
