# 🧩 Problem: First Non-Repeating Character
# Given a string s, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Example 1:
# Input: "leetcode"
# Output: 0
#
# Example 2:
# Input: "loveleetcode"
# Output: 2
#
# Example 3:
# Input: "aabb"
# Output: -1

def firstnonrepchar(str):
    count ={}
    for i in str:
        count[i]=count.get(i,0)+1
    for i,char in enumerate(str):
        if count[char] == 1:
            return i
    return -1

#The enumerate() function lets you loop through a list (or any iterable) and keep track of the index of each item at the same time.
res = firstnonrepchar('oolloo')
print(res)