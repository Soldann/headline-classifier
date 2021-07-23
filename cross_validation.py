import math
from predict import *

def cross_validation(folds, labels, value_list):
    """
    Determines the best threshold probability value for the whitelist algorithm.

    Returns 4 lists: training and validation accuracy, training and validation precision

    :param folds: folds for cross validation
    :type folds: List[List[List[Any]]]
    :param value_list: a list of parameter values
    :type value_list: List[float]
    :return: training accuracy, validation accuracy, training precision, validation precision lists
    :rtype: List[float], List[float], List[float], List[float]
    """
    fold_count = len(folds)
    value_count = len(value_list)

    # initialize list with all zeros
    training_accuracy = [0] * value_count
    validation_accuracy = [0] * value_count
    training_precision = [0] * value_count
    validation_precision = [0] * value_count
    

    for i in range(fold_count):
        # set validation set for each iteration
        validation_set = folds[i]
        training_set = []

        # create training set for iteration
        for j in range(fold_count):
            if i == j:
                continue
            training_set.extend(folds[j])

        # get accuracy and precision for each parameter value k
        for k in range(value_count):
            predictor = Predict(training_set, True, True, k)
            train_acc, train_prec = predictor.test_whitelist(training_set, labels)
            valid_acc, valid_prec = predictor.test_whitelist(validation_set, labels)

            training_accuracy[k] += train_acc
            validation_accuracy[k] += valid_acc
            training_precision[k] += train_prec
            validation_precision[k] += valid_prec
        
    # divide by fold_count to get average accuracy and precision values
    for i in range(len(training_accuracy)):
        training_accuracy[i] = training_accuracy[i] / fold_count
        validation_accuracy[i] = validation_accuracy[i] / fold_count
        training_precision[i] = training_precision[i] / fold_count
        validation_precision[i] = validation_precision[i] / fold_count
    
    return training_accuracy, validation_accuracy, training_precision, validation_precision
