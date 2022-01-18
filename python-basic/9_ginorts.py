S = input()

lower = []
upper = []
odd = []
even = []

for c in sorted(S):
    try:
        if int(c) % 2 == 0:
            even.append(c)
        else:
            odd.append(c)
    except:
        if c.upper() == c:
            upper.append(c)
        else:
            lower.append(c)

result = ''.join(lower + upper + odd + even)
print(result)