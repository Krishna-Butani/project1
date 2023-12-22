#Importing the packages
import pandas as pd
import numpy as np
from sklearn. feature_extraction. text import CountVectorizer
from sklearn. model_selection import train_test_split
from sklearn. tree import DecisionTreeClassifier
import nltk
import re
nltk. download('stopwords')
from nltk. corpus import stopwords
stopword = set(stopwords.words('english'))
stemmer = nltk. SnowballStemmer("english")
data = pd. read_csv("data.csv")
#To preview the data
print(data. head())
data["labels"] = data["class"]. map({0: " Hate Speech", 1: "Offensive Speech", 2: "No Hate and Offensive Speech"})
data = data[["tweet", "labels"]]
print(data. head())
def clean(text):
    text = str 