theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def converter(x):
    if x == 0:
        x = "woko"
    elif x == 1:
        x = "wiki"
    return x

newBools = list(map(converter,theBools))
print(newBools)