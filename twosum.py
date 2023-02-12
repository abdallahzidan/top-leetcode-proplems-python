import pyconf

def twosum(nums,target):
    # initialize dictionary 
    _map={}
    
    # loop over elements    
    for i,v in enumerate(nums):
        # calculate diff
        diff= target-v
        if diff in _map:
            return [i,_map[diff]]
        else:
            _map[v]=i
    return [0,0]    
        
        

if __name__ == "__main__":
    arr= [2,1,5,3]
    target=6
    a= twosum(arr,target)
    print(a)
    