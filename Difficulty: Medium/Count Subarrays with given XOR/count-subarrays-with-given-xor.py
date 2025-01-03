class Solution:
    def subarrayXor(self, arr, k):
        # Code here
        prefix_xors = {}
        curr_xor = 0
        count = 0

        for num in arr:
            curr_xor ^= num

            if curr_xor == k:
                count += 1

            required_xor = curr_xor ^ k
            if required_xor in prefix_xors:
                count += prefix_xors[required_xor]

            prefix_xors[curr_xor] = prefix_xors.get(curr_xor, 0) + 1

        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends