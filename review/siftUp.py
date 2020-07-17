"""
    The reason why I have these function because if we try inOrder Traversal or Postorder Traversal on a Binaray Tree
    we insert the values in an array, will find as follow:
    1- If do in-order then will get an array that:
        A- Array thats sorted in an increasing order
        B- Aarray that we can peform minHeap from left to right
        C- Array that we can peform maxHeap from right to left
        D- We can sift up on that array to see if its minHeap or maxHeap by using:
            ~ left children -> left = (2 * position) + 1
            ~ right children -> ight = (2 * position) + 2

    2- If we peform post-order then will get an array as follow:
        A- Array that a minHeap from left to right
        B- We can peform a binary search tree if we start from to left
"""



# This array is from a binary search tree that a in-order traversal was peformed on.
# We also checked wether the tree is BS by applying the siftUp techinques
lst = [10, 20, 25, 30, 35, 40, 45, 50, 65, 70, 90] 
n = len(lst)
def leftChild(position):
    left = (2 * position) + 1
    return left

def rightChild(position):
    right = (2 * position) + 2
    return right
    
def siftUp():
    n = len(lst)
    i = 0
    left = leftChild(i)
    right = rightChild(i)
    while i < n and left < n and right < n:
        if lst[i] >= lst[left] or lst[i] >= lst[right]:
            return False
        i += 1
        left = leftChild(i)
        right = rightChild(i)
    return True 
siftUp()