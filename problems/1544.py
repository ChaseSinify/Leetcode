"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stacky = []
        for c in s:
            if not stacky: stacky.append(c)
            elif stacky[-1].islower() and stacky[-1].upper() == c: stacky.pop()
            elif stacky[-1].isupper() and stacky[-1].lower() == c: stacky.pop()
            else: stacky.append(c)
        return ''.join(stacky)