def most_freq(nums):
    max_count=0
    new=[]
    for i in nums:
        count=0
        if i in new:
            count+=1
        if count>max_count:
            max_count=count
        new.append(i)
    for i in new:
        if new.count(i)>max_count:
            return i
nums=[1,2,3,4,5,2]                    
print(most_freq(nums))
