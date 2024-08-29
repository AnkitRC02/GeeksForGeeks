from typing import List

class Solution:
    def findMaxDiff(self, arr: List[int]) -> int:
        n = len(arr)
        
        left_smaller = [0] * n
        right_smaller = [0] * n
        
        stack = []
        
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                left_smaller[i] = stack[-1]
            stack.append(arr[i])
        
        stack.clear()
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                right_smaller[i] = stack[-1]
            stack.append(arr[i])
        
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(left_smaller[i] - right_smaller[i]))
        
        return max_diff

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends