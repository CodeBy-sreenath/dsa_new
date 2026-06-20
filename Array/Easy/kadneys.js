function kadney(nums)
{
    let currentSum=nums[0]
    let max_sum=nums[0]
    for(i=1;i<nums.length;i++)
    {
        currentSum=Math.max(nums[i],nums[i]+currentSum)
        max_sum=Math.max(currentSum,max_sum)
    }
    return max_sum
}