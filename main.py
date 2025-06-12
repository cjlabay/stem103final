from madlibs import *

# randomly pick mad libs story

import random
randmadlib = random.randint(1, 2)

# prompt user to provide words from lists, using generated story
# if randmadlib == 1:
       
person1 = get_word(people, "name")
noun1 = get_word(nouns, "object")
verb1 = get_word(verbs, "action")
verb2 = get_word(verbs, "action")
feeling1 = get_word(emotions, "emotion")
adjective1 = get_word(adjectives, "adjective")
food1 = get_word(foods, "food")
animal1 = get_word(animals, "animal")
color1 = get_word(colors, "color")
print(f'''
        This weekend I am going camping with {person1}. I packed my lantern, sleeping bag, and 
        {noun1}. I am so {feeling1} to {verb1} in a tent. We are going to hike, fish, and {verb2}. 
         If I see a {color1} {animal1} while hiking, I am going to bring it home as a pet! 
        At night we will tell {adjective1} stories and roast {food1} around the campfire!!''')