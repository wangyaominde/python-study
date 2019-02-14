import numpy as np
import tensorflow as tf
from sklearn import datasets
from sklearn.cross_validation import train_test_split 

print(tf.__version__)

iris = datasets.load_iris()
train_X, test_X, train_y, test_y = train_test_split(iris.data, iris.target, test_size = 0.2, random_state = 0)