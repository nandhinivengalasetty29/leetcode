class Solution(object):
    def leftRightDifference(self, nums):
        answer = []
        for i in range(len(nums)):
            left_sum = sum(nums[:i])     
            right_sum = sum(nums[i+1:])  
            answer.append(abs(left_sum - right_sum))
        return answer
        