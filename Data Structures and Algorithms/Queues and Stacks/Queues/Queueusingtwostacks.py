# Problem statement
# You will be given ‘Q’ queries. You need to implement a queue using two stacks according to those queries. Each query will belong to one of these three types:
#
# 1 ‘X’: Enqueue element ‘X’  into the end of the nth queue. Returns true after the element is enqueued.
#
# 2: Dequeue the element at the front of the nth queue. Returns -1 if the queue is empty, otherwise, returns the dequeued element.
# Note:
# Enqueue means adding an element to the end of the queue, while Dequeue means removing the element from the front of the queue.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= Q <= 10^5
# 1 <= P <= 2
# 1 <= X <= 10^5
#
# Time limit: 1 sec
# Sample Input 1:
# 7
# 1 2
# 1 3
# 2
# 1 4
# 1 6
# 1 7
# 2
# Sample Output 1:
# True
# True
# 2
# True
# True
# True
# 3
# Explanation of Sample Output 1:
# For this input, we have the number of queries, 'Q' = 7.
#
# Operations performed on the queue are as follows:
#
# push(2): Push element ‘2’ into the queue. This returns true.
# push(3): Push element ‘3’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 2.
# push(4): Push element ‘4’ into the queue. This returns true.
# push(6): Push element ‘6’ into the queue. This returns true.
# push(7): Push element ‘7’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 3.
# Sample Input 2:
# 7
# 1 11
# 1 51
# 1 26
# 2
# 1 6
# 2
# 2
# Sample Output 2:
# True
# True
# True
# 11
# True
# 51
# 26
# Explanation for Sample Output 2:
# For this input, we have the number of queries, Q = 7.
#
# Operations performed on the queue are as follows:
#
# push(11): Push element ‘11’ into the queue. This returns true.
# push(51): Push element ‘51’ into the queue. This returns true.
# push(26): Push element ‘26’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 11.
# push(6): Push element ‘6’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 51.
# pop(): Pop the top element from the queue. This returns 26.

from os import *
from sys import *
from collections import *
from math import *

class queueusingtwostacks:
    def __init__(self):
        self.__s1 = []
        self.__s2 =[]

    def enqueue(self,x):
        #O(n)
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        self.__s1.append(x)
        while len(self.__s2) != 0:
            self.__s1.append(self.__s2.pop())
        return True
    #dequeue should return 1 if stack is empty else pop the first element in the stack
    def dequeue(self):
        #O(1)
        if len(self.__s1) == 0:
            return -1
        return self.__s1.pop()
    def front(self):
        #return the front element else return -1
        #O(1)
        if len(self.__s1) == 0:
            return -1
        return self.__s1[-1]
    def size(self):
        if len(self.__s1) == 0:
            return -1
        return len(self.__s1)
    def isEmpty(self):
        return self.size == 0

#main
q = int(stdin.readline().strip())
queue = queueusingtwostacks()
while q > 0:
    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])
    #
    if choice == 1:
        data = int(inputs[1])
        res = queue.enqueue(data)
        print(res)
    elif choice == 2:
        print(queue.dequeue())
    elif choice == 3:
        print(queue.front())
    elif choice == 4:
        print(queue.size())
    else:
        if queue.isEmpty():
            print("true")
        else:
            print("false")
    q -= 1
