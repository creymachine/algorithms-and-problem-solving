# Имея массив целых чисел и целую цель, индексы этих двух чисел возвращаются так, что они складываются в цель.

# Можно предположить, что каждый вход будет иметь ровно одно решение, и не использовать один и тот же элемент дважды.

# Вы можете вернуть ответ в любом порядке.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        num_map={}
        for i in range(len(nums)):
            Compliment=target-nums[i]
            if Compliment in num_map:
                return[num_map[Compliment],i]

            num_map[nums[i]]=i

a = Solution()
print(a.twoSum(nums = [3, 3], target=6))
