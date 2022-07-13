'''
반복분 (for,while)
'''
'''
#0~9 까지
a=range(10)
#list로 출력
print(list(a))
'''
'''
for i in range(10):
    print("Hello")

#1부터 10까지 10포함
for i in range (1,11):
    print(i)

#10부터 1까지 1포함
for i in range(10,0,-1):
    print(i)

x=1
while x<=10:
    print(x)
    x+=1

i=1
# 반복문 한무반복
while True:
    print(i)
    if i==10:
        break
    # 연산자 축약 i=i+1과 같음
    i+=1
'''
for i in range(1,11):
    #짝수들은 건너띄고 싶어
    if i%2==0:
        continue
    print(i)