# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        split_str = str.split('.')
        res = ""
        
        for i in range(len(split_str) - 1, -1, -1):
            if i == 0:
                res += split_str[i]
            else:
                res += split_str[i] + "."
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends