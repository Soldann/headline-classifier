from categories import *
from random import randrange


# whitelist: headline, whitelist_dictionary -> category
#   string, (string, string) -> category enum

# need to replace
def preprocess(headline):
    return ["apple", "walk", "take", "python"]

def whitelist(headline, whitelist_dictionary):
    words = preprocess(headline)

    for word in words:
        if word in whitelist_dictionary:
            return whitelist_dictionary[word]
    
    rand = randrange(0, NUM_CATEGORIES)
    # print("random: ")
    return Category(rand)