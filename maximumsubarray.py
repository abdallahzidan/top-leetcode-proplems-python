def solution(nums):
    _max=nums[0]
    _sum=0
    for i in nums:
     _sum= _sum+i
     if _sum<0:
         _sum=0      
     _max=max(_max,_sum)
    return _max
        
    
if __name__ == "__main__":
    arr= [-2,1,-3,4,-1,2,1,-5,4]
    a= solution(arr)
    print(a)
    