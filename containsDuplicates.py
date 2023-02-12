def solution(nums):
    _set=set()
    for i in nums:
        _set.add(i)
    if len(_set)==len(nums):
        return False
    return True  
    
    
if __name__ == "__main__":
    arr= [7,3,10,1,5,4]
    a= solution(arr)
    print(a)
    