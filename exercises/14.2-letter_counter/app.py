par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for char in par:
    if char != ' ':
        if char.lower() in counts:
            counts[char.lower()] += 1
        else:
            counts[char.lower()] = 1
    

print(counts)
# print(counts)

