arr = [23, 1, 43, 12, 11, 9, 8, 25]
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
    return arr
bubble_sort(arr)
print(arr)