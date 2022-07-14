'''
2처원 리시트 생성과 접근
'''
#10개의 인덱스 0으로 초기화 
a=[0]*10
#print(a)

#2차원 배열 생성
a=[[0]*3 for _ in range(3)]
print(a)

#2차원리스트 표처럼 확인
for x in a:
    print(x)

#2차원리스트 값들만 뽑기
for x in a:
    for y in x:
        print(y,end=' ')
    print()

