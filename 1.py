
def twoSum(nums:list, target):
    mp={}
    ind=0
    for i in nums:
        if target - i in mp:
            print(mp[target-i], ind)
        mp[i]=ind
        ind+=1
            
a =[2,7,11,15]
twoSum(a,9)
