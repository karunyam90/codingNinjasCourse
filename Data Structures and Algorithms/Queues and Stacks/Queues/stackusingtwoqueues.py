# Problem statement
# Implement a Stack Data Structure specifically to store integer data using two Queues. You have to implement it in such a way that the push operation is done in O(1) time and the pop and top operations are done in O(N) time.
#
# There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.
#
# Implement the following public functions :
#
# 1. Constructor:
# It initialises the data members as required.
#
# 2. push(data) :
# This function should take one argument of type integer. It pushes the element into the stack and returns nothing.
#
# 3. pop() :
# It pops the element from the top of the stack and in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.
#
# 4. top :
# It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.
#
# 5. size() :
# It returns the size of the stack at any given instance of time.
#
# 6. isEmpty() :
# It returns a boolean value indicating whether the stack is empty or not.
#
# Operations Performed on the Stack:
# Query-1(Denoted by an integer 1): Pushes an integer data to the stack.
#
# Query-2(Denoted by an integer 2): Pops the data kept at the top of the stack and returns it to the caller.
#
# Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the top of the stack but doesn't remove it, unlike the pop function.
#
# Query-4(Denoted by an integer 4): Returns the current size of the stack.
#
# Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the stack is empty or not.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= q <= 100
# 1 <= x <= 5
# -2^31 <= data <= 2^31 - 1 and data != -1
#
# Where 'q' is the total number of queries being performed on the stack, 'x' is the range for every query and data represents the integer pushed into the stack.
#
# Time Limit: 1 second
# Sample Input 1:
# 6
# 1 13
# 1 47
# 4
# 5
# 2
# 3
# Sample Output 1:
# 2
# false
# 47
# 13
#
# Explanation: The operations are as follows:
# Push 13 into the stack.
# Push 47 into the stack.
# Print the size of the stack. Since we have pushed two elements, the size is 2.
# Check if the stack is empty. Since there are elements in the stack, it returns false.
# Pop the top element from the stack. The top element is 47, so it is removed and returned.
# Fetch and return the top element of the stack. Now, the top element is 13, so 13 is returned.
# So, the output for this test case is 2 false 47 13.
# Sample Input 2:
# 4
# 5
# 2
# 1 10
# 5
#  Sample Output 2:
# true
# -1
# false
#
# Explanation: The operations are as follows:
# Check if the stack is empty. Since no elements have been pushed yet, it returns true.
# Try to pop the top element from the stack. Since the stack is empty, it returns -1.
# Push 10 into the stack.
# Check if the stack is empty. Since there is one element in the stack, it returns false.
# So, the output for this test case is true -1 false.
import queue
from sys import stdin


class Stack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def getSize(self):
        return self.q1.qsize()

    def isEmpty(self):
        return self.getSize() == 0

    def push(self, data):
        self.q1.put(data)

    def pop(self):
        if self.isEmpty():
            return -1

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        ans = self.q1.get()

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return ans

    def top(self):

        if self.isEmpty():
            return -1

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        ans = self.q1.get()
        self.q2.put(ans)

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return ans


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1