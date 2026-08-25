def second(arr,target):
    first=arr.index(target)
    for i in range(first+1,len(arr)):
        if arr[i]==target:
            return i
arr=[1,2,3,4,3,5]
target=3
print(second(arr,target))        