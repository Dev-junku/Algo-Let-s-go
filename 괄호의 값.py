string = input()

def comfirm(string):

    stack = []
    for s in string:
        if s == '(':
            stack.append('(')
        elif s == ')' and stack:
            v = stack.pop()
            if v == '(':
                continue
            else:
                return False
        elif s == '[':
            stack.append('[')
        elif s == ']' and stack:
            v = stack.pop()
            if v == '[':
                continue
            else:
                return False
    if not stack:
        return True
    else:
        return False


def sum_s(string):
    stack = []
    for s in string:
        print(stack)
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                total = 0
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = total*2
                        break
                    else:
                        total += stack[-1]
                        stack.pop()
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                total = 0
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = total*3
                        break
                    else:
                        total += stack[i]
                        stack.pop()
    return sum(stack)

if comfirm(string):
    print(sum_s(string))
else:
    print(0)




