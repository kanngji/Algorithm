#deque 를 사용하기 위해서 import 받기
from collections import deque
d=deque()
n=int(input())
for _ in range(n):
    cmd=input().split()


    if cmd[0]=='push_back':
        d.append(cmd[1])
    elif cmd[0]=='push_front':
        d.appendleft(cmd[1])
    elif cmd[0]=='pop_front':
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())
    elif cmd[0]=='pop_back':
        if len(d)==0:
            print(-1)
        else:
            print(d.pop())
    elif cmd[0]=='size':
        print(len(d))
    elif cmd[0]=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
    elif cmd[0]=='back':
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])


#시간 초과나서 따른 풀이 검색
#풀이 방법은 같은데
#import sys
#command = sys.stdin.readline().split() 이렇게 받으니 빨라진데...