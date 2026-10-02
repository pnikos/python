import wsgiref.util


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        ws = []
        k1=k2=0
        for i in range(len(word1)+len(word2)):
            if k1 < len(word1):
                ws.append(word1[k1])
                k1+=1
            if k2 < len(word2):
                ws.append(word2[k2])
                k2+=1
        return ''.join(ws)

word1 = "ab"
word2 = "pqrs"
c = Solution()

print(c.mergeAlternately(word1,word2))