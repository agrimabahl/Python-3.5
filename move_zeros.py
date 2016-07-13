
def moveZeroes(nums):
    flag=0
    count=0
    for i in range(len(nums)):
        if nums[i]==0:
            flag=1
            count+=1
        else:
            if flag==1:
                for j in range(i):
                    if nums[j]==0:
                        nums[j]=nums[i]
                        nums[i]=0
    return nums
print(moveZeroes([0,1,0,3,12]))
