#https://school.programmers.co.kr/learn/courses/30/lessons/12969

# n,m 받기,띄어쓰기 기준으로 n,m받는다

n,m=map(int,input().split())

# 가로가 n 세로가 m 
for _ in range(m):
    print("*"*n)
