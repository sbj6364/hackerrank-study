if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        S = input().split()
        cmd = S[0]
        if cmd == 'print':
            print(L)
        elif cmd == 'insert':
            L.insert(int(S[1]), int(S[2]))
        elif cmd == 'append':
            L.append(int(S[1]))
        elif cmd == "remove":
            L.remove(int(S[1]))
        elif cmd == "pop":
            L.pop()
        elif cmd == "append":
            L.append(int(S[1]))
        elif cmd == "sort":
            L.sort()
        else:
            L.reverse()
