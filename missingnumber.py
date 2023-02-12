def solution(nums):
    sum_ = sum(range(min(nums),len(nums)+2))
    other = sum(nums)
    return sum_-other
        
    
if __name__ == "__main__":
    arr= [1,2,3,5,4,7]
    a= solution(arr)
    print(a)
    