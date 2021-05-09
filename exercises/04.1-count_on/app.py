
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for i in range(len(my_list)):
    print(my_list[i])
    if type(my_list[i]) == list or type(my_list[i]) == dict:
        hello.append(my_list[i])

print(hello)
