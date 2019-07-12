'''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

思路：
遇到左括号，将括号放在栈中，往后读取，如果是右括号，与栈中的前一个元素比较，如果匹配，就pop出来，直到栈为空
'''


class Solution(object):
    def is_valid(self, s):
        a_stack = []
        valid_hash = {')': '(', ']': '[', '}': '{'}
        for alp in s:
            if alp in valid_hash:
                if not a_stack or valid_hash[alp] != a_stack.pop():
                    return False
            else:
                a_stack.append(alp)
        return not a_stack


print(Solution().is_valid('()'))

