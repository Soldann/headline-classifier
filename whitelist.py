from categories import *
from random import randrange
from preprocess import *

# whitelist: headline, whitelist_dictionary -> category
#   string, (string, string) -> category enum
def whitelist(headline, whitelist_dictionary):
    words = preprocess(headline, True, True)

    for word in words:
        if word in whitelist_dictionary:
            return whitelist_dictionary[word]
    
    rand = randrange(0, NUM_CATEGORIES)
    # print("random: ")
    return Category(rand)