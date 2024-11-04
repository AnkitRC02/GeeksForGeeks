#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        from collections import defaultdict 

        n = len(arr)
        pair_sum_dict = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                pair_sum_dict[pair_sum].append([i, j])
        
        result = []
        visited_triplets = set()
        
        for i in range(n):
            target = -arr[i]
            
            if target in pair_sum_dict:
                for a, b in pair_sum_dict[target]:
                    if i != a and i != b:
                        triplet = sorted([i, a, b])
                        
                        if triplet[0] < triplet[1] < triplet[2] and tuple(triplet) not in visited_triplets:
                            result.append(triplet)
                            visited_triplets.add(tuple(triplet))
        
        return result

        
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends