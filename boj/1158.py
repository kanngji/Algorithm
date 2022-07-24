import sys
#deque를 쓸려면 이걸 꼭해야함
from collections import deque

#n,k 받기
n,k=map(int,input().split())

#1번 부터 n명 까지 세팅하기
dq=list(range(1,n+1))
#deque 사용하기
dq=deque(dq)
#정답 넣을 answer 리스트 생성
answer=[]

cnt=1
while(len(dq)!=1):
    #k번째 사람이면 popleft()하고 answer에 넣어주기
    if cnt==k:
        answer.append(dq.popleft())
        #그리고 cnt 초기화
        cnt=1
    else:
        #아니라면 cnt+=1 해주고 popleft()한것을 다시 추
        cnt+=1
        dq.append(dq.popleft())
        
#dq마지막 요소를 answer에 투입
answer.append(dq[0])



    
