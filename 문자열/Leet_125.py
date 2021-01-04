# Valid Palindrome

from collections import deque
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence=list()
        for char in s:
            if char.isalnum():
                sentence.append(char.lower())
                
        return sentence==sentence[::-1]

''' # Using DEQUE
class Solution:
    def isPalindrome(self, s: str) -> bool:
        q=deque()
        for char in s:
            if char.isalnum():
                q.append(char.lower())
                
        while len(q)>1:
            if q.popleft()!=q.pop():
                return False
        return True
'''

'''# Using Regular Expression
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]','',s)

        return s==s[::-1]
'''