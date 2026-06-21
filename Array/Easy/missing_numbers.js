function missingNumber(nums,n)
{
    let set=new Set(nums)
    let result=[]
    for(let i=1;i<=n;i++)
    {
        if(!set.has(i))
        {
            result.push(i)
        }
    }
    return result
}
nums = [1,2,3,4,7,8,9]
n = 9
console.log(missingNumber(nums,n))