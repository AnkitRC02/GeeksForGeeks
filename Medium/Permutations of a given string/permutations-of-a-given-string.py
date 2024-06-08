#User function Template for python3

class Solution:
    def find_permutation(self, S):
        return list(set(["".join(x) for x in list(__import__("itertools").permutations(S))]))
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends