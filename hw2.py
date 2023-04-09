def min_max(a):
    if (n := len(a)) <= 1:
        return a[0], a[0]
    
    min = a[0]
    max = a[0]
    
    for i in range(1, n):
        if a[i] < min:
            min = a[i]
        elif a[i] > max:
            max = a[i]
            
        j = i-1
        key = a[i]
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        
    return min, max

lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
min, max = min_max(lst)
print("Минимальное значение:", min)
print("Максимальное значение:", max)