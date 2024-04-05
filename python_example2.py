#기본 데이터 타입

#1. Python 기본 데이타 타입
#파이썬에 사용되는 기본 데이타 타입(Scalar Data Type)에는 아래와 같은 타입들이 있다.

#타입	설명	표현 예
#int	정수형 데이타	100, 0xFF (16진수), 0o56 (8진수)
#float	소숫점을 포함한 실수	a = 10.25
#bool	참, 거짓을 표현하는 부울린	a = True
#None	Null과 같은 표현	a = None
#정수형은 소숫점을 갖지 않는 정수를 갖는 데이타 타입이며, float는 소숫점을 갖는 데이타 타입이다. bool 타입은 True 혹은 False 만을 갖는 타입이고, None은 아무 데이타를 갖지 않는다는 것을 표현하는 것으로 타 언어의 Null과 같은 개념이다. 정수형에 리터럴 데이타를 넣을 때, 10진수 이외에 16진수 혹은 8진수를 위의 예와 같이 사용할 수 있다.

#리터럴 데이타를 특정 타입으로 변경하기 위하여 int(), float(), bool() 등과 같은 타입 생성자를 사용할 수 있다. 예를 들어, int(3.5)는 float 데이타를 정수형으로 변경하여 정수값 3 을 리턴한다. float("1.6")은 float형 1.6을 리턴한다.

int(3.5)      # 3
2e3           # 2000.0
float("1.6")  # 1.6
float("inf")  # 무한대
float("-inf") # -무한대
bool(0)       # False. 숫자에서 0만 False임,
bool(-1)      # True
bool("False") # True
a = None      # a는 None
a is None     # a가 None 이므로 True

#위의 예제에서 리터럴 2e3 (혹은 2E3 도 같은 표현)은 2 * (10 ** 3)과 같은 표현이다. 또한, bool 타입은 숫자의 경우 0 만이 거짓이 되고, 0이 아니면 참이 된다. bool() 안에 문자형이나 컬렉션 타입들이 있을 경우 비어있으면 거짓이 되고 값이 있으면 참이된다. 즉, 위의 마지막 예인 bool("False")는 문자열이 비어있지 않으므로 참이 된다.


#2. 복소수
#파이썬은 복소수 타입을 지원하는데, 복소수는 a+bj 와 같이 표현된다 (수학에서 복소수를 표현할 때 i 를 사용하지만 파이썬에서는 j 를 사용한다). 실수부의 값을 얻기 위해서는 복소수 변수명.real을, 허수부의 값을 얻기 위해선 변수명.imag 를 사용한다.

v = 2 + 3j
v.real  # 2
v.imag  # 3


#연산자
#파이썬은 산술연산자, 비교연산자, 할당연산자, 논리연산자, Bitwise 연산자, 멤버쉽연산자, Identity연산자를 지원한다.

#1. 산술연산자
#산술연산자에는 (1) 사칙연산자 +, -, *, / 와 (2) 제곱을 나타내는 **, (3) 나머지를 산출하는 % (Modulus), 그리고 (4) 나누기에 소숫점 이하를 버리는 // 연산자(Floor Division) 등이 있다.

5 % 2   # 1
5 // 2  # 2

#2. 비교연산자
#비교연산자는 관계연산자로도 불리우는데, 여기에는 등호(==), 같지 않음(!=), 부등호(<, >, <=, >=) 등이 있다.

if a != 1:
   print("1이 아님")

#3. 할당연산자
#할당연산자는 변수에 값을 할당하기 위하여 사용되는데, 기본적으로 = (Equal Sign)을 사용한다. 산술연산자와 함께 사용되어 할당을 보다 간결히 하기 위해 사용되는 +=, -=, *=, /=, %=, //= 등과 같은 연산자도 할당연산자에 해당된다.

a = a * 10
a *= 10     # 위와 동일한 표현

#4. 논리연산자
#논리연산자에는 and, or, not 이 있는데, and 는 양쪽의 값이 모두 참인 경우만 참이 되고, or 는 어느 한쪽만 참이면 참이된다. not 은 참이면 거짓으로 거짓이면 참이 된다. 아래 예제는 No가 출력된다.

x = True
y = False

if x and y:
    print("Yes")
else:
    print("No")

#5. Bitwise 연산자
#Bitwise연산자에는 & (AND), | (OR), ^ (XOR), ~ (Complement), <<, >> (Shift)가 있는데, 이 연산자는 비트단위의 연산을 하는데 사용된다.

a = 8     # 0000 1000
b = 11    # 0000 1011
c = a & b # 0000 1000  (8)
d = a ^ b # 0000 0011  (3)

print(c)
print(d)

#6. 멤버쉽 연산자
#멤버쉽연산자에는 in, not in 이 있는데, 이는 좌측 Operand가 우측 컬렉션에 속해 있는지 아닌지를 체크한다.

a = [1,2,3,4]
b = 3 in a    # True
print(b)

#7. Identity 연산자
#Identity연산자에는 is, is not 이 있는데, 이는 양쪽 Operand가 동일한 Object를 가리키는지 아닌지를 체크한다.

a = "ABC"
b = a
print(a is b)  # True


#문자열과 바이트
#1. 문자열
#파이썬에서 문자열은 단일인용부호(') 혹은 이중인용부호(") 를 사용하여 표현한다.
#예를 들어, 아래 표현은 s 라는 변수에 가나다 라는 문자열을 할당하는 것으로 동일한 표현이다.

s = '가나다'
s = "가나다"

#만약 여러 라인에 걸쳐 있는 문자열을 표현하고 싶다면, ''' 또는 """ 처럼 3개의 인용부호를 사용한다.

s = '''아리랑
아리랑
아라리요
'''
print(s)

#복수 라인 문자열을 한 라인으로 표현하고 싶다면, Escape Sequence (\n#)를 사용하면 된다. 즉, 다음 표현은 위와 동일한 표현이다.

#실제 리눅스나 Mac OS에서는 Newline이 \n#으로 표현되지만, 윈도우즈에서 \r\n#을 사용한다. 하지만, 파이썬에서는 Universal Newline이 지원되어 모든 OS에서 공히 \n#을 사용한다.

s = '아리랑\n#아리랑\n#아라리요'
print(s)

#물론 문자열에서 사용되는 Escape Sequence에는 타 언어와 비슷하게 여러 가지를 사용할 수 있다. 예를 들어 탭은 \t, 이중따옴표는 \", 백슬래쉬는 등과 같이 표현한다.

#문자열 포맷팅
#일정한 포맷에 맞춰 문자열을 조합하는 것을 문자열 포맷팅이라하는데, 문자열 포맷 탬플릿 안에 대입값이 들어갈 자리를 지정해 두고 나중에 그 값을 채워 넣는 방식이다. 예를 들어, "답: %s" % "A" 와 같은 표현에서 % 앞 부분은 포맷 템플릿이고, % 뒤는 실제 대입할 값이다. 이때 % 를 포맷팅 연산자 (Formatting Operator)라 부른다. % 앞뒤로 각각 하나의 값만을 받아들이므로 만약 % 뒤의 값이 복수 개이면 튜플로 묶어주어야 한다.

p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)
# 출력: 이름: 김유신 나이: 65

p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
print(p)
# 출력: X = 3.142, Y =       3.14

#% (Formatting Operator) 앞의 포맷 템플릿에는 %s, %d 등과 같이 대입값 형식을 지정해 주는데 이를 변환 지시어(Conversion Specifier)라 부른다. 아래 표는 Conversion Specifier 들의 의미를 설명한 것이다.

#Conversion Specifier	의미
#%s	문자열 (파이썬 객체를 str()을 사용하여 변환)
#%r	문자열 (파이썬 객체를 repr()을 사용하여 변환)
#%c	문자(char)
#%d 또는 %i	정수 (int)
#%f 또는 %F	부동소수 (float) (%f 소문자 / %F 대문자)
#%e 또는 %E	지수형 부동소수 (소문자 / 대문자)
#%g 또는 %G	일반형: 값에 따라 %e 혹은 %f 사용 (소문자 / 대문자)
#%o 또는 %O	8진수 (소문자 / 대문자)
#%x 또는 %X	16진수 (소문자 / 대문자)
#%%	% 퍼센트 리터럴

#Conversion Specifier는 % 와 Conversion 문자(예: s, d, f) 사이에 전체 자릿수와 소숫점 뒤자리수를 지정할 수 있다. 예를 들어 %10.2f 는 전체 10자리이고 값이 적으면 앞에 빈칸을 채우게 되고, .2 는 소수점 2째 자리까지만 표시한다는 것을 의미한다. 만약 %-10.2f 처럼 마이너스로 표현하면 전체 10자리인데 왼쪽으로 정렬한다는 의미이다.

#2. str (문자열 클래스)
#문자열은 내부적으로 str 이라는 클래스 타입인데, 파이썬의 문자열은 기본적으로 유니코드이고, 한번 설정되면 다시 변경시킬 수 없는 Immutable 타입이다.

#문자열은 인덱스를 사용하여 문자열 중 특정위치의 문자를 표현할 수 있다. 인덱스는 0로부터 시작하는데, 문자열 s 에 대하여 첫번째 문자는 s[0], 두번째 문자는 s[1] 과 같이 표현된다.

