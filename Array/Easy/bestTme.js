function bestTime(prices)
{
    let min_price=Infinity
    let max_profit=0
    for(let i=0;i<prices.length;i++)
    {
        min_price=Math.min(min_price,prices[i])
        max_profit=Math.max(max_profit,prices[i]-min_price)
    }
    return max_profit
}
prices=[7,1,5,3,6,4]
console.log(bestTime(prices))