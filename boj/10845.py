#10845 Queue
#파이썬에서 queue를 사용하려면 list를 이용해야함

#push x : 정수 x를 큐에 넣는다
#pop : 큐에서 가장 앞에있는 정수를 빼고 그 수를 출력
#큐에 들어있는 정수가 없을떄 -1
#size: 큐에 들어있는 정수의 개수 출력
#empty : 큐가 비어있으면 1 아니면 0 출력
#front: 큐의 가장 앞에 있는 정수 출력 큐에 정수 없을떄 -1
#back : 큐의 가장 뒤에있는 정수를 출력한다
#만약 큐에 들어있는 정수가 없을 경우 -1 출력

#pop() 마지막 요소 제거 후 반환
#pop(0) 첫번째 요소 제거 후 반환
n = int(input())
queue=[]
for _ in range(n):
    cmd = list(input().split())
    if cmd[0]=="push":
        queue.append(cmd[1])
    elif cmd[0]=="pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))
    elif cmd[0]=="size":
        print(len(queue))
    elif cmd[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0]=="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
                  



        
