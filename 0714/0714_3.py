'''
리스트와 내장함수(2)
'''

a=[23,12,36,53,19]
# print(a[:3])
# print(a[1:4])

# print(len(a))

# for i in range(len(a)):
#     print(a[i], end=' ')
# print()

# for x in a:
#     print(x, end=' ')
# print()

#튜플의 자료형태로 출력되는데 index,value값이 같이 출력된다.
# for x in enumerate(a):
#     print(x)
#소괄호를 열면 튜플이됩니다.
# b=(1,2,3,4,5)
# print(b[0])
# #튜플은 값변경이 불가능합니다.
# b[0]=7

# for x in enumerate(a):
#     print(x[0],x[1])
# print()

# for index, value in enumerate(a):
#     print(index,value)
# print()

#조건이 모두가 참이여야 true를 반환
if all(60>x for x in a):
    print("YES")
else:
    print("NO")
    


#조건이 하나 라도 참이 있으면 true를 반환\
#모두가 거짓일떄 false
if any(50>x for x in a):
    print("YES")
else:
    print("NO")
    
