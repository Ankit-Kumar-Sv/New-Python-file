def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j]>min:
                min = arr[j]
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
    return arr

arr = [12, 9, 45, 89, 3, 32, 23, 0, 11, -9]
selection_sort(arr)
print(arr)
            