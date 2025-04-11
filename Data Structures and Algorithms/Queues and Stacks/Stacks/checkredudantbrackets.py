# Problem statement
# For a given expression in the form of a string, find if there exist any redundant brackets or not. It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
#
# A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.
#
# Example:
# Expression: (a+b)+c
# Since there are no needless brackets, hence, the output must be 'false'.
#
# Expression: ((a+b))
# The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.
# Note:
# You will not get a partial score for this problem. You will get marks only if all the test cases are passed.
# Return "false" if no brackets are present in the input.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the expression.
#
# Time Limit: 1 second
# Sample Input 1:
# a+(b)+c
# Sample Output 1:
# true
# Explanation:
# The expression can be reduced to a+b+c. Hence, the brackets are redundant.
# Sample Input 2:
# (a+b)
# Sample Output 2:
# false
#
#
def redudant(exp):
    temp=0
    if len(exp)==0:
        return -1
    for i in range(len(exp)-1):
        if exp[i] == '(' and exp[i+2] == ')':
            return True
        if exp[i] == '(' and exp[i + 1] == '(':
            print(i,i+1)
            temp = 2
        if exp[i] == ')' and exp[i + 1] == ')' and temp == 2:
            return True
    return False


exp ='((a+b)*(c+d))'
res = redudant(exp)
print(res)