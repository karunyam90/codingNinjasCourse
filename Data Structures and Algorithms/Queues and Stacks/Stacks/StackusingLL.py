#node has data and next pointer
from sys import stdin
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create a stack with head and count
#imlpement push,pop,isempty,top and getsize opeerations
class stack:
    def __init__(self):
        self.__head = None
        self.__count = 0
    def push(self,data):
        newnode = Node(data)
        newnode.next = self.__head
        self.__head = newnode
        self.__count += 1

    def pop(self):
        #if it is underflow
        if self.isempty():
            return -1
        popped_data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return popped_data
    def isempty(self):
        return self.__count == 0

    def top(self):
        return self.__head.data

    def getsize(self):
        return self.__count
    def __str__(self):
        results =[]
        temp=self.__head
        while temp:
            results.append(str(temp.data))
            temp = temp.next
        return '->'.join(results) if results else 'empty'

q= int(stdin.readline().strip())
st=stack()
while q>0:
    inputs = stdin.readline().strip().split(' ')
    choice = int(inputs[0])
    if choice == 1:
        data = int(inputs[1])
        st.push(data)
    if choice == 2:
        st.pop()
    if choice == 3:
        data = st.isempty()
        print(data)
    if choice == 4:
        data = st.top()
        print(data)
    if choice == 5:
        data = st.getsize()
        print(data)
    if choice ==6:
        print(st)
    q=q-1