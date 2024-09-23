money = False
if money :
    print("택시를 타고 가라")
else : 
    print("걸어가라")

""""
 비교 연산자 응용 
x < y	x가 y보다 작다.
x > y	x가 y보다 크다.
x == y	x와 y가 같다.
x != y	x와 y가 같지 않다.
x >= y	x가 y보다 크거나 같다.
x <= y	x가 y보다 작거나 같다.
"""
# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않음녀 걸어가라.
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
    print("택시가 없으면 기차를 타라")
else:
    print("버스를 타라")

""""
x or y : x와 y 둘 중 하나만 참이어도 참이다.
x and y : x와 y 모두 참이어야 참이다.
not x :	x가 거짓이면 참이다.
"""

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않다면 걸어가라.

money = 4000
card = True
if money >= 3000  or card:
    print("택시를 타고가라")
else: 
    print("걸어가라")
    

 








