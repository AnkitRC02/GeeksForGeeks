#User function Template for python3

def LongestPalindromeSubString(text):
    pairs = [ 0 for _ in range(2*len(text)-1) ]
    
    longest=1
    index=0
    
    box=0
    mirror=0
    
    for i in range(1,len(pairs)):
        left_c = (i-1)//2
        right_c = (i+2)//2
        
        if right_c<box:
            identical = pairs[ mirror - ( i - mirror ) ];
            
            if right_c+identical > box+1:
                identical = box+1-right_c
            
            right_c += identical
            pairs[i] = identical
            left_c -= identical
            
            if right_c<=box or right_c==len(text):
                continue
        
        while left_c>=0 and right_c<len(text) and text[left_c]==text[right_c]:
            left_c -=1
            right_c +=1
            pairs[i] +=1
        
        if pairs[i]>1 and right_c-1>box:
            box = right_c-1
            mirror = i
        
        length = 2*pairs[i]
        if i%2==0:
            length +=1
        
        if length>longest:
            longest=length
            index=(i+1)//2 - length//2
    
    return text[ index : index+longest ]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        text=input().strip()
        print(LongestPalindromeSubString(text))

# } Driver Code Ends