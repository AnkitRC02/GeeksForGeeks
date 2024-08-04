#User function Template for python3

class Solution:
    def maximumMeetings(self, n, start, end):
        meetings = sorted(zip(end, start))
        last_end_time = meetings[0][0]
        count = 1
        for i in range(1, n):
            if meetings[i][1] > last_end_time:
                count += 1
                last_end_time = meetings[i][0]
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends