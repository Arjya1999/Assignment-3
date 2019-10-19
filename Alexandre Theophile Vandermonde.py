import numpy as np
n=int(input("Enter the size of the array"))
ar=[]
np.array(ar)
for i in range(n):
    ele=int(input("Enter a number"))
    ar.append(ele)
def func(ar):
    np.array(ar)
    n=len(ar)
    arr=[]
    np.array([[]*n]*n)
    for i in ar:
        arr.append([i**k for k in range(n)])
    print(arr)
print(func(ar))
#print(np.vander(ar,len(ar)))