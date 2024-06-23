#User function Template for python3

class Solution:
    def bracketNumbers(self, string):

        op_num = 0
        stack = []
        answer = []

        for char in string:
            if char == '(':  
                op_num += 1  
                stack.append(op_num)  
                answer.append(op_num) 
            elif char == ')':  
                if stack:  
                    answer.append(stack.pop())

        return answer



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends