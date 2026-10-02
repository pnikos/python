class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s.split())
        lst.reverse()
        return ' '.join(lst)



s = "the sky is blue"
c = Solution()
print(c.reverseWords(s))