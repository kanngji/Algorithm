# 문자열은 문자들로 구성된 시퀀스이고, 
# 리스트는 값으로 구성된 시퀀스지만, 
# 문자들로 구성된 리스트는 문자열과 같지는 않다.
# 설명 잘되있는 싸이트: https://seongonion.tistory.com/53

#1406 에디터
#list
#append() :원소 마지막에 추가
#insert() : (입력할 index,값)

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif cmd[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif cmd[0]=='B':
        if st1:
            st1.pop()
    else:
        st1.append(cmd[1])

st1.extend(reversed(st2))
print(''.join(st1))

