def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_is_small= True if len(word1) < len(word2) else False
        string1=[]
        if word1_is_small :
            for x in range(len(word1)):
                string1.append(word1[x])
                string1.append(word2[x])
            string1.append(word2[(len(word1)):(len(word2))])
        else:
            for x in range(len(word2)):
                string1.append(word1[x])
                string1.append(word2[x])
            string1.append(word1[(len(word2)):(len(word1))])
        return "".join(string1)

if __name__ == '__main__':
    print(mergeAlternately("abc","pqr"))