user_number = int(input("Give the target number to add to the sum\n"))

sum_of_even = 0
for number in range(2, user_number + 1, 2):
    sum_of_even = sum_of_even + number
print(sum_of_even)