# Problem statement
# Given a Singly Linked List of integers, delete all the alternate nodes in the list.
#
# Example:
# List: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> null
# Alternate nodes will be:  20, 40, and 60.
#
# Hence after deleting, the list will be:
# Output: 10 -> 30 -> 50 -> null
# Note :
# The head of the list will remain the same. Don't need to print or return anything.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 1 2 3 4 5 -1
# Sample Output 1:
# 1 3 5
# Explanation of Sample Input 1:
# 2, 4 are alternate nodes so we need to delete them
# Sample Input 2:
# 10 20 30 40 50 60 70 -1
# Sample Output 2:
# 10 30 50 70
# '''
#     Following is the node structure
#
# class Node :
#     def __init__(self, data) :
#         self.data = data
#         self.next = None
#
# '''
#
#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(229)
node2= Node(286)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)
# 229 286 271 229 155 170 105 150 167 225 -1
head = node1
node1.next= node2
node2.next= node3
node3.next= node4
node4.next=node5
node5.next = node6
#
# while head.next != None:
#     print(head.data )
#     head=head.next

def deletealternatenodes(head):
    head1= head
    if head == None:
        return -1
    while head != None:
        ptr1 = head.next
        head.next = ptr1.next
        head= head.next
    return head1

head2 = deletealternatenodes(node1)
while head2 != None:
    print(head2.data )
    head2=head2.next
