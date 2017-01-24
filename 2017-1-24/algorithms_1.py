# coding:utf-8

'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
给定一个数组和一个目标，返回两数相加可得目标的数组。(索引)

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def twoSum(nums, target):
    cur_pos = 0  # 从第一个开始
    for i1, x in enumerate(nums[cur_pos:]):
        for i2, y in enumerate(nums[cur_pos + 1:]):
            if x + y == target:
                return [i1, i1 + i2 + 1]
        cur_pos = cur_pos + 1
    return None


'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''

def addTwoNumbers2(l1, l2):
    cur_pos = 0



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_l1 = l1
        jin_wei = 0
        while l1 or l2:
            if l1 and l2:
                l1.val = l2.val + l1.val + jin_wei
                if l1.val > 9:
                    jin_wei = 1
                    l1.val = 10 - l1.val
                else:
                    jin_wei = 0
                l1 = l1.next
                l2 = l2.next
            else:
                if l1 is None:
                    cur_num = l2.val + jin_wei
                    if cur_num > 9:
                        jin_wei = 1
                        l1 = ListNode(10 - cur_num)
                    else:
                        jin_wei = 0
                        l1 = ListNode(l2.val)
                else:
                    cur_num = l1.val + jin_wei
                    if cur_num > 9:
                        jin_wei = 1
                        l1.val = 10 - l1.val
                    else:
                        jin_wei = 0
                l1 = l1.next

        if jin_wei > 0:
            l1.next = ListNode(jin_wei)
        return first_l1


def addTwoNumbers(l1, l2):
    first_l1 = l1
    last_l1 = l1
    jin_wei = 0
    while l1 or l2:
        if l1 and l2:
            l1.val = l2.val + l1.val + jin_wei
            if l1.val > 9:
                jin_wei = 1
                l1.val -= 10
                if (l1.next is None) and (l2.next is None):
                    last_l1 = l1
                    l1.next = ListNode(jin_wei)
                    return first_l1
            else:
                jin_wei = 0
            last_l1 = l1
            l1 = l1.next
            l2 = l2.next
        else:
            if l1 is None:
                cur_num = l2.val + jin_wei
                if cur_num > 9:
                    jin_wei = 1
                    l1 = ListNode(cur_num - 10)
                else:
                    jin_wei = 0
                    l1 = ListNode(cur_num)
                last_l1.next = l1
                l2 = l2.next
            else:
                cur_num = l1.val + jin_wei
                if cur_num > 9:
                    jin_wei = 1
                    l1.val = cur_num -10
                else:
                    jin_wei = 0
                    l1.val = cur_num
            last_l1 = l1
            l1 = l1.next
    if jin_wei > 0:
        last_l1.next = ListNode(jin_wei)
    return first_l1

'''

[8,6]
[6,4,8]
'''

'''

3. Longest Substring Without Repeating Character

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring
, "pwke" is a subsequence and not a substring.

'''
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    long_sub = []
    last_result = 0
    for i in s:
        if not i in long_sub:
            long_sub.append(i)
        else:
            if len(long_sub) > last_result:
                last_result = len(long_sub)
            long_sub = long_sub[long_sub.index(i)+1:]
            long_sub.append(i)
    return last_result if last_result > len(long_sub) else len(long_sub)

if __name__ == '__main__':
    print lengthOfLongestSubstring('asdqweasd')
    pass