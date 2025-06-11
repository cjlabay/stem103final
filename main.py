from functions import *

# randomly pick mad libs story

import random
randmadlib = random.randint(1, 2)

# prompt user to provide words from lists, using generated story
# if randmadlib == 1:
#         get_word([people], "name")
       
get_word(person1, [people], "name")
get_word(noun1, [nouns], "object")





print(f'''
        This weekend I am going camping with {person1}. I packed my lantern, sleeping bag, and 
        {noun1}. I am so {feeling1} to {verb1} in a tent. We are going to hike, fish, and {verb2}. 
         If I see a {color1} {animal1} while hiking, I am going to bring it home as a pet! 
        At night we will tell {adjective1} stories and roast {food1} around the campfire!!''')