#push x:정수 x를 스택에 넣는 연산이다
#pop: 스택에서 가장 위에있는 정수를 빼고, 
#그 수를 출력한다.만약 스택에 들어있는 정수가
#없는 경우에는 -1출력
#size:스택에 들어있는 정수의 개수를 출력한다.
#empty: 스택이 비어있으면 1, 아니면 0을 출력한다
#top: 스택의 가장 위에 있는 정수를 출력
#만약 스택에 들어있는 정수가 없는 경우에는 -1출력

#입력: 첫째 줄에는 주어지는 명령의 수
#둘째 줄 부터 n개의 줄에서는 명령이 하나씩 주어진다
import sys
#n을 명령의 수로 받았다.
n=int(input())
stack=[]
#띄어쓰기 기준으로 cmd를 받는다 cmd[0]은 커맨드 이름
#ex)push,pop,size,empty,top 등등...

#cmd[0]이 'push'이면 stack에 cmd[1] ex) push 5 라면
#5를 append한다
for _ in range(n):
    cmd=input().split()
    if cmd[0]=='push':
        stack.append(cmd[1])
    if cmd[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    if cmd[0]=='size':
        print(len(stack))
    if cmd[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if cmd[0]=='pop':
        if len(stack)==0:
           print(-1)
        else:
            print(stack.pop())








