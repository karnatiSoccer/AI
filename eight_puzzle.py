from collections import deque

goal = "123456780"

def moves(s):
    i = s.index('0')
    res = []
    for j,c in [(i-1,i%3),(i+1,i%3!=2),(i-3,i>2),(i+3,i<6)]:
        if c:
            t = list(s)
            t[i], t[j] = t[j], t[i]
            res.append("".join(t))
    return res

print("Enter puzzle (use 0 for blank):")
start = "".join(input().replace(" ","") for _ in range(3))  # fix input

q = deque([(start,0)])
vis = {start}

found = False

while q:
    s,step = q.popleft()
    if s == goal:
        print("Steps:", step)
        found = True
        break
    for m in moves(s):
        if m not in vis:
            vis.add(m)
            q.append((m,step+1))

if not found:
    print("No solution")