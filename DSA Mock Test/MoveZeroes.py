def moveZeroes(nums):
    count = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    
    while count < len(nums):
        nums[count] = 0
        count += 1
    
    return nums

print(moveZeroes([0,1,0,3,12])) # Output [0,1,0,3,12]
print(moveZeroes([0])) # Output [0]
print(moveZeroes([1,0,2,0,11,12,0,14,15])) # Output [1, 2, 11, 12, 14, 15, 0, 0, 0]