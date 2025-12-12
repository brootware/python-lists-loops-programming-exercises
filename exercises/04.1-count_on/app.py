my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list = []

for elm in my_list:
    if type(elm) == dict or type(elm) == list:
        new_list.append(elm)

print(new_list)