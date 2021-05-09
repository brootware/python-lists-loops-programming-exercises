def lyrics_generator(arr):
    lyrics = ""
    count = 0
    for i in arr:
        if i == 0:
            lyrics += "Boom "
        elif i == 1:
            count += 1
            lyrics += "Drop the base "
            if count > 2:
                lyrics += "!!!Break the base!!! " 

    return lyrics

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
