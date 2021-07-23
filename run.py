from csv_reader import read_data
from preprocess import preprocess
from categories import Category
from predict import Predict

headline = "Sonic the Hedgehog is in Minecraft now"

predictor = Predict('training.csv',True,True)

data, labels = read_data('Polygon Article Categorization Dataset.csv')

print(predictor.test_bayes(data,labels))

print(predictor.test_whitelist(data,labels))