list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(arr):
    odd = []
    even = []
    merged = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)
    merged.append(odd)
    merged.append(even)
    return merged

print(merge_two_list(list_of_numbers))