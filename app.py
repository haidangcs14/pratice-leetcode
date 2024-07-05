numbers = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

ans = Solution()


print(ans.twoSum(numbers, target))