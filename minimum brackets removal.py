s = "))((cd"
stack = []

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    elif s[i] == ")":
        if stack and s[stack[-1]] == "(":
            stack.pop()
        else:
            stack.append(i)

ans = ""
print(stack)
if stack:
    pt = 0
    for j in range(len(s)):
        try:
            if j == stack[pt]:
                pt += 1
                continue
        except Exception as e:
            ans += s[j]
            continue
        else:
            ans += s[j]
    print(ans)
else:
    print(s)