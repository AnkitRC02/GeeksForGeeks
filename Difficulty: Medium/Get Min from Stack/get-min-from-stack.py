class Solution:

    def __init__(self):
        self.s=[]
        self.minEle=None
        
    def push(self,x):
        self.minEle = min(x, self.minEle) if self.s else x
        self.s.append(x)

    def pop(self):
        topEle = self.s.pop() if self.s else -1
        if topEle == self.minEle:
            self.minEle = min(self.s) if self.s else None
        return topEle

    def peek(self):
        return self.s[-1] if self.s else -1

    def getMin(self):
        return self.minEle if self.s else -1



#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends