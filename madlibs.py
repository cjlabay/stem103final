# lists of acceptable inputs
# initialize lists
# random options partially provided by perchance.org random generators

names = ["Bob", "Branson", "Rex", "Ronald", "Marques", "Zayden", "Elsa", "Jada", "Dani", "Julia", "Kelsie", "Anabelle"]
nouns = ["guitar", "crowbar", "bed", "old tin can", "soccer ball", "coffee pot", "toilet", "purse", "baseball hat", "hammer", "bottle cap", "steak knife"]
verbs = ["jump", "sail", "stand", "explode", "swim", "fly", "teleport", "fall", "mine", "live", "sleep", "evolve"]
adjectives = ["glorious", "dark", "gloomy", "funny", "short", "nice", "chewy", "shallow", "spicy", "bad", "scary", "true"]
emotions = ["ashamed", "excited", "proud", "afraid", "furious", "mad", "interested", "happy", "remorseful", "disappointed"]
animals = ["beaver", "raccoon", "peacock", "dog", "cat", "hedgehog", "kangaroo", "dolphin", "gnu", "rat", "squirrel", "bear"]
foods = ["radish", "beans", "mangoes", "hamburgers", "soup", "steak", "popcorn", "marshmallows", "chocolates", "ice cream"]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "brown", "gray", "white"]
numbers = ["2", "3", "5", "7", "9", "12", "20", "50", "100", "1000"]
times = ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]

#initializing variables (to be changed later by user)
name1 = ""
noun1 = ""
noun2 = ""
verb1 = ""
verb2 = ""
adjective1 = ""
adjective2 = ""
emotion1 = ""
animal1 = ""
animal2 = ""
animal3 = ""
color1 = ""
food1 = ""
number1 = ""
time1 = ""

#function to get word required by madlib with function inputs of list and specified category

import random
def get_word(list, category):
    init_words = True
    while init_words:
        option = input(f"Mad Lib {category} selection: {list} \nInput a shown {category} or type 1 for random: ")
        if option == "1":
            option = random.choice(list)
            return option
        elif option in list:
            return option
        else: 
            print("Invalid option. Please choose an item from the list.")