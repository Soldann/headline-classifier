from csv_reader import read_data
from preprocess import preprocess
from categories import Category
from predict import Predict

predictor = Predict('training.csv',True,True)

data, labels = read_data('Polygon Article Categorization Dataset.csv')

print("Bayes accuracy + precision:",predictor.test_bayes(data,labels))

print("Whitelist accuracy + precision:", predictor.test_whitelist(data,labels))