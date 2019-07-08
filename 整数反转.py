# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# # #
# # # 示例 1:
# # #
# # # 输入: 123
# # # 输出: 321
# # #  示例 2:
# # #
# # # 输入: -123
# # # 输出: -321
# # # 示例 3:
# # #
# # # 输入: 120
# # # 输出: 21
# # #
# # # 来源：力扣（LeetCode）
# # # 链接：https://leetcode-cn.com/problems/reverse-integer
# # # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def reverse_num(self, x):
        result = 0
        if x == 0:
            return x
        num_list = list(str(x))
        if x < 0:
            num_list.pop(0)
            num_list.reverse()
            result = int('-' + ''.join(num_list))
        elif x > 0:
            num_list.reverse()
            result = int(''.join(num_list))
        if result >= 2**31-1 or result <= -2**31:
            return 0
        return result


print(Solution().reverse_num(1563847412))
