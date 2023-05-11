# Given an array of integers nums where all integers >= 0 and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.
# Input: 
# [2,7,11,15]
# 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: 
# [3,2,4]
# 6
# Output: 
# [1,2]

#Input: 
# [3,3]
# 6
# Output: 
# [0,1]

def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
