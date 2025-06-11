# lists of acceptable inputs
# initialize lists
# random options partially provided by perchance.org random generators

people = ["Bob", "Branson", "Rex", "Ronald", "Marques", "Zayden", "Elsa", "Jada", "Dani", "Julia", "Kelsie", "Anabelle"]
nouns = ["dolphin", "crowbar", "bed", "can of peas", "soccer ball", "coffee pot", "toilet", "purse", "baseball hat", "hammer", "bottle cap", "steak knife"]
verbs = ["prepare", "boast", "stand", "explode", "taste", "carry", "teleport", "fall", "mine", "remember", "sleep", "squeeze"]
adjectives = ["firmer", "old", "gloomy", "funny", "short", "nice", "chewy", "shallow", "spicy", "bad", "scary", "true"]
emotions = ["ashamed", "excited", "proud", "afraid", "furious", "mad", "interested", "happy", "remorseful", "disappointed"]
animals = ["beaver", "raccoon", "peacock", "dog", "cat", "hedgehog", "kangaroo", "squirrel", "gnu", "fox", "goose", "bear"]
foods = ["radish", "beans", "mangoes", "hamburgers", "soup", "steak", "popcorn", "marshmallows", "chocolates", "ice cream"]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "brown", "gray", "white"]

#initializing variables (to be changed later by user)
person1 = ""
noun1 = ""
verb1 = ""
verb2 = ""
adjective1 = ""
feeling1 = ""
animal1 = ""
color1 = ""
food1 = ""

#function to get word required by madlib with function inputs of list and specified category

def get_word(word, list, category):
    init_words = True
    while init_words:
        option = input(f"Mad Lib {category} selection: {list} \nInput a shown {category}: ")
        if option in list:
            word = option
            return word
        else: 
            print("Invalid option. Please choose an item from the list.")