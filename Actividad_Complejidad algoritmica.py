#Ordenamiento por burbuja

def bubblesort(s):
    n = len(s)                              #O(1)
    for j in range(n):                      #O(n)
        print(s)                            #O(n)
        for i in range(n - 1 - j):          #O(n²)
            if s[i] > s[i+1]:               #O(n²)
                s[i], s[i+1] = s[i+1], s[i] #O(n²)
    return s                                #O(1)

s = [50, 30, 40, 10, 20]  #O(1)
bubblesort(s)             #O(1)
print(s)                   #O(n)

#Nivel de complejidad: O(n²)

#Ordenamiento por selección

def selectionsort1(s):
    aux = []                        #O(1)
    while len(s) > 0:               #O(n)
        menor = s.index(min(s))     #O(n)
        aux.append(s.pop(menor))    #O(n)
    return aux                      #O(1)

s = [50, 30, 40, 10, 20]            #O(1)
r = selectionsort1(s)               #O(1)
print(r)                            #O(n)

# #Nivel de complejidad: O(n)

#Ordenamiento por Seleccion 2

def selectionsort2(s):
    n = len(s)                          #O(1)
    for i in range(n - 1):              #O(n)
        print(s)                        #O(n)
        menor = i                       #O(n)
        for j in range(i+1, n):         #O(n²)
            if s[menor] > s[j]:         #O(n²)
                menor = j               #O(n²)
        s[i], s[menor] = s[menor], s[i] #O(n)
    return s                            #O(1)

s = [50, 30, 40, 10, 20]                #O(1)
r = selectionsort2(s)                   #O(1)
print(r)                                #O(n)

# #Nivel de complejidad: O(n²)

#Ordenanimeto por Insercion

def insertionsort1(s):
    aux = []                        #O(1)
    while len(s) > 0:               #O(n)
        print(aux, s)               #O(n)  
        x = s.pop(0)                #O(n)
        j = len(aux) - 1            #O(n)
        while j>=0 and aux[j] > x:  #O(n²)
            j -= 1                  #O(n²)
        aux.insert(j+1, x)          #O(n)
    return aux                      #O(1)

s = [50, 30, 40, 10, 20]            #O(1)
r = insertionsort1(s)               #O(1)
print(r)                            #O(n)

# #Nivel de complejidad: O(n²)

#Ordenanimeto por Insercion 2

def insertionsort2(s):
    n = len(s)                      #O(1)
    for i in range(1, n):           #O(n)
        print(s)                    #O(n)
        x = s[i]                    #O(n)
        j = i-1                     #O(n)
        while j>=0 and s[j] > x:    #O(n²)
            s[j+1] = s[j]           #O(n²)
            j -= 1                  #O(n²)
        s[j+1] = x                  #O(n)
    return s                        #O(1)

s = [10, 20, 30, 40, 50]            #O(1)
r = insertionsort2(s)               #O(1)
print(r)                            #O(n)

#Nivel de complejidad: O(n²)

#Ordenamiento por fusion

def mergesort1(S):
    n = len(S)                     #O(1)
    if n > 1:                      #O(1)
        print(S)                   #O(1)
        mid = n // 2               #O(1)
        L, R = S[:mid], S[mid:]    #O(1)
        mergesort1(L)              #T(n/2)
        mergesort1(R)              #T(n/2)
        merge1(S, L, R)            #O(1)

        
def merge1(S, L, R):
    k = 0                               #O(1)
    while len(L) > 0 and len(R) > 0:    #O(n)
        if L[0] <= R[0]:                #O(n)
            S[k] = L.pop(0)             #O(n)
        else:                           #O(n)
            S[k] = R.pop(0)             #O(n)
        k += 1                          #O(n)
    while len(L) != 0:                  #O(n)
        S[k] = L.pop(0)                 #O(n)
        k += 1                          #O(n)
    while len(R) != 0:                  #O(n)
        S[k] = R.pop(0)                 #O(n)
        k += 1                          #O(n)

S = [27, 10, 12, 20, 25, 13, 15, 22]    #O(n)
mergesort1(S)                           #O(n)
print(S)                                #O(n)

#Nivel de complejidad: O(nlogn)

#Ordenamiento por fusion 2

def mergesort2(S, low, high):           
    if low < high:                      #O(1)
        print(S)                        #O(n)
        mid = (low + high) // 2         #O(1)
        mergesort2(S, low, mid)         #T(n/2)
        mergesort2(S, mid + 1, high)    #T(n/2)
        merge2(S, low, mid, high)       #O(n)


def merge2 (S, low, mid, high):
    R = []                              #O(1) 
    i, j = low, mid + 1                 #O(1)
    while i <= mid and j <= high:       #O(n)
        if S[i] < S[j]:                 #O(n)
            R.append(S[i]); i += 1      #O(n)
        else:                           #O(n)
            R.append(S[j]); j += 1      #O(n)
    if i > mid:                         #O(n)
        for k in range(j, high + 1):    #O(n)
            R.append(S[j])              #O(n)
    else:                               #O(n)
        for k in range(i, mid + 1):     #O(n)
            R.append(S[i])              #O(n)
    for k in range(len(R)):             #O(n)
        S[low+k] = R[k]                 #O(n)


S = [27, 10, 12, 20, 25, 13, 15, 22]    #O(1) 
mergesort2(S, 0, len(S)-1)              #O(1) 
print(S)                                #O(n)

#Nivel de complejidad: O(nlogn)


#Ordenamiento rapido

def quicksort1(S, low, high):
    if low < high:                              #O(1)
        print(S)                                #O(n)
        pivotpoint = partition1(S, low, high)   #O(n)
        quicksort1(S, low, pivotpoint - 1)      #T(m)
        quicksort1(S, pivotpoint + 1, high)     #T(n-m-1)


def partition1(S, low, high):
    pivot = S[low]                              #O(1)
    left, right = low + 1, high                 #O(1)
    while left < right:                         #O(n)
        print(S)                                #O(n)
        while left <= right and S[left] <= pivot:#O(n²)
            left += 1                            #O(n²)
        while left <= right and S[right] >= pivot:#O(n²)
            right -= 1                            #O(n²)
        if left < right:                          #O(n)
            S[left], S[right] = S[right], S[left] #O(n)
    pivotpoint = right                            #O(1)
    S[low], S[pivotpoint] = S[pivotpoint], S[low] #O(1)
    return pivotpoint                             #O(1)

S = [15, 10, 12, 13, 25, 20, 22]                  #O(1)
quicksort1(S, 0, len(S)-1)                        #O(1)
print(S)                                          #O(n)  

#Nivel de complejidad: O(n²)

#Ordenamiento rapido 2

def quicksort2(S, low, high):
    if low < high:                              #O(1)
        pivotpoint = partition2(S, low, high)   #O(n)
        quicksort2(S, low, pivotpoint - 1)      #T(m)
        quicksort2(S, pivotpoint + 1, high)     #T(n-m-1)


from random import randint

def partition2(S, low, high):                   #O(1)
    rand = randint(low, high)                   #O(1)
    S[low], S[rand] = S[rand], S[low]           #O(1)
    pivot, left, right = S[low], low, high      #O(1)
    print(S, left, right, "pivot = ", pivot)    #O(n)
    while left < right:                         #O(n)
        while left < high and S[left] <= pivot:   left += 1 #O(n²)
        while right > low and pivot <= S[right]: right -= 1 #O(n²)
        if left < right:  S[left], S[right] = S[right], S[left] #O(n)
    S[low], S[right] = S[right], S[low]                         #O(1)
    return right                                                #O(1)

S = [15, 10, 12, 20, 25, 13, 22]                                #O(1)
quicksort2(S, 0, len(S)-1)                                      #O(1)
print(S)                                                        #O(n)

#Nivel de complejidad: O(n²)

# modo python
def quicksort(lista):
    if len(lista) <= 1:                                 #O(1)
        return lista                                    #O(1)
    pivot = lista[len(lista) // 2]                      #O(1)
    left  = [x for x in lista if x <  pivot]            #O(n)
    middle= [x for x in lista if x == pivot]            #O(n)
    right = [x for x in lista if x >  pivot]            #O(n)
    return quicksort(left) + middle + quicksort(right)  #T(len(left)) + T(len(right)) + O(n)

#Nivel de complejidad: O(n log n)