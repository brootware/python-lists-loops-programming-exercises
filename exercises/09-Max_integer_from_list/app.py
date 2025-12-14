my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(num_list:list) -> list:
    max_num = 0
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

print(max_integer(my_list))