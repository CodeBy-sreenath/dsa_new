function missingNumber(nums)
{
   let  n=nums.length
    let expectedSum=n*(n+1)/2
    let currentSum=nums.reduce((sum,num)=>sum+num,0)
    return expectedSum-currentSum
}
console.log(missingNumber([3,0,1]))