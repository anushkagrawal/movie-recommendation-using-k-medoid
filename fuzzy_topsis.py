import math

def dist_calc(a,b):
    t=(pow( (a[2]-b[2]) , 2 )) + (pow( (a[1]-b[1]) , 2 )) + (pow( (a[0]-b[0]) , 2))
    #print(t)
    #print(t/3)
    return(math.sqrt(t/3))
    #m=math.sqrt( (pow( (a[2]-b[2]) , 2 )) + (pow( (a[1]-b[1]) , 2))+ (pow( (a[0]-b[0]) , 2)) /3)
    #return m
    

def find_max_a(cm,j):
    max_a=cm[0][j][0]
    for i in range (1,len(cm)):
        if cm[i][j][0] > max_a:
            max_a=cm[i][j][2]
    return max_a
def find_max_b(cm,j):
    max_b=cm[0][j][1]
    for i in range (1,len(cm)):
        if cm[i][j][1] > max_b:
            max_b=cm[i][j][1]
    return max_b
def find_max_c(cm,j):
    max_c=cm[0][j][2]
    for i in range (1,len(cm)):
        if cm[i][j][2] > max_c:
            max_c=cm[i][j][2]
    return max_c       
def find_min_a(cm,j):
    min_a=cm[0][j][0]
    for i in range (1,len(cm)):
        if cm[i][j][0] < min_a:
            min_a=cm[i][j][0]
    return min_a 
def find_min_b(cm,j):
    min_b=cm[0][j][1]
    for i in range (1,len(cm)):
        if cm[i][j][a] < min_b:
            min_b=cm[i][j][1]
    return min_b
def find_min_c(cm,j):
    min_c=cm[0][j][2]
    for i in range (1,len(cm)):
        if cm[i][j][0] < min_c:
            min_c=cm[i][j][2]
    return min_c    
dm1=[]
dm1.append([[3,5,7],[7,9,9],[5,7,9]])
dm1.append([[5,7,9],[7,9,9],[3,5,7]])
dm1.append([[7,9,9],[3,5,7],[1,3,5]])
dm1.append([[1,3,5],[3,5,7],[1,1,3]])

dm2=[]
dm2.append([[5,7,9],[7,9,9],[5,7,9]])
dm2.append([[5,7,9],[5,7,9],[3,5,7]])
dm2.append([[7,9,9],[3,5,7],[1,1,3]])
dm2.append([[1,3,5],[3,5,7],[1,1,3]])

dm3=[]
dm3.append([[3,5,7],[5,7,9],[5,7,9]])
dm3.append([[5,7,9],[3,5,7],[3,5,7]])
dm3.append([[5,7,9],[3,5,7],[1,3,5]])
dm3.append([[1,1,3],[1,3,5],[1,1,3]])


#combined decision matrix
cm=[]
#t=[]
def return_append(i):
    s=[]
    for j in range(3):
        s.append([  min(dm1[i][j][0],dm2[i][j][0],dm3[i][j][0]) , (dm1[i][j][1]+dm2[i][j][1]+dm3[i][j][1])/3 , max(dm1[i][j][2],dm2[i][j][2],dm3[i][j][2])  ])
    #print(s)    
    return s    

cm=[] 
    
for i in range (len(dm1)):
    cm.append(return_append(i))

    
#printing combined decision matrix  
print('combined decision matrix : ')    
print(cm)

#weightage to be converted into fuzzy numbers

wt=[]
wt.append([5,7,9])
wt.append([7,9,9])
wt.append([3,5,7])

#normalized fuzzy decision  matrix
#max value dersired ==> benefit criteria
#min value desired ==>cost criteria

#c is for benefit criteria
c=[]
for j in range (2):
    c.append(find_max_c(cm,j))
    #print(c[j])
#print(c)    
    
    
#a is for cost criteria
a=[]
#for j in range (2):
a.append(find_min_a(cm,2))
#print(a)      
          
#normalised fuzzy matrix

for i in range(len(cm)):
    for j in range(2):
        for t in range(3):
            cm[i][j][t]=cm[i][j][t]/c[j]
            
            
j=2

for i in range (len(cm)):
    cm[i][j]=list(reversed(cm[i][j]))
    for t in  range(3):
        cm[i][j][t]=a[0]/(cm[i][j][t])
   
print('normalised fuzzy matrix :')      
print(cm)            
            
        
#weighted normalised decision matrix
for i in range(len(cm)):
    for j in range(3):
        for t in range(3):
            cm[i][j][t]=cm[i][j][t]*wt[j][t]    
            
    
          
print('weighted normalised decision matrix : ')       
print(cm) 
       
def exists(a, i):
    if (a in i): 
        return True
    else:
        return False

def count_t_a(cm,j,t):
    count=0
    for i in range (len(cm)):
        if cm[i][j][0] == t:
            count=count+1
    return count

def find_row_for_a(cm,j,t):
    for i in range(len(cm)):
        if cm[i][j][0] ==t:
            return i
        
def find_rows_for_a(cm,j,t):
    i=[]
    for a in range(len(cm)):
        if cm[a][j][0] == t:
            i.append(a)
    return i 
    
