chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    newList = []
    for i in chunk_one:
        newList.append(i)

    for j in chunk_two:
        newList.append(j)

    return newList
    
print(merge_list(chunk_one, chunk_two))
