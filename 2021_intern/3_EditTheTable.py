def solution(n, k, cmd):
    answer = ''
    table = []
    for i in range(n):
        table.append([i, 0])

    tmp = []
    for i in range(len(cmd)):
        print(table)
        if len(cmd[i]) > 1:
            c, n = cmd[i].split(" ")
            n = int(n)
        else:
            c = cmd[i]

        if i == 0:
            if c == "D":
                cur = n + k
                if cur > len(cmd):
                    cur = n - 1

            elif c == "U":
                cur = n - k

            elif c == "C":
                # cmd[cur][2] = 1
                tmp.append(table[cur])
                del table[cur]
                table.append('#')

            elif c == "Z":
                n, state = tmp.pop()
                state = 0
                table.insert(cur,[n, state])
                cur += 1

        else:
            print(cmd[i],"cur:", cur,"tmp:", tmp)
            if c == "D":
                cur = cur + n
                if cur > len(cmd):
                    cur = n - 1

            elif c == "U":
                cur = cur - n

            elif c == "C":
                # print(cmd[cur][2])
                # cmd[cur][2] = 1
                tmp.append(table[cur])
                del table[cur]
                table.append('#')
                

            elif c == "Z":
                print(tmp)
                n, state = tmp.pop()
                state = 0
                table.insert(cur, [cur, state])
                cur += 1
    print(table, tmp)
    for i in range(len(table)):
        if table[i] == '#':
            break
        if table[i][0] == i:
            answer += 'O'
        else:
            answer += 'x'
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
sol = solution(n, k, cmd)
print(sol)