def count_t_b(cm,j,t):
    count=0
    for i in range (len(cm)):
        if cm[i][j][1] == t:
            count=count+1
    return count

def find_row_for_b(cm,j,t):
    for i in range(len(cm)):
        if cm[i][j][1] ==t:
            return i
        
def find_rows_for_b(cm,j,t):
    i=[]
    for a in range(len(cm)):
        if cm[a][j][1] == t:
            i.append(a)
    return i    

def count_t_c(cm,j,t):
    count=0
    for i in range (len(cm)):
        if cm[i][j][2] == t:
            count=count+1
    return count

def find_row_for_c(cm,j,t):
    for i in range(len(cm)):
        if cm[i][j][2] ==t:
            return i
        
def find_rows_for_c(cm,j,t):
    i=[]
    for a in range(len(cm)):
        if cm[a][j][2] == t:
            i.append(a)
    return i

def find_max_b_in_rows(cm,j,t,i):
    max=-125368566
    for a in range (len(cm)):
        if cm[a][j][1] > max and exists(a,i):
            max=cm[a][j][1]
    return max        
            
def find_max_a_in_rows(cm,j,t,i):
    max=-125368566
    for a in range (len(cm)):
        if cm[a][j][0] > max and exists(a,i):
            max=cm[a][j][0]
    return max    


def find_min_b_in_rows(cm,j,t,i):
    min=125368566
    for a in range (len(cm)):
        if cm[a][j][1] < min and exists(a,i):
            min=cm[a][j][1]
    return min        
            
def find_min_c_in_rows(cm,j,t,i):
    min=125368566
    for a in range (len(cm)):
        if cm[a][j][2] < min and exists(a,i):
            min=cm[a][j][2]
    return min        
        
        
        

#fpis and fnis
a_star=[]

for j in range (3):
    t=find_max_c(cm,j)
    count=count_t_c(cm,j,t)
    if count == 1:
        i=find_row_for_c(cm,j,t)
        a_star.append(cm[i][j])
    else:
        i=[]
        i=find_rows_for_c(cm,j,t)
        t=find_max_b_in_rows(cm,j,t,i)
        count=count_t_b(cm,j,t)
        if count == 1:
            i=find_row_for_b(cm,j,t)
            a_star.append(cm[i][j])
        else:
             i=[]
             i=find_rows_for_a(cm,j,t)
             t=find_max_a_in_rows(cm,j,t,i)
             #count=count_t(cm,j,t)
             i=find_row_for_a(cm,j,t)
             a_star.append(cm[i][j])
            
            
print('a star : ')        
print(a_star)

a_minus=[]

for j in range (3):
    t=find_min_a(cm,j)
    count=count_t_a(cm,j,t)
    if count == 1:
        i=find_row_for_a(cm,j,t)
        a_minus.append(cm[i][j])
    else:
        i=[]
        i=find_rows_for_a(cm,j,t)
        t=find_min_b_in_rows(cm,j,t,i)
        count=count_t_b(cm,j,t)
        if count == 1:
            i=find_row_for_b(cm,j,t)
            a_minus.append(cm[i][j])
        else:
             i=[]
             i=find_rows_for_c(cm,j,t)
             t=find_min_c_in_rows(cm,j,t,i)
             #count=count_t(cm,j,t)
             i=find_row_for_c(cm,j,t)
             a_minus.append(cm[i][j])
            
            
print('a minus : ')        
print(a_minus)

dist_from_a_star=[]

def return_dist_a_star(j):
    dist_from_a_star=[]
    for i in range(len(cm)):
        dist_from_a_star.append(dist_calc(cm[i][j],a_star[j]))
    return dist_from_a_star    
        
        
        
for j in range(3):
    dist_from_a_star.append(return_dist_a_star(j))
        
        
print('dist_from_a_star :')
print(dist_from_a_star)

dist_from_a_minus=[]

def return_dist_a_minus(j):
    dist_from_a_minus=[]
    for i in range(len(cm)):
        dist_from_a_minus.append(dist_calc(cm[i][j],a_minus[j]))
    return dist_from_a_minus    
        
        
        
for j in range(3):
    dist_from_a_minus.append(return_dist_a_minus(j))
        
        
print('dist_from_a_minus :')
print(dist_from_a_minus)


di_star=[]

for j in range(4):
    sum=0
    for i in range(len(dist_from_a_star)):
        sum=sum+dist_from_a_star[i][j]
    di_star.append(sum)

print('di_star')
print(di_star)    
 

di_minus=[]

for j in range(4):
    sum=0
    for i in range(len(dist_from_a_minus)):
        sum=sum+dist_from_a_minus[i][j]
    di_minus.append(sum)

print('di_minus')
print(di_minus) 

#closeness coffecient

cc=[]

for i in range(len(di_minus)):
    cc.append(di_minus[i]/(di_minus[i]+di_star[i]))
    
print('closeness coefficient : ')
print(cc)    

#ranking the alternatives
rank_1=[]
rank=[]

for i in range(len(cc)):
    rank_1.append([cc[i],i])
    
rank_1.sort(reverse=True) 

for i in range(len(rank_1)):
    rank.append(rank_1[i][1])



print('rank')
print(rank)


