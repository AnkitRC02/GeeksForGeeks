#Initial Template for Python 3

#Initial Template for Python 3
class Solution:
    #Function to find the length of longest subsequence of given array.
    def ZigZagMaxLength(self, nums):
        
        # Code here
        #if length of nums is less than 2, return the length of nums.
        if len(nums) < 2:
            return len(nums)
        #initialize up and down variables to 1.
        up = 1
        down = 1
        #iterating over the array starting from the second element.
        for i in range(1, len(nums)):
            #checking if current element is greater than the previous element.
            #if yes, update up variable as down+1.
            if nums[i] > nums[i - 1]:
                up = down + 1
            #checking if current element is less than the previous element.
            #if yes, update down variable as up+1.
            elif nums[i] < nums[i - 1]:
                down = up + 1
        #returning the maximum of up and down, which is the length of the longest zigzag subsequence.
        return max(up, down)



		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.ZigZagMaxLength(A))
# } Driver Code Ends