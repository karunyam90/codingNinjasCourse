# Problem statement
# You have been given two stacks that can store integers as the data. Out of the two given stacks, one is populated and the other one is empty. You are required to write
# a function that reverses the populated stack using the one which is empty.
# Constraints:
# 1 <= N <= 10^3
# -2^31 <= data <= 2^31 - 1
# Output:
# Sample Input 1:
# 6
# 1 2 3 4 5 10
# Note:
# Here, 10 is at the top of the stack.
# Sample Output 1:
# 1 2 3 4 5 10
# Note:
# Here, 1 is at the top of the stack.
# Sample Input 2:
# 5
# 2 8 15 1 10
# Sample Output 2:
# 2 8 15 1 10

def reversestack(s1,s2):
    if len(s1) <= 1:
        return
    data = s1.pop()
    reversestack(s1, s2)
    while s1:
        s2.append(s1.pop())
    s1.append(data)
    while s2:
        s1.append(s2.pop())
    return s1
s1=[1,2,3,4,5]
s2=[]
res = reversestack(s1,s2)
print(res)