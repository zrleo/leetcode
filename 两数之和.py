# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution(object):
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sum_new(self, nums, target):
        hash_map = dict()
        for i, m in enumerate(nums):
            if hash_map.get(target - m) is not None:
                return [i, hash_map.get(target - m)]
            hash_map[m] = i


print(Solution().two_sum([2, 7, 11, 15], 9))
print(Solution().two_sum_new([2, 7, 11, 15], 17))