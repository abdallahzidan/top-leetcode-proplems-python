def mostprofit(nums):
    #arr= [7,3,8,1,7,4]
    max_profit=0
    l,r=0,1
    while(r<len(nums)):
         if nums[l]<nums[r]:
             max_profit=max(max_profit,nums[r]-nums[l])
         else:
             l=r
         r=r+1
         
    return max_profit
        

if __name__ == "__main__":
    arr= [7,3,10,1,7,4]
    a= mostprofit(arr)
    print(a)
    