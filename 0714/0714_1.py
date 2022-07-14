'''
문자열과 내장함수
'''

msg = "It is Time"

# #다 대문자로 통일
# print(msg.upper())

# #다 소문자로 통일
# print(msg.lower())

# tmp=msg.upper()
# print(tmp)

# # T가 어디에있는지 INDEX 번호 출력
# print(tmp.find('T'))
# # T가 몇 개 들어있는지 
# print(tmp.count('T'))

# print(msg)
# print(msg[:2])
# print(msg[3:5])
# print(len(msg))

# for i in range(len(msg)):
#     print(i)

# for i in msg:
#     print(i,end='')

# for x in msg:
#     print(x, end=' ')

# 대문자만 출력하기
# for x in msg:
#     if x.isupper():
#         print(x, end='')

# print()


# for y in msg:
#     if y.islower():
#         print(y,end='')

# 공백죽이고 붙이기

# for x in msg:
#     if x.isalpha():
#         print(x,end='')
# print()

#아스키넘버

tmp='AZ'
for x in tmp:
    #대문자 A 대문자 Z
    #ord 아스키문자 출력
    print(ord(x))
    # A=65 Z=90


tmp='az'
for x in tmp:
    print(ord(x))
    #a=97 z=122

#아스키넘버를 문자로 출력
tmp=65
print(chr(tmp))