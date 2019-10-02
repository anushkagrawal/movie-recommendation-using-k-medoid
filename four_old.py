# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 00:33:39 2019

@author: ANUSHKA
"""

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
movies = pd.read_csv('ml-latest-small/movies.csv')

# Import the ratings dataset
ratings = pd.read_csv('ml-latest-small/ratings.csv')

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

#returns top 5 movies of all genres
def top_movies(genre,user_user_id):
    
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    Romance2 = ratings4[['title','userId', 'genres','rating']]

    rating_romance = ratings4.genres.str.contains(genre)
    
    Romance2=Romance2[rating_romance]
    userid1=ratings4.userId==user_user_id
    
    #ensures that already watched movies are not recommended
    Romance2=Romance2[~userid1]

    #ensures that average rating is taken into consideration
    t=Romance2.groupby(['title']).mean()
    
    #sorts the movies by avg rating...only top are recommended
    asc_user_rating=t.sort_values(by ='rating',ascending=False )
    print('\n')
    print('Top Rated Movies in', genre)
    top=asc_user_rating.head(5)
    for row in top.index: 
        print(row, end = '\n') 
 
#returns movies watched by centroid and not by user
def unwatched_movies(genre, centroid_userid, user_user_id):
    
    #forms dataframe containing details only of centroid_user_id
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == centroid_userid 
    romance=ratings4[rating_romance & rating_id]
    #print(romance)
    title1=romance["title"]
    title1=pd.DataFrame(title1)

    #forms dataframe containing details only of user_user_id
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == user_user_id
    romance2=ratings4[rating_romance & rating_id]

    #print(romance2)
    title2=romance2["title"]
    title2=pd.DataFrame(title2)

#droping duplicates titles
    c=pd.DataFrame()
    d=pd.DataFrame()
    c=pd.concat([title1, title2]).drop_duplicates(keep=False)
    d = pd.merge(c, title1, how='inner', on=['title'])
    print('recommended movies')
    print(d)       

#returns genre 
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
        
        
#calculates pearson correlation coefficient      
#genre=
def pearson_similarity(centroid_userid, user_user_id, genre):
    
    #forms dataframe containing details only of centroid_user_id
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == centroid_userid
    romance=ratings4[rating_romance & rating_id]
    #print(romance)
    
    #forms dataframe containing details only of user_user_id
    ratings4=pd.read_csv('combined.csv',encoding = "ISO-8859-1")
    rating_romance =  ratings4.genres.str.contains(genre)
    rating_id= ratings4.userId == user_user_id
    romance2=ratings4[rating_romance & rating_id]
   # print(romance2)
    
    romance=pd.DataFrame(romance)
    romance2=pd.DataFrame(romance2)
    #now,we merged the above two dataframes 
    Romance=pd.merge(romance,romance2, on ="movieId")
    Romance=pd.DataFrame(Romance)
#    print('Romance')
#    print(Romance)
    
    #contains ratings given by centroid for particular genre
    list1=Romance.iloc[:,5]  
    #contains ratings given by user for particular genre
    list2=Romance.iloc[:,11]
    #calculates pearson coefficient
    z=np.corrcoef(list1, list2)[0,1]
    if np.isnan(z):
        return 0

    return z
    
#centroids=list of all centroids
#index=cluster no.    
#finds the user_id of centroid        
def find_user_id(centroid, index, user_user_id):
    centroid_userid=-1
    for i in range(len(genre_ratings)):
        if centroid[index][0]==genre_ratings[i][0] and centroid[index][1]==genre_ratings[i][1]:
            centroid_userid=i
            break
        
    print('centroid_userid=',centroid_userid+1)
    
    find_centroid_entry(centroid_userid,user_user_id)        
    
#forms dataframe of the movies watched by centroid                
def find_centroid_entry(centroid_userid,user_user_id):
    centroid_userid+=1

    ratings2 = pd.read_csv('ml-latest-small/combined1.csv', index_col = "userId",encoding = "ISO-8859-1") 
    centroid_data1 = ratings2.loc[[centroid_userid],["movieId","title","genres","rating"]]
#    print('centroid_data1')

    
    ######### finding similarity ###########
    p={}    
#p_romance
    p[0]=pearson_similarity(centroid_userid, user_user_id, "Romance")
#p_scifi
    p[1]=pearson_similarity(centroid_userid, user_user_id, "Sci-Fi")
#p_comedy
    p[2]=pearson_similarity(centroid_userid, user_user_id, "Comedy")
#p_drama
    p[3]=pearson_similarity(centroid_userid, user_user_id, "Drama")
#p_animation
    p[4]=pearson_similarity(centroid_userid, user_user_id, "Animation")
#p_fantasy
    p[5]=pearson_similarity(centroid_userid, user_user_id, "Fantasy")
#p_thriller
    p[6]=pearson_similarity(centroid_userid, user_user_id, "Thriller")


    max=-1
    index=-1

#    for i in range(7):
#        print(p[i])
    
    for i in range(7):
        if p[i]>max: 
            max=p[i]
            index=i
        
    similar_genre=return_genre(index)
    print('\n')
    print('similar genre=')
    print(similar_genre)
    print('\n')
    
    print('max p coeff')
    print(max)
    
    unwatched_movies(similar_genre, centroid_userid, user_user_id)
    print('\n')
    print('TOP RECOMMENDED MOVIES')
    top_movies("Romance", user_user_id)
    top_movies("Sci-Fi", user_user_id)
    top_movies("Comedy", user_user_id)
    top_movies("Drama", user_user_id)
    top_movies("Thriller", user_user_id)
    
    
# Returns the euclidian distance between a and b.
def Distance(a,b):

    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))

# D=data points
# medoids=centroids of clusters
# assigns clusters to all data points
def assignClusters(D, medoids):
	clusters = {}
	for dataPoint in D:
		distances = []
		
		for medoid in medoids:
			distances.append(Distance(dataPoint, medoid))

		
		minIndex = distances.index(min(distances))
  
		clusters.setdefault(minIndex, []).append(dataPoint)
         
	return clusters


# Returns the medoid of the points.
def findClusterMedoid(cluster):
    minDistance = 100
    for point in cluster:
        for comparePoint in cluster:
            if Distance(point, comparePoint) < minDistance:
                minDistance = Distance(point,comparePoint)
                medoid = point
                
    return medoid


#D=data points
#k=no. of clusters
#user_user_id=input userid
#KMedoids assigns clusters to all data points
def KMedoids(D, k, user_user_id):
    
    medoids = D[0:k]
    oldMedoids = [None] * k
 
    centroids = D[0:k]
        
    while medoids != oldMedoids:
        clusters = assignClusters(D, centroids)
        
        for i in range(k):
           
            oldMedoids[i] = medoids[i]
            medoid = findClusterMedoid(clusters[i])
            medoids[i] = medoid
            
            
            newCentroid = findClusterMedoid(clusters[i])
            centroids[i] = newCentroid	
           
    x_value=gr.loc[user_user_id-1][0]
    y_value=gr.loc[user_user_id-1][1]
    min_d=100
    index=0
    
    for i in range(k):
        d=Distance([centroids[i][0],centroids[i][1]],[x_value,y_value])
       # print( i, d)
        if d<min_d:
            min_d=d
            index=i
           
    print('user belongs to cluster:', index)    
    
    find_user_id(centroids, index, user_user_id)
    
    return clusters

def visualize(clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    i = 0
    
    for cluster in clusters.values():
        for point in cluster:
            plt.scatter(point[0], point[1], color = colors[i])
        i +=1 
        
    #label axes
    plt.xlabel('Average Romantic Rating')
    plt.ylabel('Average Sci-fi Rating')
    #save visualization to a .png file
    plt.savefig('kmedoids.png')
    plt.show()
       
    
def main():
    user_user_id=5
    print('user_user_id=')
    print(user_user_id)
    
    myMedoids = KMedoids(points, 3, user_user_id)
    
    
    '''print('***************************************************')
    `
    
    for i in range(2):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('cluster:',i)
        for mm in myMedoids[i]:
            print(mm)
   
    '''
    visualize(myMedoids)
    
    
if __name__ == '__main__':
    main()
    
    

