# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:19:58 2019

@author: ANUSHKA
"""

#A template for the implementation of K-Medoids.
import math #sqrt
import matplotlib.pyplot as plt
import pandas as pd
import helper
import csv
import numpy as np
from csv import reader

centres=0

#Importing Dataset
#dataset = pd.read_csv('ml-latest-small/movies.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')


# Import the ratings dataset
ratings = pd.read_csv('ml-latest-small/ratings.csv')
#combined= pd.merge(movies, ratings.rename(columns={'movieId':'movieId'}), on='movieId',  how='left')
combined = pd.merge(movies, ratings, on='movieId', how='inner')
genre_ratings = helper.get_genre_ratings(ratings, movies, ['Romance', 'Sci-Fi'], ['avg_romance_rating', 'avg_scifi_rating'])
genre_ratings.head()

#avg_romance_rating -- X-axis
X = genre_ratings.iloc[:,0] 
#avg_sci-fi_rating	   -- Y-axis
Y = genre_ratings.iloc[:,1]

gr=pd.DataFrame(genre_ratings)

genre_ratings=np.nan_to_num(genre_ratings)  
#print(X, Y)
#writing gr to the csv file gre2
#gr.to_csv("gre3.csv")

points = []
point = []

with open("gre2.csv", 'r') as data_file:
    read_obj = reader(data_file)
    for row in read_obj:
        #print(row)
        point = [float(row[1]), float(row[2])]
        points.append(point)

def unwatched_movies(genre):
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == 3
    romance=ratings4[rating_romance & rating_id]
    #print(romance)
    title1=romance["title"]
    title1=pd.DataFrame(title1)

    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == 7
    romance2=ratings4[rating_romance & rating_id]
#print(romance2)
    title2=romance2["title"]
    title2=pd.DataFrame(title2)

#droping duplicates titles
    c=pd.DataFrame()
    d=pd.DataFrame()
    c=pd.concat([title1, title2]).drop_duplicates(keep=False)
#d=pd.concat([c, title2]).drop_duplicates(keep=False)
    d = pd.merge(c, title1, how='inner', on=['title'])
    print('recommended movies')
    print(d)       

def return_genre(i):
    if i==0:
        return "Romance"
    if i==1:
        return "Sci-Fi"
    if i==2:
        return "Comedy"
    if i==3:
        return "Drama"
    if i==4:
        return "Animation"
    if i==5:
        return "Fantasy"
    if i==6:
        return "Thriller"
        
def pearson_coefficient(centroid_userid, user_user_id, genre):
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == centroid_userid
    romance=ratings4[rating_romance & rating_id]
    #print(romance)
    
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == user_user_id
    romance2=ratings4[rating_romance & rating_id]
   # print(romance2)
    
    romance=pd.DataFrame(romance)
    romance2=pd.DataFrame(romance2)
    Romance=pd.merge(romance,romance2, on ="movieId")
    Romance=pd.DataFrame(Romance)
    print('Romance')
    print(Romance)
    
    list1=Romance.iloc[:,5]  
    list2=Romance.iloc[:,11]
    z=np.corrcoef(list1, list2)[0,1]
    if np.isnan(z):
        return 0

    return z
        
def find_user_id(centroid, index, user_user_id):
    centroid_userid=-1
    for i in range(len(genre_ratings)):
        if centroid[index][0]==genre_ratings[i][0] and centroid[index][1]==genre_ratings[i][1]:
            centroid_userid=i
            break
    print('centroid_userid=',centroid_userid+1)
    find_centroid_entry(centroid_userid,user_user_id)        
    
                
def find_centroid_entry(centroid_userid,user_user_id):
    centroid_userid+=1
    movie_ids=[]
    ratings=[]
    entry=[]
    centroid_data=[]

    ratings1 = pd.read_csv('ml-latest-small/ratings.csv', index_col ="userId") 
    centroid_data = ratings1.loc[[centroid_userid],["movieId","rating"]]
    print('centroid_data--------------------------------------------')
    print(centroid_data)
    #centroid_data=pd.DataFrame(centroid_data)
   # print(centroid_data[1][1])
    ratings2 = pd.read_csv('ml-latest-small/combined1.csv', index_col = "userId",encoding = "ISO-8859-1") 
    centroid_data1 = ratings2.loc[[centroid_userid],["movieId","title","genres","rating"]]
    print('centroid_data1')
#    print(centroid_data1)
#    centroid_data1=pd.DataFrame(centroid_data1)
    #avg rating of each genre  
# '''ratings2 = pd.read_csv('ml-latest-small/ratings.csv',encoding = "ISO-8859-1") 
#    new = ratings2["userId"].isin([centroid_userid])
#    print('ratings2[new]')
#    print(ratings2[new])
#    
#    
#    movies2 = pd.read_csv('combined.csv',encoding = "ISO-8859-1") 
#    new1 = movies2["userId"].isin([centroid_userid])
#    print('movies2[new1]')
#    movies2_new1=movies2[new1]
#    print(movies2_new1)
#    
#    
#    ratings3 = pd.read_csv('ml-latest-small/ratings.csv',encoding = "ISO-8859-1") 
#    new2 = ratings3["userId"].isin([user_user_id])
#    print('ratings3[new2]')
#    print(ratings3[new2])
#    
#    
#    movies3 = pd.read_csv('combined.csv',encoding = "ISO-8859-1") 
#    new3 = movies3["userId"].isin([user_user_id])
#    print('movies3[new3]')
#    print(movies3[new3])
#    
#    
#    genre_ratings_centroid = helper.get_genre_ratings(ratings2[new], movies2[new1], ['Romance', 'Sci-Fi'], ['avg_romance_rating', 'avg_scifi_rating'])
#    print('genre_ratings_centroid')
#    print(genre_ratings_centroid)
#    
#    genre_ratings_user_user_id = helper.get_genre_ratings(ratings3[new2], movies3[new3], ['Romance', 'Sci-Fi'], ['avg_romance_rating', 'avg_scifi_rating'])
#    print('genre_ratings_user_user_id')
#    print(genre_ratings_user_user_id)'''
    
    
    ######### finding similarity ###########
    p={}    
#p_romance
    p[0]=pearson_similarity("Romance")
#p_scifi
    p[1]=pearson_similarity("Sci-Fi")
#p_comedy
    p[2]=pearson_similarity("Comedy")
#p_drama
    p[3]=pearson_similarity("Drama")
#p_animation
    p[4]=pearson_similarity("Animation")
#p_fantasy
    p[5]=pearson_similarity("Fantasy")
#p_thriller
    p[6]=pearson_similarity("Thriller")


    max=-1
    index=-1

    for i in range(7):
        print(p[i])
    
    for i in range(7):
        if p[i]>max: 
            max=p[i]
            index=i
        
    print(index)
    print(max)

    similar_genre=return_genre(index)
    print(similar_genre)


    print('p coeff')
    print(z)
    unwatched_movies(similar_genre)
#    genre_ratings_centroid_r=movies2_new1["genre"].isin(["Romance"])
#    print('genre_ratings_centroid_r')
#    print(genre_ratings_centroid_r)     


                 
# Accepts two data points a and b.
# Returns the distance between a and b.
# Note that this might be specific to your data.
def Distance(a,b):
    #    x = float(a[0]) - float(b[0])
    #    y = float(a[1]) - float(b[1])
    #    return float(math.sqrt(x*x + y*y))
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))

# Accepts a list of data points D, and a list of centers
# Returns a dictionary of lists called "clusters", such that
# clusters[c] is a list of every data point in D that is closest
#  to center c.
def assignClusters(D, medoids):
	clusters = {}
	for dataPoint in D:
		distances = []
		#compare each data point to all 3 centroids stored in an array distances[]
		for medoid in medoids:
			distances.append(Distance(dataPoint, medoid))

		#find the minimum distance and keep track of its index
		minIndex = distances.index(min(distances))

		#index i of minimum distance = ith cluster in clusters[i]
		clusters.setdefault(minIndex, []).append(dataPoint)
         
              #print('clusters:', clusters) 
	return clusters

# Accepts a list of data points.
# Returns the medoid of the points.
def findClusterMedoid(cluster):
    minDistance = 100
    for point in cluster:
        for comparePoint in cluster:
            if Distance(point, comparePoint) < minDistance:
                minDistance = Distance(point,comparePoint)
                medoid = point
                
    return medoid

# Accepts a list of data points, and a number of clusters.
# Produces a set of lists representing a K-Medoids clustering
#  of D.
def KMedoids(D, k, x, user_user_id):
    #initialize medoids and oldMedoidss to size k
    medoids = D[0:k]
    oldMedoids = [None] * k
 
    #initialize centroids with first k amount of points in D
    centroids = D[0:k]
        
    while medoids != oldMedoids:
        clusters = assignClusters(D, centroids)
        
        for i in range(k):
            #find mean point of each cluster
            #reassign oldMedoids before assigning new means
            oldMedoids[i] = medoids[i]
            medoid = findClusterMedoid(clusters[i])
            medoids[i] = medoid
            
            #readjust data points according to means
            newCentroid = findClusterMedoid(clusters[i])
            centroids[i] = newCentroid	
           
            print('Old medoids: ', oldMedoids)
            print('medoids: ', medoids)
            print('new centroids: ', centroids)
            '''print('clusters[0]:',clusters[0])
            print('----------------------------------------------------------')
            print('clusters[1]:',clusters[1])'''
            
    #centroids=pd.DataFrame(centroids)
    print('centroid[0][0]:', centroids[0][0])
    print('centroid[0][1]:', centroids[0][1])
    print('centroid[1][0]:', centroids[1][0])
    print('centroid[1][1]:', centroids[1][1])
    print('x=', x)
    
    min_d=100
    index=0
    
    for i in range(k):
        d=Distance([centroids[i][0],centroids[i][1]], x)
        print( i, d)
        if d<min_d:
            min_d=d
            index=i
           
    print('user belongs to cluster:', index)    
    #find_centroid_entry(x,[centroids[index][0],centroids[index][1]])
    find_user_id(centroids, index, user_user_id)
    #pearson_coefficient(user_id,centroid)
    return clusters

def visualize(clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    i = 0
    
    for cluster in clusters.values():
        for point in cluster:
            plt.scatter(point[0], point[1], color = colors[i])
        i +=1 
        
    #label axes
    plt.xlabel('Purchase Power')
    plt.ylabel('Cappuccino')
    #save visualization to a .png file
    plt.savefig('kmedoids.png')
    plt.show()
   
    
#def visualize(clusters):
#	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
#	i = 0
#	
#	#Assign different colors to each cluster
#	for cluster in clusters.values():
#		for point in cluster:	
#			plt.scatter(point[0], point[1], color=colors[i])
#		i+=1

def main():
    user_user_id=7
    print(user_user_id)
    x=[2.5,3]
    
    myMedoids = KMedoids(points, 5, x, user_user_id)
    
    '''print('***************************************************')
    
    
    for i in range(2):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('cluster:',i)
        for mm in myMedoids[i]:
            print(mm)
   
    '''
    visualize(myMedoids)
    
    
if __name__ == '__main__':
    main()
    
    

