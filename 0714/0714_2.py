'''
리스트와 내장함수(1)
'''
import random as r
#빈리스트 생성
# a=[]
# print(a)
# b=list()
# print(b)

# a=[1,2,3,4,5]
# #print(a)

# #range로도 리스트 초기화 할수있따.
# b=list(range(1,11))
# #print(b)

# #중복은 제거가 안되네요?
# c=a+b
# #print(c)

# print(a)
# a.append(6)
# print(a)
# a.insert(3,7)
# print(a)

# a.pop()
# print(a)
# #3번 인덱스에 있는 값을 빼라
# a.pop(3)
# print(a)
# a.append(1)

# #특정 값을 지우기
# a.remove(1)
# print(a)
# #리스트의 5라는 값이 몇번째 index에 있느냐?
# print(a.index(5))

a=list(range(1,11))
# print(a)
#a라는 리스트에 모든 값을 다 더해라.
# print(sum(a))

#a라는 리스트에 가장 큰 값 ,가장 작은 값 
# print(max(a))
# print(min(a))

# 7,5 인자 값들 중에 최소 값 알아내는 함수
# print(min(7,5))

#a라는 리스트를 무작위로 섞어라
r.shuffle(a)
print(a)
#오름차순으로 a리스트를 정렬
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# 리스트에 있는 값 다 날리기
a.clear()