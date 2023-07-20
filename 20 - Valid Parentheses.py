"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Node(): 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class Stack(): 
    def __init__(self): 
        self.head = None 
        self.size = 0 

    def push(self, data): 
        if self.head is None: 
            self.head = Node(data)
        else: 
            new_node = Node(data)
            new_node.next = self.head 
            self.head = new_node 
    
    def pop(self): 
        if self.head is None: 
            return None 
        else: 
            output = self.head.data 
            self.head = self.head.next 
            return output 
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for c in s: 
            if c == '(': 
                stack.push(')') 
            elif c == '[': 
                stack.push(']')
            elif c == '{': 
                stack.push('}')
            else: 
                if stack.pop() != c: 
                    return False
                
        if stack.pop() is not None: 
            return False
        else: 
            return True 
    