# is 연산자 (결과: [T/F])
# 두 객체가 동일한 주소에 할당된 객체임을 확인할때 사용
# 같은 데이터 값이더라도 다르게 생성된 객체이면 False 츨력

# [1]
a=[1,2,3,4,5]
b=a
c=[1,2,3,4,5]

# [2]
print('[2-1] a is b =' a is b)   #---True--;;
print('[2-2] a is c =' a is c)   #---False--;;

# [3]
a='korea'
print(a, id(a))   

b='korea'
print(b, id(b))
print(a is b)   #---True--;;

b+='!'
print(b, id(b))
print(a is b)   #---False--;;

c=b[:1]
print(c, id(c))
print(a is c)   #---True--;;


# == 연산자 (결과: [T/F])
# 오브젝트의 데이터 값이 같은지 확인할 때 사용

# [1]
a=[1,2,3,4,5]
b=a
c=[1,2,3,4,5]

# [2]
print('a==b=' a==b)   #---True--;;
print('b==c=' b==c)   #---True--;;
print('c==a='c==a)    #---True--;;


# [summary] 
# is 연산자 := 같은 객체를 가르키는가?
# == 연산자 := 데이터의 값이 같은가?


# is 연산자 vs. == 연산자

# [1] 숫자
a=101
b=100+1
print(a is b)  #---True--;;
print(a==b)  #---Ture--;;

# [2] 문자열
c='korea'
d='korea'
print(c is d)  #---True--;;
print(c==d)  #---True--;;

# [3] 리스트
e=[1,2,3,4,5]
f=[1,2,3,4,5]
print(e is f)  #---False--;;
print(e==f)  #---True--;;

# [summary] 숫자 or 문자(열)은 메모리를 효율적으로 사용하기 위해 새로운 할당 공간을 만들지 않음
# but 리스트는 새로운 공간 생성
print(id(e), id(f)) #---두 개 다름--;;
