import re

p = re.compile("ca.e") 
# 원하는 형태 : 정규식
# . (ca.e): 하나의 문자를 의미
# ^ (^de): 문자열의 시작
# $ (se$): 문자열의 끝

def print_match(m):
    if m:
        print("m.group() : ",m.group()) # 일치하는 문자열 반환
        print("m.string : ",m.string) # 입력받은 문자열 반환 함수X
        print("m.start() : ",m.start()) # 입력받은 문자열의 시작 index
        print("m.end() : ",m.end()) # 입력받은 문자열의 끝 index
        print("m.span() : ",m.span()) # 입력받은 문자열의 끝 index
    else:
        print("매칭되지않음")

# m=p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 (good care) X (careless) O
# print_match(m)
# print(m.group()) # 매치되지않으면 에러가 발생

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는지 확인
# print_match(m)

lst = p.findall("careless cafe cave") # findall : 일치하는 모든 것을 "리스트" 형태로 반환
print(lst)