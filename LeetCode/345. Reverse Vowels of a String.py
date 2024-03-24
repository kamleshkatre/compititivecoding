class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index_map = {}
        list1 = []
        for x in range(len(s)):
            list1.append(s[x])
            if s[x] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                index_map[x] = s[x]
        print(index_map)
        list2 = sorted(index_map.keys(), reverse=True)
        list3 = sorted(list2)
        for x in range(len(list3)):
            print(f"this index value will {list2[x]} come to index of {list3[x]}")
            print(f"this index value will {index_map[list2[x]]} come to index of {list1[list3[x]]}")
            list1[list3[x]] = index_map[list2[x]]

        return "".join(list1)


call = Solution()
print(call.reverseVowels("Live on evasions? No, I save no evil."))
