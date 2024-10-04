#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        arr = [head.data]
        temp = head.next
        while temp!=head:
            arr.append(temp.data)
            temp = temp.next
        temp = head
        for element in arr[::-1]:
            temp.data = element
            temp = temp.next
        return head
        
    def deleteNode(self, head, key):
        prev = head
        temp = head.next
        
        tail = head
        while temp != head:
            temp = temp.next
            tail = tail.next
            
        if head.data == key:
            tail.next = head.next
            head = head.next
            return head
            
        temp = head.next
        while temp != head:
            if temp.data == key:
                prev.next = temp.next
                temp = temp.next
                break
            prev = prev.next
            temp = temp.next
        return head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends