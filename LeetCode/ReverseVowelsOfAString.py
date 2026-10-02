
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = []
        str=list(s)
        for d in str:
            if d in ['A','E','I','O','U','a','e','i','o','u']:
                vowels.append(d)
        for i in range(len(str)):
            if str[i] in ['A','E','I','O','U','a','e','i','o','u']:
                str[i] = vowels.pop()
        return ''.join(str)




s = "IceCreAm"

c = Solution()
print(c.reverseVowels(s))
