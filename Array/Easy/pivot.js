function pivot(nums)
{
    let total=nums.reduce((sum,num)=>sum+num,0)
    let left_sum=0
    for(let i=0;i<nums.length;i++)
    {
        let right_sum=total-left_sum-nums[i]
        if(left_sum==right_sum)
        {
            return i
        }
        left_sum+=nums[i]
    }
    return -1
}
