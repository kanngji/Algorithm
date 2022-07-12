'''
조건문 if(분기,중첩)
'''

# x=6
# x가 7인 것이 참이면 lucky 출력
# if x== 7:
#     print("lucky")
# 7이 아니면 땡 출력
# else:
#     print("떙")

# x=15
# if x>=10:
#     if x%2==1:
#         print("10이상의 홀수")
    
# y=12
# # y가 12이기떄문에 if y>=10: 는 통과한다
# if y>=10:
#     # 하지만 12%2==0 이기떄문에 밑에꺼는 거짓으로 10이상의 홀수는 출력하지않는다
#     if y%2==1:
#         print("10이상의 홀수")

# if문 하나로 처리하기
# x가 0보다 크고 10보다 작다
# x=8
# if x>0 and x<10:
#     print("10보다 작은 자연수")

# 파이썬은 and 연산 안써도 되지롱
# if 0<x<10:

# x=10
# if x>0:
#     print("양수")
# #if 절이 거짓인 경우 else절로 간다.
# else:
#     print("음수")

# 다중 if문
x=93
if x>90:
    print("A")
elif x>80:
    print("B")
elif x>70:
    print("C")
else:
    print("F")