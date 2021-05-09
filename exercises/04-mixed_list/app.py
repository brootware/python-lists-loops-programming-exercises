mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
def findType(arr):
    for i in range(len(arr)):
        print(type(arr[i]))

print(findType(mix))