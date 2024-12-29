
class Solution:
    def intersectionWithDuplicates(self, a, b):
        a.sort()
        b.sort()

        n1=len(a)
        n2=len(b)

        i=0
        j=0
        ans=[]

        while (i<n1 and j<n2):
            if a[i]==b[j]:
                ans.append(a[i])
                i+=1
                j+=1
            
            elif a[i]>b[j]:
                j+=1
            
            else:
                i+=1

            while (i<n1 and ans and a[i]==ans[-1]):
                i+=1
            while (j<n2 and ans and b[j]==ans[-1]):
                j+=1
        
        return ans



#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.
t = int(input().strip())
while t > 0:
    t -= 1
    # Read first array
    a = list(map(int, input().strip().split()))

    # Read second array
    b = list(map(int, input().strip().split()))

    #input()  # to consume the empty line

    # ADD Solution initialization
    sln = Solution()

    # Assuming numberofElementsInIntersection function is defined in Solution
    res = sln.intersectionWithDuplicates(a, b)

    # Sort the result
    res.sort()

    # Print the result
    if not res:
        print("[]")
    else:
        print(" ".join(map(str, res)))

    print("~")

# } Driver Code Ends