# a,b 각 변수에 들어있는 값을 표현하는 코드를 구현하시오
# a,b 변수에 들어있는 값은 100, 200 이다

# [1] 변수 선언 및 값 할당
a=100
b=200
print(a, b)

# [2] temp 변수를 사용한 swap
temp=a
a=b
b=temp
print(a, b)

# 별도의 temp 변수를 생성하지 않고 한줄로 코드를 작성해 교환하시오

# [1] 변수 선언 및 값 할당
a=100
b=200
print(a, b)

# [2] temp 변수를 사용하지 않고 swap
a, b=b, a
print(a, b)
