from preprocess import preprocess
from categories import Category
import bayes
import probabilities
import whitelist

dict1, dict2, default_prob = probabilities.get_probabilities('training.csv',True,True)

headline = "Sonic the Hedgehog is in Minecraft now"

print(bayes.bayes(preprocess(headline,True,True),dict1,dict2,default_prob))

whitelist_dict = probabilities.create_whitelist_dictionary(dict1)

print(whitelist.whitelist(headline,whitelist_dict))

print(whitelist_dict)