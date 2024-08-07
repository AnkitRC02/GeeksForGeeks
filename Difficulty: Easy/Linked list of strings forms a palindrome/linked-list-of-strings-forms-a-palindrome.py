#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    node = head
    nodes = []
    while node:
        nodes.append(node)
        node = node.next

    left, right = 0, len(nodes) -1
    lp, rp = 0, len(nodes[right].data)-1
    while left <= right:
        while lp < len(nodes[left].data) and rp >= 0:
            if nodes[left].data[lp] != nodes[right].data[rp]:
                return False
            lp += 1
            rp -= 1
        if lp >= len(nodes[left].data):
            left += 1
            lp = 0
        if rp < 0:
            right -= 1
            if right >= 0:
                rp = len(nodes[right].data)-1
    return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        if compute(ll1.head):
            print('true')
        else:
            print('false')

# } Driver Code Ends