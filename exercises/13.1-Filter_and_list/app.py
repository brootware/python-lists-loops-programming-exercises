all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def filter_R_initials(name:str) -> str:
    return name.startswith('R')

resulting_names = list(filter(filter_R_initials,all_names))
print(resulting_names)




