s = ""
stack = []

def CheckValidParenthesis(s):
    for val in s:
        if val == "(":
            stack.append(val)
        else:
            if stack and val == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

print(CheckValidParenthesis(s))
