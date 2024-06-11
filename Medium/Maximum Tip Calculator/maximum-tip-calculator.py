
from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        orders = [(arr[i], brr[i], abs(arr[i] - brr[i]), i) for i in range(n)]
        
        orders.sort(key=lambda x: x[2], reverse=True)
        
        total_tip = 0
        countA = 0  
        countB = 0  
        
        for tipA, tipB, _, _ in orders:
            if (tipA >= tipB and countA < x) or countB >= y:
                total_tip += tipA
                countA += 1
            else:
                total_tip += tipB
                countB += 1
        
        return total_tip


        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends