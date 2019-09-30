# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:26:41 2019

@author: ANUSHKA
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
import helper
import array 

# Import the Movies dataset
movies = pd.read_csv('ml-latest-small/movies.csv')
movies.head()

# Import the ratings dataset
ratings = pd.read_csv('ml-latest-small/ratings.csv')
ratings.head()


print('The dataset contains: ', len(ratings), ' ratings of ', len(movies), ' movies.')

genre_ratings = helper.get_genre_ratings(ratings, movies, ['Romance', 'Sci-Fi','Comedy','Drama','Thriller','Fantasy','Animation','Action','Adventure','Children'], ['avg_romance_rating', 'avg_scifi_rating','avg_Comedy','avg_Drama','avg_Thriller','avg_Fantasy','avg_Animation','avg_Action','avg_Adventure','avg_Children'])
genre_ratings.head()
#self added
gr=pd.DataFrame(genre_ratings)
print(gr)

arr = array.array('i', [1])  
for i in range (0, 223):
    arr.append(1)   
    
for i in range (0, 224):
    arr.append(2)
    
for i in range (0, 223):
    arr.append(3)

gr['customer_segment']=arr

#till here self added

X = gr.iloc[:, 0:10].values
y = gr.iloc[:, 10].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train=np.nan_to_num(X_train)     #self added 
X_train = sc.fit_transform(X_train)
X_test=np.nan_to_num(X_test)         #self added
X_test = sc.transform(X_test)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = None)# initially we had kept in None to know how   
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
''
