

nums = [1, 1, 1, 1, 2, 3, 3]


class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            print('nums[%d] is %d' % (i, nums[i]))
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


x = Solution()

x.removeDuplicates(nums)

'''

for i in range(len(nums)-2):
    print('nums[%d] is %d' % (i ,nums[i]) )
    if nums[i] == nums[i-1]:
        del nums[i]
'''

print(nums)
