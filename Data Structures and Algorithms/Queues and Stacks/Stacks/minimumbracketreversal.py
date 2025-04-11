# Problem statement
# For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
#
# If the expression can't be balanced, return -1.
#
# Example:
# Expression: {{{{
# If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.
#
# Expression: {{{
# In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the expression.
#
# Time Limit: 1sec
# Sample Input 1:
# {{{
# Sample Output 1:
# -1
# Sample Input 2:
# {{{{}}
# Sample Output 2:
# 1
#
# from sys import stdin
#
def minimumbracket(exp):
    st =[]
    count =0
    for i in exp:
        if i == '{':
            st.append(i)
        elif i == '}' and len(st)!=0:
             st.pop()
        elif i == '}' and len(st) == 0:
            count += 1
    number = len(st) % 2
    if len(st) % 2 != 0 or count % 2 != 0:
        return -1
    else:
        return (len(st) // 2) + (count // 2)

s=minimumbracket('{{{')
print(s)