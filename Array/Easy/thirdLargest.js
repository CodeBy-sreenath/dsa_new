function thirdLargest(nums)
{
    nums=[...new Set(nums)]
    if(nums.length>=3)
    {
        return nums[2]

    }
    return nums[0]

}
console.log(thirdLargest([2,2,3,1]))