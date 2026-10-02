# 392. Is Subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=j=0

        if len(s)==0:
            return True

        while j < len(t):
            if s[i] == t[j]:
                i+=1
                if i==len(s):
                    break
            j+=1


        if i == len(s):
            return True
        else:
            return False

c = Solution()

s=""
t="ahbgdc"
print(c.isSubsequence(s,t))