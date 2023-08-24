import random

template1 = '''It was about {0} {1} ago when I arrived at the hospital in a {2}. 
The hospital is a/an {3} place, there are a lot of {4} {5} here. There are nurses here who
have {6} {7}. If someone wants to come into my room I told them that they have to {8} first.
I've decorated my room with {9} {10}. Today I talked to a doctor and they were wearing a {11} on 
their {12}. I heard that all doctors {8} {13} every day for breakfast. The most {14} thing 
about being in the hospital is the {15} {5} !'''

template2 = '''This weekend I am going camping with {0}. I packed my lantern, sleeping bag, and {1}. 
I am so {2} to {3} in a tent. I am {4} we might see a(n) {5}, I hear they're kind of dangerous. 
While we're camping, we are going to hike, fish, and {6}. I have heard that the {7} lake is great for {8}. 
Then we will {9} hike through the forest for {10} {11}. If I see a {7} {5} while hiking, 
I am going to bring it home as a pet! At night we will tell {10} {11} stories and roast {12} around the campfire!!'''

template3 = '''Dear {0}, I am writing to you from a {1} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {2} {3} in {4}. There are {5} {6} and {7} {8} here! 
In the {9} there is a pool full of {10}. I fall asleep each night on a {11} of {12} and dream of {13} {14}. 
It feels as though I have lived here for {15} {16}. I hope one day you can visit, although the only way
 to get here now is {17} on a {18} {19}!!'''

templates = [template1, template2, template3]
selected_template = random.choice(templates)

if selected_template == template1:
    print("Randomly selected template is Template 1\n")
    number = input("Type in a number:\n")
    measure_of_time = input("Type in a measure of time in the plural form:\n")
    transportation_mode = input("Type in a mode of transportation:\n")
    adjective = input("Type in an adjective:\n")
    adjective2 = input("Type in one more adjective:\n")
    noun = input("Type in a noun in the plural form:\n")
    color = input("Type in a color:\n")
    body_part = input("Type in a part of a body in the plural form:\n")
    verb = input("Type in a verb:\n")
    number2 = input("Type in a number:\n")
    noun2 = input("Type in a noun in the plural form:\n")
    noun3 = input("Type in one more noun:\n")
    body_part2 = input("Type in a part of a body:\n")
    noun4 = input("Type in a noun:\n")
    adjective3 = input("Type in an adjective:\n")
    silly_word = input("Type in a silly word:\n")
    print(template1.format(number, measure_of_time, transportation_mode, adjective, adjective2, noun, color, body_part, verb, number2, noun2, noun3, body_part2, noun4, adjective3, silly_word))
elif selected_template == template2:
    print("Randomly selected template is Template 2:\n")
    name = input("Type in a proper noun:\n")
    noun = input("Type in a noun:\n")
    adjective_feeling = input("Type in an adjective describing a feeling:\n")
    verb = input("Type in a verb:\n")
    adjective_feeling2 = input("Type in another adjective describing a feeling:\n")
    animal = input("Type in an animal:\n")
    verb2 = input("Type in a verb:\n")
    color = input("Type in a color:\n")
    verb_ing = input("Type in a verb ending in 'ing':\n")
    adverb = input("Type in an adverb ending in ly:\n")
    number = input("Type in a number:\n")
    measure_of_time = input("Type in a measure of time in the plural form:\n")
    silly_word = input("Type in a silly word:\n")
    noun2 = input("Type in a number:\n")
    print(template2.format(name, noun, adjective_feeling, verb, adjective_feeling2, animal, verb2, color, verb_ing, adverb, number, measure_of_time, silly_word, noun2))
elif selected_template == template3:
    print("Randomly selected template is Template 3:\n")
    name = input("Type in a proper noun:\n")
    adjective = input("Type in an adjective:\n")
    color = input("Type in a color:\n")
    animal = input("Type in an animal:\n")
    place = input("Type in a place:\n")
    adjective2 = input("Type in an adjective:\n")
    magical_creature = input("Type in a magical creautre in the plural form:\n")
    adjective3 = input("Type in an adjective:\n")
    magical_creature2 = input("Type in another magical creauture in the plural form:\n")
    room = input("Type in a room in a house:\n")
    noun = input("Type in a noun in the plural form:\n")
    noun2 = input("Type in another noun:\n")
    noun3 = input("Type in another noun in the plural form:\n")
    adjective4 = input("Type in an adjective:\n")
    noun4 = input("Type in a noun in the plural form:\n")
    number = input("Type in a number:\n")
    measure_of_time = input("Type in a measure of time in the plural form:\n")
    verb = input("Type in a verb ending with 'ing':\n")
    adjective5 = input("Type in an adjective:\n")
    noun5 = input("Type in a noun:\n")
    print(template3.format(name, adjective, color, animal, place, adjective2, magical_creature, adjective3, magical_creature2, room, noun, noun2, noun3, adjective4, noun4, number, measure_of_time, verb, adjective5, noun5))







































