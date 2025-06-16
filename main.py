from madlibs import *

# randomly pick mad libs story

import random
randmadlib = random.randrange(2)

# prompt user to provide words from lists, using generated story

if randmadlib == 0:   
        name1 = get_word(names, "name")
        noun1 = get_word(nouns, "object")
        verb1 = get_word(verbs, "action")
        verb2 = get_word(verbs, "second action")
        emotion1 = get_word(emotions, "emotion")
        adjective1 = get_word(adjectives, "adjective")
        food1 = get_word(foods, "food")
        animal1 = get_word(animals, "animal")
        color1 = get_word(colors, "color")
        number1 = get_word(numbers, "number")
        time1 = get_word(times, "unit of time")
        print(f'''
        This weekend I am going camping with {name1}. I packed my lantern, sleeping bag, and {noun1}.
        I am so {emotion1} to {verb1} in a tent. We are going to hike, fish, and {verb2}. 
        Then we will hike through the forest for {number1} {time1}.
        If I see a {color1} {animal1} while hiking, I am going to bring it home as a pet! 
        At night we will tell {adjective1} stories and roast {food1} around the campfire!!''')
        
if randmadlib == 1:
        name1 = get_word(names, "name")
        noun1 = get_word(nouns, "object")
        verb1 = get_word(verbs, "action")
        adjective1 = get_word(adjectives, "adjective")
        adjective2 = get_word(adjectives, "second adjective")
        food1 = get_word(foods, "food")
        animal1 = get_word(animals, "animal")
        animal2 = get_word(animals, "second animal")
        animal3 = get_word(animals, "third animal")
        color1 = get_word(colors, "color")
        number1 = get_word(numbers, "number")
        time1 = get_word(times, "unit of time")
        print(f'''
             Dear {name1}, 
        I am writing to you from a {adjective1} castle in an enchanted forest. I found myself here
        one day after following a {color1} {animal1}. There are magical {animal2}s and {animal3}s that {verb1}.
        I fall asleep each night on a bed of {food1} and dream of {adjective2} {noun1}s. 
        It feels as though I have lived here for {number1} {time1}. I hope one day you can visit, 
        although the only way to get here now is by finding the {color1} {animal1}!''')