#변수는 간단하게 데이타들을 저장하는 공간이다
#변수는 알파벳이나 숫자로 짓는다
#변수명 정하기
# 1) 영문과 숫자, _로 이루어진다
# 2) 대소문자를 구분한다
# 3) 문자나 , _로 시작한다
# 4) 특수문자를 사용하면 안된다. (& ,% 등)
# 5) 키워드를 사용하면 안된다. (if , for 등)


#1을 a라는 변수에 집어넣겠다 (대입) !!같다라는 뜻이 아님!!
# a = 1
# A = 2


#a와 A는 다르기 때문에 a는 1 A는 2가 찍힌다.
# print(a)
# print(A)

'''
여러줄을
주석
처리
하는
방법
입니다'''


# 3개를 한번에 넣기
# a,b,c = 3,2,1
# print(a,b,c)

# 값 교환 이거는 javascript 에서는 안되고 파이썬에는 가능
# a,b=10,20
# print(a,b)
# a,b=b,a
# print(a,b)

#변수 타입
a=12345
print(type(a))
b="1234"
print(type(b))
#8바이트 넘어가면 데이터 손실난다.
c=12.1234512341234123
print(c)
print(type(c))

#출력방식
print("number")
a,b,c=1,2,3
print(a,b,c)
print("number",a,b,c)

#seperate 각 변수사이를 = 이후에 나온것으로 정해라
print(a,b,c,sep=', ')

#print() 는 자동 줄바꿈 end로 자동줄바꿈 막기.
print(1, end=' ')
print(100, end=' ')
print(1000)