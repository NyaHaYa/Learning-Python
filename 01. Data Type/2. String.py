#   자료형

##  문자형  ##


# 문자열(String)이란 문자, 단어등으로 구성된 문자들의 집합을 의미한다. 예를들어,
"Life is Egg"
"삷은 계란이다"
"a"
"777"           # 따옴표로 둘러싸여 있으면 모두 문자열이다.

## 문자열을 만드는 방법

# 1. 큰 따옴표로 양쪽 둘러싸기
"Hello World!!"
# 2. 작은 따옴표로 양쪽 둘러싸기
'Hello World!!'
# 3. 큰 따옴표 3개를 써서 둘러싸기
"""Hello World!!"""
# 4. 작은 따옴표 3개를 써서 둘러싸기
'''Hello World!!'''

lines = """
    Hello World!!
    My Name is
    Suk-Min
    """
print(lines)            # Hello World!!
                        # My Name is
                        # Suk-Min

## 문자열 곱하기
s = "Hello"
print(s * 2)            # HelloHello

## 문자열 인덱싱 & 슬라이싱
line = "Life is Egg"
print([line[2]])        # f
                        # "Life is Egg"의 3번째 자리인 "f"가 출력된다.

line = "Life is Egg"
print(line[0:4])        # Life  (0 ~ 4번째 자리까지 출력한다. [ 시작번호 : 끝번호 ])

## 문자열 포매팅
"I have %d Eggs" % 3            # I have 3 Eggs
"I have %s Eggs" % "Two"            # I have Two Eggs

num = "Two"
"I have %s Eggs" % num          # I have Two Eggs

"I have {0} Eggs".format(10)            # I have 10 Eggs
"I have {0} Eggs".format("Ten")         # I have Ten Eggs
"I have {0} Eggs".format(num)           # I have Two Eggs

"I have {num} Eggs and ate {ate}".format(num=3, ate=2)          # I have 3 Eggs and ate 3

## 문자 개수 세기
a = "Hello"
print(a.count('l'))         # 2

# 문자 위치 알려주기
a = "Life is Egg"
print(a.find('E'))          # 8
print(a.find('h'))          # -1 (찾는 문자나 문자열이 존재하지 않으면 -1 반환)

print(a.index('E'))         # 8
print(a.index('h'))         # ValueError: substring not found (찾는 문자가 없기 때문에 에러)

## 문자열 함수 ##

## 문자열 집어넣기
a = ","
a.join('hello')         # 'h,e,l,l,o'

## 소문자를 대문자로
a = "hello"
a.upper()           # HELLO

## 대문자를 소문자로
a = "HELLO"
a.lower(O)          # hello

## 왼쪽 공백 지우기
a = " hi "
a.lstrip()          # 'hi '

## 오른쪽 공백 지우기
a = " hi "
a.rstrip()          # ' hi'

## 양쪽 공백 지우기
a = " hi "
a.strip()           # 'hi'

## 문자열 바꾸기
a = "Life is Egg"
a.replace("Life", "Money")          # 'Money is Egg'

## 문자열 나누기
a = "Life is Egg"
a.split()           # ['Life', 'is', 'Egg']
a = "a:b:c:d"
a.split()           # ['a', 'b', 'c', 'd']

