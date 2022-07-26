# https://school.programmers.co.kr/learn/courses/30/lessons/12954

#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가
#하는 숫자를 n개 지니는 리스트를 리턴해야합니다

#예
#x=2 n=5 answer 2,4,6,8,10

#x와 n을 입력받자
def solution(a,b):
    # 답을 위한 list 생성
    answer=[]
    # a만큼 증가 시켜야함으로 i=a 를 주었다
    # 그것도 모르고 a+=a 줘서 오답나옴...
    i=a
    for _ in range(b):
        answer.append(a)
        a+=i 
    return answer
x,n=map(int,input().split())
print(solution(x,n))

