#User function Template for python3
class Solution:
    def constructLowerArray(self, arr):
        def merge_sort(indices):
            if len(indices) <= 1:
                return indices
            mid = len(indices) // 2
            left_indices = merge_sort(indices[:mid])
            right_indices = merge_sort(indices[mid:])
            return merge(left_indices, right_indices)

        def merge(left_indices, right_indices):
            sorted_indices = []
            i = j = 0
            while i < len(left_indices) and j < len(right_indices):
                if arr[left_indices[i]] <= arr[right_indices[j]]:
                    sorted_indices.append(left_indices[i])
                    counts[left_indices[i]] += j
                    i += 1
                else:
                    sorted_indices.append(right_indices[j])
                    j += 1
            while i < len(left_indices):
                sorted_indices.append(left_indices[i])
                counts[left_indices[i]] += j
                i += 1
            while j < len(right_indices):
                sorted_indices.append(right_indices[j])
                j += 1
            return sorted_indices

        n = len(arr)
        counts = [0] * n
        indices = list(range(n))
        merge_sort(indices)
        return counts


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends