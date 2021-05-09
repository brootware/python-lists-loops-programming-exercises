my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def average(arr):
    total = 0
    mean = 0
    for i in arr:
        total += i

    mean = total / len(arr)-1
    return mean

print(average(my_list))