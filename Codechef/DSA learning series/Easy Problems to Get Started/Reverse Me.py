# You are given a list of N integers and you need to reverse it and print the reversed list in a new line.
#
# Input:
# First-line will contain the number N.
# Second line will contain N space-separated integers.
# Output:
# Print the reversed list in a single line.
#
# Constraints
# 1≤N,Ai≤105
# Sample Input 1:
# 4
# 1 3 2 4
# Sample Output 1:
# 4 2 3 1
# Sample Input 2:
# 2
# 9 8
# Sample Output 2:
# 8 9
# EXPLANATION:
# In the first example, the reverse of the [1,3,2,4] is [4,2,3,1].
# In the second example, the reverse of [9,8] is [8,9].
n=int(input())
#strip for get the all extra whitspaces get clean
str1=[str(i) for i in input().strip().split()]
str1=str1[-1::-1]
print(" ".join(str1))
