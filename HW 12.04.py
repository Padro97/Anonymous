def insertionSort(a):

     

    if (n := len(a)) <= 1:

      return

    for i in range(1, n):

         

        key = a[i]
 

        
        j = i-1

        while j >=0 and key < a[j] :

                a[j+1] = a[j]

                j -= 1

        a[j+1] = key
 
 


a = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
insertionSort(a)

print(a)
