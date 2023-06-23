from collections import deque
d = deque()
n = int(input().slice())
print(n)
for i in range(1,n+1):
    txt = input()
    a = txt.split(" ")[0]
    b = txt.split(" ")[1]
    getattr(d,f"{a}({b})")
