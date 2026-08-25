def small_large(arr):
    smallest=arr[0]
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    return largest,smallest
print(small_large([1,8,4,0,2]))            