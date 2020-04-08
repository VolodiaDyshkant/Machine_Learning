import time
import numpy as np

def random_matrix(n,m):
    a=[[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j]=np.random.randint(1,100+1)
    return a

def print_matrix(a):
    n=len(a)
    m=len(a[0])
    for i in range(n):
        print(a[i])


def multiply_matrix(a,b):
    m = len(a)
    n = len(b)
    q = len(b[0])
    bt = [[0 for i in range(n)] for j in range(q)]
    for i in range(q):
        for j in range(n):
            bt[i][j] = b[j][i];
    c=[[0 for i in range(q)] for j in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * bt[j][k];
    return c


a=random_matrix(500,400)
b=random_matrix(400,600)

ti=time.time();
c1=multiply_matrix(a,b)
print('Run time of my code: ',time.time()-ti)

ti=time.time();
c2=np.dot(a,b)
print('Run time of numpy: ',time.time()-ti)

