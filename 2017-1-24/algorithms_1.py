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

'''


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
    jin_wei = 0
    while l1 or l2:
        if l1 and l2:
            l1.val = l2.val + l1.val + jin_wei
            if l1.val > 9:
                jin_wei = 1
                l1.val -= 10
                if l1.next is None and l2.next is None:
                    l1.next = ListNode(jin_wei)
                    return first_l1
            else:
                jin_wei = 0
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
                    l1 = ListNode(l2.val)
            else:
                cur_num = l1.val + jin_wei
                if cur_num > 9:
                    jin_wei = 1
                    l1.val -= 10
                else:
                    jin_wei = 0
            l1 = l1.next
    if jin_wei > 0:
        l1.next = ListNode(jin_wei)
    return first_l1


if __name__ == '__main__':
    demodata1 = ListNode(0)
    # demodata1.next = ListNode(4)
    # demodata1.next.next = ListNode(3)
    demodata2 = ListNode(7)
    demodata2.next = ListNode(3)
    # demodata2.next.next = ListNode(4)
    resultNode = addTwoNumbers(demodata1, demodata2)
    while resultNode:
        print resultNode.val
        resultNode = resultNode.next
    pass
