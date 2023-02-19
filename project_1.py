print(5+4) #연산
print('lol') #문자열
print('ㅋ'*8) #문자 연산 가능
print(5 < 10) # boolean
print(not True) # not 

# 변수
name = "연탄"
animal = 'cat'
age =4
is_adult = age>=3
print("우리집"+animal+"이고 "+name+"이야")
print(name+"는"+str(age)+"살이고") # + 이용시 문자형이 아닌 형태르르 출력시 str()이 필요함
print("어른 일까요?", is_adult) # , 사용시 str()필요없음

# 주석
'''이것도 주석임'''
'''ctrl + /'''

# 연산자
print(2**3) #8
print(5%3) #2 나머지
print(5//3) #1 몫
print(3 == 3) # TRUE
print( 3 != 3 ) # FALSE
print((3>0) and (3<5)) # and = &
print((3>0) or (3>5)) # or  = |

# n+=1
# n = n+1

#숫자 처리 함수
print(abs(-5)) # 절대값
print(pow(4,5)) # 승 , 제곱
print(max(5,12)) # 최대값
print(min(5,12)) # 최솟값
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

# random
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 1.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 정수값 생성
print(int(random() * 45) + 1 ) # 1~ 45이하의 임의의 정수값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 정수값 생성
print(randint(1, 45)) # 1 ~ 45 미만의 임의의 정수값 생성

#문자열
sentence = """
아주 좋은 
꿀팁이요!
"""
print(sentence)

#슬라이싱
some = "010812-1234567"

print("sex : "+ some[7])
print("year : "+ some[0:2]) # 0부터 2직전까지 (0,1)
print("month : "+ some[2:4])
print("day : "+ some[4:6])

print("front : "+ some[:6]) #처음부터 6직전까지
print("back : "+ some[7:]) #7부터 끝까지
print("뒤 7자리(뒤에부터) : "+ some[-7:]) # 맨 뒤7번째 부터 끝까지

# 문자열 처리 함수
pyth0n = "python is Amazing"
print(pyth0n.lower()) # 소문자
print(pyth0n.upper()) # 대문자
print(pyth0n[0].isupper()) # 대문자인가?
print(len(pyth0n))
print(pyth0n.replace("Python", "Java")) # Python -> Java 교체
index = pyth0n.index("n") #'n'이 어디있냐
print(index)
index = pyth0n.index("n", index +1) #다음 'n'이 어디있냐
print(index)
print(pyth0n.find("n")) # n의 위치 / 없을 경우 -1
index = pyth0n.index("n") #에러 발생후 프로그램 종료

print(pyth0n.count("n")) # n의 개수

#문자열 포멧
print("나는 %d살입니다." % 20) # 나는 20살입니다
print("나는 %s을 좋아합니다." % "파이썬") # 나는 파이썬을 좋아합니다.
print("Apple 은 %c로 시작해요." % "A") # Apple 은 A로 시작해요.
print("나는 %s살입니다." % 20) # 나는 20살입니다 (%s 로도 정수값 표현 가능)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다.".format(20)) # 나는 20살입니다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 나는 빨간색과 파란색을 좋아해요

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))# 나는 20살이며, 빨간색을 좋아해요
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))# 나는 20살이며, 빨간색을 좋아해요 (.format 뒤에 순서를 변경해도 괜찮아요)

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
 #\n 줄바꿈
print('저는 "나도코딩"입니다.')
print('저는 \"나도코딩\"입니다.')
# \\ -> \
print("Red Apple\rPine") # PineApple

#리스트
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호")) # 조세호씨가 몇 번째 칸에 타고 있는가?
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하 내림
print(subway) # ['유재석', '정형돈', '조세호', '박명수']
#유재석 추가
subway.append("유재석")
print(subway.count("유재석")) # 유재석씨가 2명

num_list = [5, 2, 4, 3, 1]
num_list.sort() # 정렬
print(num_list) # [1, 2, 3, 4, 5]

num_list.reverse() # 순서 뒤집기
print(num_list) # [5, 4, 3, 2, 1]

num_list.clear()
print(num_list) # []

mix_list = ["조세호", 20, True] # 다양한 자료형
print(mix_list) # ['조세호', 20, True]
num_list = [5, 2, 4, 3, 1] # num_list 값 다시 정의
num_list.extend(mix_list) # 리스트 확장
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]

#사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(5)) # 프로그램 종료 없이 계속 진행 가능
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)  # True
print(5 in cabinet)  # False

# key 는 정수형이 아닌 문자열도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
# 업데이트 또는 추가
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" # key 에 해당하는 값이 있는 경우 업데이트
cabinet["C-20"] = "조세호" # key 에 해당하는 값이 없는 경우 신규 추가
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}
# 삭제
del cabinet["A-3"] # key "A-3" 에 해당하는 데이터 삭제
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}
# 전체 삭제
cabinet.clear()
print(cabinet) # {}
# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])
# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])
# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 튜플
#변경 불가능
menu = ("돈까스", "치즈까스")

name = "김종국"
age = 20
hobby = "코딩"
(name, age, hobby) = ("김종국", 20, "코딩")

#세트, 집합 (set)
my_set = {1, 2, 3, 3, 3} # 중복을 허용하지 않음
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합
print(java | python) # {'박명수', '유재석', '김태호', '양세형'}
print(java.union(python)) # {'박명수', '유재석', '김태호', '양세형'}

# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# python 개발자 추가 (기존 개발자 : 박명수, 유재석)
python.add("김태호")
print(python) # {'박명수', '유재석', '김태호'}

# java 개발자 삭제
java.remove("김태호")
print(java) # {'유재석', '양세형'}

#자료구조 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # menu 의 type 정보 : set

menu = list(menu) # 리스트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : list
menu = tuple(menu) # 튜플 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : tuple
menu = set(menu) # 세트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : set

