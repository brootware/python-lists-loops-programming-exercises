def lyrics_generator(beats:list) -> str:
    lyrics = ""
    count = 0

    for beat in beats:
        if beat == 0:
            lyrics += 'Boom '
            count = 0
        elif beat == 1:
            lyrics += 'Drop the bass '
            count += 1

            if count == 3:
                lyrics += "!!!Break the bass!!! "
                count = 0

    return lyrics
        


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
