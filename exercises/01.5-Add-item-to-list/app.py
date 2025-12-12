# Remember to import random function here

my_list = [4, 5, 734, 43, 45]

# The magic goes below
import random
for i in range(10):
    my_random_int = random.randint(1,10)
    my_list.append(my_random_int)

print(my_list)