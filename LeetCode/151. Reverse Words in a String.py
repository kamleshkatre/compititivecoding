class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

call = Solution()
print(call.reverseWords("  a good   example  "))