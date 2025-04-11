## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nextNumber(head):
    # Implement Your Code here
    current = head
    length =0
    #calculate the length
    while current and current.next:
        length += 1
        # print (current.data)
        current = current.next
    count = length
    if current.data < 9:
        current.data +=1
    return head

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)
# print(head)