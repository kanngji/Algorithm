'''반복문을 이용한 문제풀이
1) 1부터 n까지 홀수 출력하기
2) 1부터 n까지의 합 구하기
3) n의 약수 출력하기
'''

# n = int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         continue
#     print(i)


# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i

# print(sum)

# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

'''
중첩 반복문(2중 for문)

# i가 0~4까지 반복한다 
for i in range(5):
    # i가 0일때 j가 0~4
    # i가 1일때 j가 0~4 
    # ... 돈다
    for j in range(5):
'''

# 별거꾸로 찍기
for i in range(5,0,-1):
    print("*"*i)

