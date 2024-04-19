import datetime

char_a = "5"
int_a = 5

"""기본적으로 {} 포맷팅의 특성을 그대로 가짐"""
print(1234567890)
print(f"{char_a:>5}")  # >는 오른쪽정렬
print(f"{char_a:<5}")  # <는 왼쪽정렬
print(f"{char_a:^5}")  # ^는 가운데정렬
print(f"{int_a:0<5}")  # <는 왼쪽정렬, 빈자리를 0으로 채울수도 있음

print(1234567890)
print(f"{int_a:>10f}")  # >는 오른쪽정렬, 정수를 넣어도 f로 포맷팅하면 실수로 표현
print(
    f"{int_a:^10.2f}"
)  # ^는 가운데정렬, 10을 썼으니 10자리 기준 가운데 정렬, 소수점 2자리 감안해서 가운데 정렬

date = datetime.date(1978, 1, 18)
print(f"{date} was on a {date:%A}")
print(f"{date:%b %d, %Y}")
