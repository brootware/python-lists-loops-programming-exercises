#Remember import random function here:
import random
my_list = [4,5,734,43,45]

for i in range(10):
    generateRandom = random.randint(0,10)
    my_list.append(generateRandom)

print(my_list)
#The magic is here:
