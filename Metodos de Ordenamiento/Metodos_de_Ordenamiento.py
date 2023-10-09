arr= [12,34,2,6,456,34,12]
#print("Que metodo deseas probrar: \n1.- Metodo Burbuja\n2.-Metodo QuickSort")
case= input("Que metodo deseas probrar: \n1.- Metodo Burbuja\n2.-Metodo QuickSort\n3.-Metodo Insertion Sort\n4.-Metodo Selection Sort\n5.-Metodo Mergesort\n6.-Metodo RadixSort\n")

#METODO BURBUJA
def m_burbuja(arr): 
    n=len(arr)
    for x in range(n):
        for y in range(0,n-x-1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y +1] = arr[y + 1], arr[y]
    print("Lista Ordenada por el METODO BURBUJA:")
    print(arr)

#METODO QUICKSORT
def m_quicksort(arr):
    if len(arr) <=1:
        return arr
    pivote=arr[len(arr)//2]
    izq=[x for x in arr if x < pivote]
    med=[x for x in arr if x == pivote]
    der=[x for x in arr if x > pivote]
    return m_quicksort(izq) + med + m_quicksort(der)
    
#INSERTION SORT
def insertionsort(arr):
    for x in range (1, len(arr)):
        key=arr[x]
        y=x-1
        while y >= 0 and key < arr[y]:
            arr[y+1]=arr[y]
            y-= 1
        arr[y+1]=key
    print(arr)

#SELECTION SORT
def selectionsort(arr):
    for x in range (len(arr)):
        index_med= x
        for y in range (x + 1,len(arr)):
            if arr[y] < arr[index_med]:
                index_med=y
        arr[x], arr[index_med] = arr[index_med], arr[x]
    print(arr)

#MERGESORT
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        izq=arr[:mid]
        der=arr[mid:]

        mergesort(izq)
        mergesort(der)

        i=j=k=0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                arr[k] = izq[i]
                i += 1
            else:
                arr[k] = der[j]
                j += 1
            k += 1

        while i < len(izq):
            arr[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            arr[k] = der[j]
            j += 1
            k += 1
    print(arr)

#RadixSort
def countingsort(arr, exp):
    n=len(arr)
    salida=[0]*n
    cuenta=[0]*10

    for x in range(n):
        index=arr[x]//exp
        cuenta[index % 10]+=1
    
    for x in range(1,10):
        cuenta[x]+=cuenta[x-1]
    x = n-1
    while x >=0:
        index=arr[x]//exp
        salida[cuenta[index % 10]- 1]=arr[x]
        cuenta[index % 10]-=1
        x-=1
    for x in range(n):
        arr[x]=salida[x]

def radixsort(arr):
    numax=max(arr)
    exp=1

    while numax//exp>0:
        countingsort(arr, exp)
        exp*=10
    print(arr)


#Main

if case == "1":
    m_burbuja(arr)
elif case == "2":
    arror=m_quicksort(arr)
    print("Lista Ordenada por el METODO QUICKSORT:")
    print(arror)
elif case == "3":
    print("Lista Ordenada por el METODO INSERTION SORT:")
    insertionsort(arr)
elif case == "4":
    print("Lista Ordenada por el METODO SELECTION SORT:")
    selectionsort(arr)
elif case == "5":
    print("Lista Ordenada por el METODO MERGESORT:")
    mergesort(arr)
elif case == "6":
    print("Lista Ordenada por el METODO RADIXSORT:")
    radixsort(arr)
else:
    print("No existe esa opcion.\nHecho por ESTEBAN BALTAZAR CARBAJAL GARCIA :)")            