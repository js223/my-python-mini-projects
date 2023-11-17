# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ______ "
# youtuber = "John" # some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
import random


def Madlibs_generator():
    noun_box = ""
    plural_noun_box = ""
    adjective_box = ""
    
    for i in range(4):
        noun = input("Enter noun: ")
        noun_box = noun_box + noun + " "
          
    for i in range(6):
        plural_noun = input("Enter plural noun: ")
        plural_noun_box = plural_noun_box + plural_noun + " "
    
    for i in range(2):
        adjective = input("Enter adjective: ")
        adjective_box = adjective_box + adjective + " "
    
    adverb = input("Enter adverb: ")
    letter = input("Enter any letter: ")
    body_part = input("Enter any body part: ")
    
    noun_list = noun_box.split()
    plural_noun_list = plural_noun_box.split()
    adjective_list = adjective_box.split()
    
    random.shuffle(noun_list)
    random.shuffle(plural_noun_list)
    random.shuffle(adjective_list)

    print(f"An inspector from the Department of Health and {random.choice(noun_list)} Services paid a surprise visit to our {random.choice(adjective_list)} school cafeteria.")
    print(f"The lunch special, prepared by our {random.choice(adjective_list)} dietician, was spaghetti and {random.choice(noun_list)} {random.choice(plural_noun_list)} with a choice of either a {random.choice(noun_list)} salad or French {random.choice(plural_noun_list)}.")
    print(f"The inspector found the meat-{random.choice(plural_noun_list)} to be overcooked and discovered a live {random.choice(noun_list)} in the fries, causing him to have a {body_part} ache.")
    print(f"In response, he threw up all over his {random.choice(plural_noun_list)}.")
    print(f"In his report, the inspector {adverb} recommended that the school cafeteria serve only nutritious {random.choice(plural_noun_list)} as well as low-calorie {random.choice(plural_noun_list)} and that all of the saturated {random.choice(plural_noun_list)} be eliminated.")
    print("He rated the cafeteria a",letter,"-minus.")
    
    

Madlibs_generator()

    