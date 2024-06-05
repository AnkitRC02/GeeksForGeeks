#User function Template for python3


#User function Template for python3

# Node class for the Trie data structure
class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]  # List to store children nodes
        self.isWord = False  # Boolean flag to check if current node represents a complete word

# Trie data structure
class Trie:
    def __init__(self):
        self.Tree = TrieNode()  # Creating root node of the Trie

    # Function to insert a word into the Trie
    def insert(self, s):
        cur = self.Tree
        prev = None
        for i in s:
            if cur.children[self.index(i)] is None:  # If character not present in children, create a new node
                cur.children[self.index(i)] = TrieNode()
            prev = cur
            cur = cur.children[self.index(i)]  # Move to the next node
        cur.isWord = True  # Mark the current node as a complete word

    # Function to check if a word is present in the Trie
    def contains(self, s):
        cur = self.Tree
        cur.isWord = True
        prev = None
        for i in s:
            if cur.children[self.index(i)] is None or cur.isWord == False:  # If character not found or the current node does not represent a complete word, return False
                return False
            prev = cur
            cur = cur.children[self.index(i)]  # Move to the next node
        return True  # Return True if the word is present in the Trie

    # Function to get the index of a character
    def index(self, char):
        return ord(char) - ord("a")

class Solution():
    # Function to find the longest string in the array that is present in the Trie
    def longestString(self, arr, n):
        trie = Trie()  # Initialize the Trie
        for s in arr:
            trie.insert(s)  # Insert all strings in the Trie
        ans = ""  # Variable to store the longest string

        # Traverse through all strings in the array
        for s in arr:
            if trie.contains(s):  # If the string is present in the Trie
                if len(s) > len(ans):  # If it is longer than the current longest string
                    ans = s  # Update the longest string
                elif len(s) == len(ans):  # If it has the same length as the current longest string
                    ans = min(ans, s)  # Compare lexicographically and update the longest string
        return ans  # Return the longest string



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends