#User function Template for python3
class Solution:
    def findSplit(self, arr):
        total_sum = sum(arr)
        
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        current_sum = 0
        first_split = -1
        second_split = -1
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            if current_sum == target_sum and first_split == -1:
                first_split = i
            
            elif current_sum == 2 * target_sum and first_split != -1:
                second_split = i
                break
        
        if first_split != -1 and second_split != -1:
            return [first_split, second_split]
        
        return [-1, -1]  


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")
        print("~")

# } Driver Code Ends