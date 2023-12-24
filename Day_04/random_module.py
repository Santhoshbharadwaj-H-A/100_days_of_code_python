import random
#importing a own module  claaed"create a module"
import create_a_module

random_number = random.randint(1,10)
print(random_number)

#for flaot

random_float = random.random()
print(random_float)

#  between 0 and 5 random number

random_5 =  random_float * 5
print(random_5)

#calling the variable in the module

var_ran = create_a_module.pi
print(var_ran)