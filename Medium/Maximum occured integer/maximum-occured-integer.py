#User function Template for python3

class Solution:
    def maxOccured(self, n, l, r, maxx):
        freq = [0] * (maxx + 2)
        
        for i in range(n):
            freq[l[i]] += 1
            if r[i] + 1 <= maxx:
                freq[r[i] + 1] -= 1
        
        max_occurrence = freq[0]
        result = 0
        
        for i in range(1, maxx + 1):
            freq[i] += freq[i - 1]
            if freq[i] > max_occurrence:
                max_occurrence = freq[i]
                result = i
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends