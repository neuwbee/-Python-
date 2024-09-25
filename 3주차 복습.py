"""
1. 리스트의 길이 = len()
    ex) letters = ['a', 'b', 'c', 'd']
        length_of_list = len(letters)
        print(length_of_list)

        >> 4
2. 리스트에 요소 추가하기 = append() -> 요소 중 맨 마지막에 추가됨
    ex) letters = ['a', 'b', 'c', 'd']
        letters.append('e')
        print(letters)

        >> ['a', 'b', 'c', 'd', 'e']

3. 리스트에 요소 삽입하기 = insert() -> (x,y) 꼴로 x자리에는 인덱스(위치), 
y 자리에는 값(요소)를 넣는다.
    ex) letters = ['a', 'b', 'c', 'd', 'e']
        letters.insert(0,'x')
        print(letters)

        >> ['x', 'a', 'b', 'c', 'd', 'e']

4. 리스트에 요소가 있는지 확인하기 = 'in' 연산자 사용하기
    ex) alphabet= ['a','b','c','d']
        print('a' in alphabet)

        >> True

5. 리스트 안에서 요소의 위치를 확인할때 = index() 사용하기
    ex) alphabet= ['a','b','c','d']
        index_b = alphabet.index('b')
        print(index_b)

        >> 2

6. 리스트에서 요소 삭제하기 = pop() -> (x)꼴일때, x에 삭제하고 싶은 인덱스(위치)를 넣어라
    ex) alphabet= ['a','b','c','d']
        alphabet.pop(0)
        print(alphabet)

        >> 'a'

7. 리스트에서 요소 삭제하기 = remove() -> (x)꼴일때, x에 삭제하고 싶은 값(요소)를 넣어라
    ex) alphabet= ['a','b','c','d']
        alphabet.remove('a')
        print(alphabet)

        >> ['b','c','d']

8. 리스트 정렬 = sort()함수 (오름차순 정리)
    ex) list = [10,7,1,2,3,4,5]
        list.sort()
        print(list)

        >>[1, 2, 3, 4, 5, 7, 10]

9. 리스트 정렬 = sort()함수에 reverse = True인자를 넣어준다
    ex) list = [10,7,1,2,3,4,5]
        list.sort(reverse=True)
        print(list)

        >>[10, 7, 5, 4, 3, 2, 1]

10. 리스트 안에 들어있는 요소의 최대/최소값 찾기 = max(), min() 사용하기
    ex) number_list=[1,2,3,4,5,6,7,8,9,10]
        max_number = max(number_list)
        min_number = min(number_list)
        print(max_number)
        print(min_number)

        >> 10
        >> 1

11. 리스트에서 인덱스(위치)를 통해 요소 꺼내기 = 리스트 안에 들어가있는 순서를 알면 그 값을 꺼내올수 있다.
    양수 indexing - 처음 0 부터 시작하여 차례로 1씩 커짐
    음수 indexing - 마지막 수가 -1부터 차례로 음수로 내려옴
        ex) alphabet= ['a','b','c','d']

            print(alphabet[0])
            print(alphabet[-1])

            >> a
            >> d

12. 리스트에서 인덱스를 통해 요소값 수정
    리스트에 들어가 있는 값을 수정하려면 그 값의 인덱스에 새로운 값을 할당해줘야한다.
        ex) alphabet= ['a','b','c','d']
            alphabet[1]='k'

            print(alphabet)

            >> ['k', 'b','c','d']

13. 조건문의 기본 구조 = if 다음에 조건절이 오는 구문으로 참 거짓의 boolean 형태로 결과가 출력된다.
    ex) a=3
        b=7

        if a>b:
            print("a is bigger than b")
        else:
            print("a is not bigger than b")
            
        >> a is not bigger than b

14. 조건이 여러개로 중첩될 때에는 if.. elif*<조건 횟수> .. else의 형태를 사용한다
    ex) if< 조건문 >:  
            < 실행할 명령문1 >    
            < 실행할 명령문2 >    
        elif < 조건문 >  
            < 실행할 명령문1 >  
            < 실행할 명령문2 >
        elif < 조건문 >
            < 실행할 명령문1 >  
            < 실행할 명령문2 >
        else:
            < 실행할 명령문1 >  
            < 실행할 명령문2 >

"""
# Quiz
#1. 6가지 알칼리 토급속의 원자 번호를 담은 리스트를 akaline_earth_metals라는 변수에 할당하라. 
# 6가지 알칼리 토금속과 원자 번호는 다음과 같다. 
# 베릴륨(4), 마그네슘(12), 칼슘(20), 스토론튬(38), 바륨(56), 라듐(88)
 
