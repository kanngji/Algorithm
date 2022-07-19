#테스트 케이스 개수 t
#올바른 괄호 문자열이면 yes
#아니면 no를 출력해라

t = int(input())
for _ in range(t):
    string=input()
    
    #일단 올바른 괄호문자가 참이라고 설정
    flag=True
    cnt=0
    #처음 괄호가 )이면 무조건 no다
    for i in range(len(string)):
        if string[0]==")":
            
            flag=False
            break
        if string[i]=="(":
            cnt+=1
        elif string[i]==")":
            cnt-=1

        if cnt<0:
            
            flag=False
            break

        if string[-1]=="(":
            
            
            flag=False
            break
    
    if(cnt==0 and flag==True):
        print("YES")
    else:
        print("NO")
            
#실수한점: flag=False 를 flag==false로 넣어서 시간씀. 
        





                        
                
            
                
