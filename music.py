import time
import sys

def print_lyrics():
    lyrics = [
        "Maybe it's 6:45",
        "Maybe I'm barely alive",
        "Maybe you've taken my shit for the last time, yeah",
        "Maybe I know that I'm drunk",
        "Maybe I know you're the one",
        "Maybe you thinking it's better if you drive",
        "- Oh, 'cause girls like you run 'round with guys like me",
        "'Til sun down when I come through,",
        "I need a girl like you, yeah"
    ]

    delays = [0.7, 0.2, 0.5, 0.5, 0.5, 1.1, 0.5, 0.5, 0.3]

    print("Girls like you: \n")
    time.sleep(1.2)
 
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()     
            time.sleep(0.06)       

        print() 
        

        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.5) 

if __name__ == "__main__":

    print_lyrics()

import time
import sys

def print_riptide_lyrics_extended():
    lyrics = [
        "There's this movie I think you will like",
        "This guy decides to give up his job and",
        "He moves to paradise",
        "", 
        "This island gives him a new start,",
        "And a new perspective",
        "From an old friend",
        "", 
        "I just wanna be your left hand man",
        "I saw you sitting in the sand",
        "Tearin' out your hair",
        "",
        "Riptide, 'til I'm caught in your riptide",
        "Dragging me away to the dark side",
        "I wanna be your left hand man"
    ]

    delays = [
        1.1,  # After "I think you will like"
        1.3,  # After "give up his job and"
        1.5,  # After "moves to paradise"
        0.5,  # After the first visual break
        1.2,  # After "new start,"
        1.5,  # After "new perspective"
        2.5,  # After "old friend"
        0.7,  # After the second visual break
        1.5,  # After "left hand man"
        1.0,  # After "sitting in the sand"
        2.0,  # After "Tearin' out your hair"
        0.5,  # After the third visual break
        1.8,  # After "caught in your riptide"
        1.5,  # After "dark side"
        2.0   # End of section
    ]

    print("Vance Joy - Riptide (Extended):\n")
    time.sleep(1.5) 

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        
        print() 
        
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.5)

if __name__ == "__main__":
    print_riptide_lyrics_extended()
