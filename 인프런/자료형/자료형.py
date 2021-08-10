# 자료형
# 많은 데이터 타입 중 -> 프로그램을 코딩하는데 여러 데이터 타입을 사용해 정보 처리
# 이때, 데이터 타입을 구분해야함 -> 자료형을 통해 구분

# [1] 숫자형-정수(int)
a=100
print(a, type(a))   #---100,<class'int'>--;;

# [2] 숫자형-실수(float)
b=3.14
print(b, type(b))   #---3.14,<class'float'>--;;

# [3] 문자형(str)
c='korea'
print(c, type(c))   #---korea,<class'str'>--;;
d='010-1234-5678'
print(d, type(d))   #---010-1234-5678,<class'str'>--;;

# [4] 리스트형(list)
lst=[1,2,3,4,5]
print(lst, type(lst))   #---[1,2,3,4,5],<class'list'>--;;

# [5] 튜플형(tuple)
tpl=(1,2,3,4,5)
print(tpl, type(tpl))   #---(1,2,3,4,5),<class'tuple'>--;;

# [6] 집합형(set)
s={1,2,3,4,5}
print(s, type(s))   #---{1,2,3,4,5},<class'set'>--;;

# [7] 딕셔너리(사전)형(dict)
dic={'a':97, 'b':98}
print(dic, type(dic))   #---{'a':97, 'b':98}--;;

# '[4] 리스트형'은 중복이 가능하지만 '[6] 집합형'은 중복이 불가능하다. 

lst=[1,2,3,4,5,5]
s={1,2,3,4,5,5}
print(lst, s)   #---[1,2,3,4,5,5], {1,2,3,4,5}--;;
