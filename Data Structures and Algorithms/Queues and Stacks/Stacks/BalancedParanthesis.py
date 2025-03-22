# Problem statement
# For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. Brackets are said to be balanced if the bracket which opens last, closes first.
#
#
#
# Example:
# Expression: (()())
# Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
# You need to return a boolean value indicating whether the expression is balanced or not.
#
# Note:
# The input expression will not contain spaces in between.
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
# Solution:
# 1. Check the expression starting with closed paranthesis
# 2. check whether the paranthesis is balanced by providing the appropriate open and close
# 3. return true if balanced else false

def isbalanced(exp):
    open =['{','[','(']
    close = ['}',')',']']
    pairs = {'{':'}','[':']','(':')'}
    stack =[]
    if exp[0] in close:
        return False
    for e in exp:
        if e in open:
            stack.append(e)
        elif e in close:
            if not stack or pairs[stack[-1]] != e:
                print(pairs[stack[-1]] != pairs.get(e))
                return False
            stack.pop()
    return len(stack) == 0


result=isbalanced('}a+b}+c')
print(result)