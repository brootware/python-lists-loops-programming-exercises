
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filterInitials(x):
    x = x.lower()
    if x[0] == 'r':
        return x

resulting_names = list(filter(filterInitials,all_names))
print(resulting_names)




