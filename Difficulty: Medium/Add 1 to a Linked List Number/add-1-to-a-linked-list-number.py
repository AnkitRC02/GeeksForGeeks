#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverseList(self, head):
        temp, prev = head, None
        
        while temp != None:
            nextt = temp.next
            temp.next = prev
            prev = temp
            temp = nextt
        
        return prev
            
    def addOne(self,head):
        revHead = self.reverseList(head)
        
        temp, carry = revHead, 1
        newHead, curr = None, None
        
        while temp != None:
            currVal = temp.data + carry
            carry = currVal // 10
            if newHead == None:
                newHead = Node(currVal % 10)
                curr = newHead
            else:
                curr.next = Node(currVal % 10)
                curr = curr.next
            
            temp = temp.next
            
        if carry > 0:
            curr.next = Node(carry)
        
        return self.reverseList(newHead)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        first = arr[0]
        for i in arr:
            list1.insert(i)
        n1 = list1.size
        resHead = Solution().addOne(list1.head)

        n2 = 0
        current = resHead
        while current is not None:
            current = current.next
            n2 += 1
        if n2 == 1:
            if n1 > 1:
                print("Return the modified linkedlist")
            if n1 == 1:
                if first < 9:
                    PrintList(resHead)
                    print()
                else:
                    print("Return the modified linkedlist")
        else:
            PrintList(resHead)
            print()

# } Driver Code Ends