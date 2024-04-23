"""
Python 기본 데이타 타입
"""

int(3.5)  # 3
2e3  # 2000.0
float("1.6")  # 1.6
float("inf")  # 무한대
float("-inf")  # -무한대
bool(0)  # False. 숫자에서 0만 False임,
bool(-1)  # True
bool("False")  # True
a = None  # a는 None
a is None  # a가 None 이므로 True

"""
복소수
"""
v = 2 + 3j
v.real  # 2
v.imag  # 3


"""
문자열
"""
s = "가나다"
s = "가나다"

s = """아리랑
아리랑
아라리요
"""
print(s)

s = "아리랑\n아리랑\n아라리요"
print(s)

s = "ABC"
type(s)  # class 'str'
v = s[1]  # B
type(s[1])  # class 'str'

path = r"C:\Temp\test.csv"
print(path)

s = ",".join(["가나", "다라", "마바"])
print(s)
# 출력: 가나,다라,마바

s = "".join(["가나", "다라", "마바"])
print(s)
# 출력 : 가나다라마바


items = "가나,다라,마바".split(",")
print(items)
# 출력 : ['가나', '다라', '마바']

departure, _, arrival = "Seattle-Seoul".partition("-")
print(departure)
# 출력 : Seattle

# 위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)  # 출력: Name: 강정수, Age: 30

# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s)  # 출력: Name: 강정수, Age: 30

# object의 인덱스 혹은 키를 사용하여 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x=area)
print(s)  # 출력: width: 10, height: 20


"""
조건문
"""
x = 1
if x < 10:
    print(x)
    print("한자리수")

# 한 라인에서 표현된 if 문
if x < 100:
    print(x)

x = 10
if x < 10:
    print("한자리수")
elif x < 100:
    print("두자리수")
else:
    print("세자리 이상")

n = 1
if n < 10:
    pass
else:
    print(n)


"""
반복문
"""
i = 1
while i <= 10:
    print(i)
    i += 1

sum_ = 0
for i in range(11):
    sum_ += i
print(sum_)

list_ = ["This", "is", "a", "book"]
for s in list_:
    print(s)

i = 0
sum_ = 0
while True:
    i += 1
    if i == 5:
        continue
    if i > 10:
        break
    sum_ += i

print(sum_)

numbers = range(2, 11, 2)

for x in numbers:
    print(x)

# 출력: 각 라인에 2 4 6 8 10 출력


"""
List
"""
a = []  # 빈 리스트
a = ["AB", 10, False]

a = ["AB", 10, False]
x = a[1]  # a의 두번째 요소 읽기
a[1] = "Test"  # a의 두번째 요소 변경
y = a[-1]  # False

a = [1, 3, 5, 7, 10]
x = a[1:3]  # [3, 5]
x = a[:2]  # [1, 3]
x = a[3:]  # [7, 10]

a = ["AB", 10, False]
a.append(21.5)  # 추가
a[1] = 11  # 변경
del a[2]  # 삭제
print(a)  # ['AB', 11, 21.5]

# 병합
a = [1, 2]
b = [3, 4, 5]
c = a + b
print(c)  # [1, 2, 3, 4, 5]

# 반복
d = a * 3
print(d)  # [1, 2, 1, 2, 1, 2]

mylist = "This is a book That is a pencil".split()
i = mylist.index("book")  # i = 3
n = mylist.count("is")  # n = 2
print(i, n)

list = [n**2 for n in range(10) if n % 3 == 0]

print(list)
# 출력: [0, 9, 36, 81]


"""
Tuple
"""
t = ("AB", 10, False)
print(t)

t1 = 123
print(t1)  # int 타입

t2 = (123,)
print(t2)  # tuple 타입

t = (1, 5, 10)

# 인덱스
second = t[1]  # 5
last = t[-1]  # 10

# 슬라이스
s = t[1:2]  # (5)
s = t[1:]  # (5, 10)

# 병합
a = (1, 2)
b = (3, 4, 5)
c = a + b
print(c)  # (1, 2, 3, 4, 5)

# 반복
d = a * 3  # 혹은 "d = 3 * a" 도 동일
print(d)  # (1, 2, 1, 2, 1, 2)

name = ("John", "Kim")
print(name)
# 출력: ('John', 'Kim')

firstname, lastname = ("John", "Kim")
print(lastname, ",", firstname)
# 출력: Kim, John


"""
Dictionary
"""
scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores["민수"]  # 특정 요소 읽기
scores["민수"] = 88  # 쓰기
print(t)

# 1. Tuple List로부터 dict 생성
persons = [("김기수", 30), ("홍대길", 35), ("강찬수", 25)]
mydict = dict(persons)

age = mydict["홍대길"]
print(age)  # 35

# 2. Key=Value 파라미터로부터 dict 생성
scores = dict(a=80, b=90, c=85)
print(scores["b"])  # 90

scores = {"철수": 90, "민수": 85, "영희": 80}
scores["민수"] = 88  # 수정
scores["길동"] = 95  # 추가
del scores["영희"]
print(scores)
# 출력 {'철수': 90, '길동': 95, '민수': 88}


scores = {"철수": 90, "민수": 85, "영희": 80}

for key in scores:
    val = scores[key]
    print("%s : %d" % (key, val))

scores = {"철수": 90, "민수": 85, "영희": 80}

# keys
keys = scores.keys()
for k in keys:
    print(k)

# values
values = scores.values()
for v in values:
    print(v)

scores = {"철수": 90, "민수": 85, "영희": 80}

items = scores.items()
print(items)
# 출력: dict_items([('민수', 85), ('영희', 80), ('철수', 90)])

# dict_items를 리스트로 변환할 때
# itemsList = list(items)

scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores.get("민수")  # 85
v = scores.get("길동")  # None
# v = scores["길동"]  # 에러 발생

# 멤버쉽연산자 in 사용
if "길동" in scores:
    print(scores["길동"])

scores.clear()  # 모두 삭제
print(scores)

persons = [("김기수", 30), ("홍대길", 35), ("강찬수", 25)]
mydict = dict(persons)

mydict.update({"홍대길": 33, "강찬수": 26})


"""
Set
"""
# set 정의
myset = {1, 1, 3, 5, 5}
print(myset)  # 출력: {1, 3, 5}

# 리스트를 set으로 변환
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)  # 출력: {'A', 'B'}

myset = {1, 3, 5}

# 하나만 추가
myset.add(7)
print(myset)

# 여러 개 추가
myset.update({4, 2, 10})
print(myset)

# 하나만 삭제
myset.remove(1)
print(myset)

# 모두 삭제
myset.clear()
print(myset)

a = {1, 3, 5}
b = {1, 2, 5}

# 교집합
i = a & b
# i = a.intersection(b)
print(i)

# 합집합
u = a | b
# u = a.union(b)
print(u)

# 차집합
d = a - b
# d = a.difference(b)
print(d)


"""
함수
"""


def sum(a, b):
    s = a + b
    return s


total = sum(4, 7)
print(total)


# 함수내에서 i, mylist 값 변경
def f(i, mylist):
    i = i + 1
    mylist.append(0)


k = 10  # k는 int (immutable)
m = [1, 2, 3]  # m은 리스트 (mutable)

f(k, m)  # 함수 호출
print(k, m)  # 호출자 값 체크


# 출력: 10 [1, 2, 3, 0]


def calc(i, j, factor=1):
    return i * j * factor


result = calc(10, 20)
print(result)


def report(name, age, score):
    print(name, score)


report(age=10, name="Kim", score=80)


def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot


t = total(1, 2)
print(t)
t = total(1, 5, 2, 6)
print(t)


def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot


count, sum = calc(1, 5, 2, 6)  # (count, tot) 튜플을 리턴
print(count, sum)


"""
모듈
"""
import math

n = math.factorial(5)
print(n)

# factorial 함수만 import
from math import factorial

n = factorial(5) / factorial(3)
print(n)

# 여러 함수를 import
from math import factorial, acos

n = factorial(3) + acos(1)
print(n)

# 모든 함수를 import
from math import *

n = sqrt(5) + fabs(-12.5)
print(n)

# factorial() 함수를 f()로 사용 가능
from math import factorial as f

n = f(5) / f(3)
print(n)
