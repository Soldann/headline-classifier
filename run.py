from preprocess import preprocess
from categories import Category
from predict import Predict

headline = "Sonic the Hedgehog is in Minecraft now"

predictor = Predict('training.csv',False,True)

print(predictor.bayes(headline))