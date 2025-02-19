#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        min_heap = []
        for l in arr:
            if l:
                heapq.heappush(min_heap, Node(l))
 
        head = Node(None)
        current = head

        while min_heap:
            tmp = heapq.heappop(min_heap)
            current.next = tmp.data
            current = current.next
            if current.next:
                heapq.heappush(min_heap, Node(current.next))
                
        return head.next


#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends