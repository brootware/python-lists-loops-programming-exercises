the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def wiki_woko(num:int) -> int:
    if num == 0:
        return 'woko'
    if num == 1:
        return 'wiki'
    
new_list = list(map(wiki_woko,the_bools))
print(new_list)