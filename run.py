from preprocess import preprocess
from categories import Category
import bayes
import probabilities

dict1, dict2, default_prob = probabilities.get_probabilities('training.csv',True,True)

print(bayes.bayes(preprocess("Star Wars: Republic Commando review: Who needs the Jedi?",True,True),dict1,dict2,default_prob))
