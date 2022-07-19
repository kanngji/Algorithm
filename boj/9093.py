#문장이 주어졌을 때 단어를 모두 뒤집어서 출력하는 프로그램
#첫째 줄에 테스트 케이스의 개수 T가 주어진다
#단어와 단어 사이에는 공백이 하나 있다


t=int(input())

for _ in range(t):
    text=input().split()
    #print(len(text))
    for i in range(len(text)):
        a=text[i]
        #문자열 거꾸로 출력
        print(a[::-1],end=' ')
    print()
        