s = "ABC"
type(s)      # class 'str'
v = s[1]     # B
type(s[1])   # class 'str'

#파이썬에는 C, C# 등에서 존재하는 문자(char) 타입이 존재하지 않는다. 따라서, 위의 예에서 s[1]의 타입이 char가 아닌 문자열 str 타입이 된다. 참고로 type(변수명)은 해당 변수의 타입을 리턴한다.

#문자열을 표현할 때, r'문자열' 과 같이 사용하면, 이는 Escape Sequence를 표현하지 않고 Raw String을 직접 사용한다는 것을 의미한다. 예를 들어, 윈도우즈에서 파일경로를 간략히 표현하기 위해 아래와 같이 Raw String 표현을 사용할 수 있다.

path = r'C:\Temp\test.csv'
print(path)

#3. 자주 사용되는 str 메서드
#문자열 str 클래스에는 여러 유용한 메서드들이 제공되고 있는데, 이 중 흔히 사용되는 몇가지만 소개한다.

#str.join()
#우선 여러 개의 문자열을 하나로 결합하는 join() 메서드가 있는데, join() 메서드는 문자열을 결합하는데 사용되는 Separator를 join 메서드 앞에 사용한다. 아래 예제에 보듯이, 콤마를 사용하여 문자열 리스트 요소들을 결합할 수도 있으며, 또한 빈 문자열을 사용하여 문자열들을 결합하는 방법도 자주 사용된다.

s = ','.join(['가나','다라','마바'])
print(s)
# 출력: 가나,다라,마바

s = ''.join(['가나','다라','마바'])
print(s)
# 출력 : 가나다라마바

#str.split()
#split() 메서드는 join() 메서드의 반대로서 특정 separator를 기준으로 문자열을 분리하여 리스트를 리턴한다. 아래 예제에서 split() 메서드는 하나의 문자열을 콤마로 분리해서 3개의 요소를 갖는 리스트를 리턴한다.

items = '가나,다라,마바'.split(',')
print(items)
# 출력 : ['가나', '다라', '마바']

#str.partition()
#partition() 메서드는 문자열을 partition() 메서드의 첫번째 파라미터로 분리하여 그 앞부분(prefix), partition 분리자(separator), 뒷부분 (suffix) 등 3개의 값을 Tuple로 리턴한다. 아래 예제는 Dash (-) 로 문자열을 분리하여 3개의 값을 리턴하는 코드이다. 일반적으로 separator는 사용하지 않아서 _ 를 사용하였다.

departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)
# 출력 : Seattle

#str.format()
#마지막으로 str 클래스에서 가장 많이 사용되는 메서드 중의 하나로 format() 메소드를 들 수 있다. format() 메서드는 다양한 방식의 문자열 포맷팅을 지원하는데, 아래는 흔히 사용되는 3가지 방식을 예시하고 있다. 먼저 위치를 기준으로한 포맷팅은 {0},{1},... 등의 필드들을 format() 파라미터들의 순서대로 치환하게 된다. 두번째 필드명을 기준으로 한 포맷팅은 {name}, {age}와 같이 임의의 필드명을 지정하고 format() 파라미터에 이들 필드명을 사용하여 값을 지정하는 것이다. 그리고 세번째 인덱스 및 키 사용 방식은 Python 오브젝트가 format()의 파라미터로 지정되고, 포맷에서 이 오브젝트의 인덱스(컬렉션의 경우) 혹은 속성, 키 등을 이용하는 것이다.

# 위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)  #출력: Name: 강정수, Age: 30

# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s) #출력: Name: 강정수, Age: 30

# object의 인덱스 혹은 키를 사용하여 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s) #출력: width: 10, height: 20

#4. bytes (바이트 클래스)
#bytes 클래스는 일련의 바이트들을 표현하는 클래스로서 bytes는 한번 설정되면 다시 변경할 수 없는 Immutable 타입이다. 문자열을 바이트로 표현하기 위해 b'문자열' 와 같이 접두어 b를 앞에 붙인다.

#문자열을 바이트들로 변경하는 인코딩을 위해 encode()를 사용한다. 반대로 바이트들을 문자열로 변경하는 디코딩을 위해 decode()를 사용한다. 문자열 안에서 유니코드값을 사용하려면, \u 에 이어 유니코드값을 적으면 된다. 아래 예제는 문자열 s1을 UTF-8 인코딩을 사용하여 바이트들로 변경하고, 이를 다시 문자열로 디코딩하는 예제이다.


#조건문 : if
#파이썬에서 조건문을 사용하기 위하여 if 문을 사용한다. if 키워드 다음에 조건식을 적게 되고, 조건식 다음에 콜론(:) 을 써서 if 조건식 끝을 표현한다 (if문은 한 라인에 모두 쓸 수 있으므로 문법상 조건식 뒤에 콜론 사용).

