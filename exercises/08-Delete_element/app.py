people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    updated_list = list(people)

    for i in updated_list:
        if i == person_name:
            updated_list.remove(i)
    
    return updated_list
    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
