people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    newList = []
    for i in people:
        newList.append(i)
        
    for j in newList:
        if j == person_name:
            newList.remove(person_name)

    return newList

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))