if x < 10:
    print(x)
    print("한자리수")

# 한 라인에서 표현된 if 문 
if x < 100:    print(x)

#if 문 조건식이 참이 아닐 때, 다음 if 문을 체크하기 위해서 elif 문을 사용할 수 있고, 모든 if 문이 거짓일 때 else 문 블럭을 실행할 수 있다. 아래 예제는 if...elif...else 를 모두 사용한 예이다. 파이썬에는 다른 언어에 있는 switch 문이 존재하지 않으므로, switch 문 기능은 if...elif...elif... 문으로 수행한다.

x = 10
if x < 10:
    print("한자리수")
elif x < 100:
    print("두자리수")
else:
    print("세자리 이상")

#if 조건문 안에서 특정 블럭/문장을 수행하지 않고 그냥 Skip하기 위하여 pass 라는 키워드를 사용할 수 있다. 아래 예제는 n 이 10보다 작은 경우는 아무 문장도 실행하지 않고 지나가고, 10보다 크거나 같을 때는 n 값을 출력한다.

if n < 10:
    pass
else:
    print(n)

#반복문
#1. 반복문 : while
#파이썬에서 반복되는 루프를 만들기 위해 while 문이나 for 문을 사용할 수 있다. 먼저 while문은 while 키워드 다음의 조건식이 참일 경우 계속 while 안의 블력을 실행한다. 예를 들어, 아래의 예제를 보면 while의 조건식은 i가 10보다 작거나 같은 경우인데, i 값이 이 조건하에 있으면 계속 루프를 돌게 된다. 따라서, 아래 예제는 1부터 10까지 값을 출력하게 된다.

i=1
while i <= 10:
    print(i)
    i += 1

#2. 반복문 : for
#반복문 for는 C#, Java 에서의 foreach 와 비슷한 것으로, 컬렉션으로부터 하나씩 요소(element)를 가져와, 루프 내의 문장들을 실행하는 것이다. 리스트, Tuple, 문자열 등의 컬렉션은 "for 요소변수 in 컬렉션" 형식에서 in 뒤에 놓게 된다.

#아래 예제는 0부터 10까지를 더하는 코드이다. 파이썬 내장함수인 range(n) 함수는 0 부터 n-1 까지의 숫자를 갖는 리스트를 리턴한다. for 루프는 이 리스트 컬렉션으로부터 요소를 하나씩 가져와서 for 블럭의 문장을 실행하게 된다.

sum = 0
for i in range(11):
    sum += i
print(sum)

#아래 예제는 문자열 요소를 갖는 리스트로부터 각 문자열들을 순차적으로 출력하는 예이다.

list = ["This", "is", "a", "book"]
for s in list:
    print(s)

#for 루프는 이 밖에도 리스트 안에 내포되어 사용될 수도 있는데, 이는 리스트 컬렉션 편에서 자세히 설명한다.

#3. break / continue
#반복문 안에서 루프를 빠져나오기 위해 break 문을 사용할 수 있다. 또한, continue문을 사용하면 루프 블럭의 나머지 문장들을 실행하지 않고 다음 루프로 직접 돌아가게 할 수 있다. 아래 예제는 break와 continue문을 사용 예시를 위한 것으로, i가 5인 경우는 continue가 실행되어 직접 다시 while문으로 이동하여 밑의 합계에 포함되지 않는다. 또한, i가 10보다 큰 경우 while 루프를 빠져나오게 된다. 따라서, 이 예제는 1부터 10까지 합을 구하는데, 5인 경우만 제외한 값 즉 50을 출력한다.

i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue
    if i > 10:
        break
    sum += i

print(sum)

#4. range
#반복문과 직접적인 연관은 없지만, 흔히 반복문과 연동되어 많이 사용되는 range에 대해 간략히 소개한다. range() 함수는 보통 아래와 같이 1~3개의 파라미터를 갖는데, 파라미터는 파라미터 갯수에 따라 아래와 같이 다른 의미를 갖는다.

#예제	파라미터 의미	리턴값
#range(3)	Stop	0, 1, 2
#range(3,6)	Start, Stop	3, 4, 5
#range(2,11,2)	Start, Stop, Step	2, 4, 6, 8, 10

numbers = range(2, 11, 2)

for x in numbers:
    print(x)

# 출력: 각 라인에 2 4 6 8 10 출력

#특히, for 반복문에서 몇 번 루프를 도는가를 표시하기 위해 range() 함수를 종종 함께 사용한다. 예를 들어, 아래는 Hello 문자열을 10번 (0부터 9까지) 출력하는 예제이다.

for i in range(10):
    print("Hello")
