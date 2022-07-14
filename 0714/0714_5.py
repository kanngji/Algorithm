'''
함수 만들기
'''
#함수는 main script 위 쪽에 선언해야한다
#인터프리터 ~.~
# def add(a,b):
#     c=a+b
#     print(c)

# add(3,2)

# def add(a,b):
#     c=a+b
#     return c

# num=add(3,2)
# print(num)

#return 값이 2개이면 튜플 값으로 반환한다. 3개도 가능하다
# def add(a,b):
#     c=a+b
#     d=a-b
#     return c,d

# print(add(3,2))
#소수찾기

# def isPrime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# a=[12,13,7,9,19]

# for y in a:
#     if isPrime(y):
#         print(y,end=' ')

'''
람다함수
'''
#익명함수라고도 부른다. 
def plus_one(x):
    return x+1

# print(plus_one(1))

# plus_two = lambda x: x+2
# print(plus_two(2))

a=[1,2,3]

print(list(map(plus_one,a)))
#람다함수
print(list(map(lambda x:x+1,a)))


