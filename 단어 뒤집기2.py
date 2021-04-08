string = input()

res = ''
i = 0
while i < len(string):
    if string[i] == '<':
        res += '<'
        i += 1
        while string[i] != '>':
            res += string[i]
            i += 1
    elif string[i] != '<' or  string[i] == ' ':
        word = ''
        while True:
            word += string[i]
            i += 1

            if i == len(string):
                res += word[::-1]
                break

            elif string[i] == ' ':
                res += word[::-1]
                break

            elif string[i] == '<':
                res += word[::-1]
                break
    if i == len(string):
        break
    if string[i] == '>':
        res += '>'
        i += 1
    elif string[i] == ' ':
        res += ' '
        i += 1

print(res)





