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
from csv import reader

centres=0

#Importing Dataset
#dataset = pd.read_csv('ml-latest-small/movies.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')


# Import the ratings dataset
ratings = pd.read_csv('ml-latest-small/ratings.csv')

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

def find_user_id(centroid, index):
    centroid_userid=-1
    for i in range(len(genre_ratings)):
        if centroid[index][0]==genre_ratings[i][0] and centroid[index][1]==genre_ratings[i][1]:
            centroid_userid=i
            break
    print('centroid_userid=',centroid_userid+1)
    find_centroid_entry(centroid_userid)        
    
                
def find_centroid_entry(centroid_userid):
    centroid_userid+=1
    movie_ids=[]
    ratings=[]
    entry=[]
    centroid_data=[]
    

#     with open('ml-latest-small/ratings.csv', 'r',encoding="utf8") as csvfile:
#        reader = csv.reader(csvfile)
#        for row in reader:
#            #print(row[0])
#            x=row[0]
#            if (centroid_userid == x):
#                print('hi')
#                movie_ids.append(row[1])
#                ratings.append(row[2])
#                print(row)
                
    with open("ml-latest-small/ratings.csv", 'r') as data_file:
        read_obj = reader(data_file)
        for row in read_obj:
            if(row[0] in centroid_userid ):
                print(row)
                entry = [row[1], row[2]]
                centroid_data.append(entry)
                 
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
def KMedoids(D, k, x):
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
    find_user_id(centroids, index)
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
    #user_id=input("enter udser_id:")
    #print(user_id)
    x=[2.5,3]
    
    myMedoids = KMedoids(points, 2, x)
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
    
    

