# Stack is a Abstract data Type and linear data Structure.it follows LIFO model.here is the simple implementation using array
from sys import stdin
class stack:
    def __init__(self):
        self.__stackarr=[]
    def push(self,data):
        self.__stackarr.append(data)
        return
    def pop(self):
        if self.isempty():
            return -1
        return self.__stackarr.pop()
    def isempty(self):
        return len(self.__stackarr)==0
    def top(self):
        if self.isempty():
            return -1
        return self.__stackarr[-1]
    def getsize(self):
        return len(self.__stackarr)

    def __str__(self):
        return str(self.__stackarr)


q = int(stdin.readline().strip())
st = stack()

while q>0:
    inputs = stdin.readline().strip().split(" ")
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
    q -= 1
