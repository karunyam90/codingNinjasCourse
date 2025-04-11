# Problem statement
# For a given queue containing all integer data, reverse the first K elements.
#
# You have been required to make the desired change in the input queue itself.
#
# Example:
# alt txt
#
# For the above input queue, if K = 4 then after reversing the first 4 elements, the queue will be updated as:
# alt txt
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^6
# 1 <= K <= N
# -2^31 <= data <= 2^31 - 1
#
#  Time Limit: 1sec
# Sample Input 1:
# 5 3
# 1 2 3 4 5
# Sample Output 1:
# 3 2 1 4 5
# Sample Input 2:
# 7 7
# 3 4 2 5 6 7 8
# Sample Output 2:
# 8 7 6 5 2 4 3
from sys import stdin, setrecursionlimit
import queue
def reverse_k_elements(q, k):
    if k == 0:
        return
    # Remove the front element
    temp = q.get()

    # Recurse for remaining K - 1 elements
    reverse_k_elements(q, k - 1)

    # Put current element at the end after recursion unfolds
    q.put(temp)

def reverseFirstKQueue(q, k):
    n = q.qsize()

    if k <= 0 or k > n:
        return q

    # Step 1: Reverse first K elements
    reverse_k_elements(q, k)

    # Step 2: Move the remaining (n - k) elements to the back
    for _ in range(n - k):
        q.put(q.get())

    return q

def takeInput():
    n=int(stdin.readline().strip())
    q = queue.Queue()
    values = list(map(int,stdin.readline().strip().split()))
    for i in range(n):
        # q.put('1')
        q.put(values[i])
    return q

t = int(stdin.readline().strip())

while t > 0:

    qu = takeInput()
    reverseFirstKQueue(qu,3)

    while not qu.empty():
        f=qu.get()
        print(f, end=" ")

    print()

    t -= 1