akaline_earth_metals = [4, 12, 20, 38, 56, 88]

#2. 라듐의 원자 번호를 담은 인덱스는 무엇인가? 
# 해답은 두 가지 방식으로 하나는 양수 인덱스로, 나머지 하나는 음수 인덱스로 써라.

print(akaline_earth_metals [5])
print(akaline_earth_metals [-1])

#3. akaline_earth_metals 리스트에 들어 있는 항목의 수를 알려주는 함수는 무엇인가?

print(len(akaline_earth_metals))

#4. akaline_earth_metals에서 가장 큰 원자 번호를 반환하는 코드를 작성하라

print(max(akaline_earth_metals))

#5. 추가적으로, 3가지의 원자 번호를 담은 리스트를 addition_atoms 에 할당해라. 
# 3가지 원자 번호는 다음과 같다. 수소(1), 헬륨(2), 리튬(3)
 
addition_atoms = [1,2,3]

#6. akaline_earth_metals 와 addition_atoms를 합쳐서 하나의 total_atoms라는 리스트를 만들어라

print(akaline_earth_metals)
print(addition_atoms)
print(akaline_earth_metals+addition_atoms)
total_atoms = akaline_earth_metals+addition_atoms
print(total_atoms)

#7. 작은 원자 번호가 앞에 오도록 total_atoms를 정렬해라.

total_atoms.sort()
print(total_atoms)

#8. 큰 원자 번호가 앞에오도록 total_atoms를 정렬해라.

total_atoms.sort(reverse=True)
print(total_atoms)

#9. total_atoms에서 수소(1)를 베릴륨(4)으로 바꾸어라.

total_atoms[-1] = 4
print(total_atoms)

#10. total_atoms의 3번째 원소와 4번째 원소 사이에 칼륨의 원자번호(19)를 넣어라.

total_atoms.insert(3,19)
print(total_atoms)

#11. total_atoms 마지막 요소를 제거해라.

total_atoms.pop(-1)
print(total_atoms)

#12. total_atoms에서 마그네슘(12)을 제거해라.  

total_atoms.remove(12)
print(total_atoms)

#13. (조건문을 활용) 몸무게와 키를 할당하는 변수를 만든 뒤, 
# 과체중인지, 정상 체중인지, 저체중인지 문구를 출력해주는 코드를 작성해라. 
# (적정체중 구하는 공식 = (키-100) * 0.9)

a = 180
b = 72
if (a-100)*0.9 < b:
    print("과체중")
elif (a-100)*0.9 == b:
    print("정상체중")
else:
    print("저체중")

#14. 조건문을 활용) 몸무게를 할당하는 변수 하나를 선언하고 임의의 몸무게를 할당한 뒤, 
# 아래 UFC 체급 기준표를 활용하여 해당 변수의 UFC 체급을 산출하는 코드를 작성해라.
"""
체급
몸무게 (kg)
플라이급
~57
벤텀급
~61.2
페더
~65.8
라이트
~70.3
웰터급
~77.1
미들
~83.9
라이트헤비
~93
헤비
~120.2
"""
a= 120
if a< 57:
    print("플라이")
elif a<61.2:
    print("밴텀")
elif a<65.8:
    print("페더")
elif a<70.3:
    print("라이트")
elif a<77.1:
    print("웰터")
elif a<83.9:
    print("미들")
elif a<93:
    print("라이트헤비")
elif a<120.2:
    print("헤비")
else:
    print("무제한급")
