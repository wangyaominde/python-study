nums = [3,2,3]
target = 6
'''
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for num1,num2 in enumerate(nums):
        num2 = target - num1
        if num2 in nums:
            y = nums.index(num2)
            x = nums.index(num1)
            if y != x:
                return [y,x]


print(twoSum(nums,target))
'''
def twoSum(nums,target):
    for x in range(len(nums)):
        for y in :
            if nums[x]+nums[y] == target:
                print(x,y)
                x+=1

twoSum(nums,target)
