def insertion_sort(arr):
    for i in range(1, len(arr)):
        ref_value = arr[i]
        x = i
        while x>0 and arr[x-1] > ref_value:
            arr[x] = arr[x-1]
            x -= 1 
        else:
            arr[x] = ref_value
    return arr
arr=[16,5,-23,11,-2]
print(insertion_sort(arr))
