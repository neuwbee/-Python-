aka = [4, 12, 20, 38, 56, 88]
print(aka[5])
print(aka[-1])
print(len(aka))
print(max(aka))
add = [1, 2, 3]
total = aka + add
print(total)
total.sort()
print(total)
total.sort(reverse=True)
print(total)
total[-1] = 4
print(total)
total.insert(3,19)
print(total)
total.pop(-1)
print(total)
total.remove(12)
print(total)

"""
리스트의 길이를 구하는 함수 : 

len(example)

리스트에 요소 추가하기 :

examlple.append(element)

리스트에 요소 삽입하기 : 

example.insert(index,element)

리스트에 요소 있는지 확인하기 :

print(element in example)

리스트안에서 요소의 위치 확인하기 : 

example.index(element)

리스트에서 요소 삭제하기 (pop) :

example.pop(index)

리스트에서 요소 삭제하기 (remove) :

example.remove(element)

리스트 오름차순 정렬 :

example.sort()

리스트 내림차순 정렬 :

example.sort(reverse=True)

리스트 최대 요소 찾기 : 

max(example)

리스트 최소 요소 찾기 : 

min(example)

리스트 위치에 있는 요소 꺼내기 :

example(index)

리스트 안에 있는 요소 수정하기 : 

example[index] = element

"""

"""

1. 복권 번호 6자리를 담은 리스트를 super_ball 라는 변수에 할당하라.
   복권 번호 6자리는 다음과 같다. 
   (45, 63, 12, 28, 8, 91)

2. 복권 번호 6자리에 숫자 (15, 37)을 추가한 후, 오름차순으로 정렬하여라

3. 복권 번호 (45)를 (27)로 수정하여라.

4. 복권 번호 4번째 자리와 5번째 자리에 있는 숫자 사이에 (84)를 넣어라

5. 복권 번호에서 가장 큰 수와 가장 작은 수를 구하고 큰수를 작은수로 나눈 몫을 구하여라.

6. 복권 번호 안의 요소의 개수를 구하여라.

7. 복권 번호 안에 (63)이 있는지 확인하고, 있다면 그 위치를 구하여라.

8. 복권 번호를 내림차순으로 정리하고, 2번째로 작은수를 삭제하는 함수를 두가지 방식으로 전개하라.

9. 복권 번호에서 마지막에서 2번째 있는 수를 음수로 표현하여 꺼내라.

10. Python 기본 문법
    정수 : 
    실수 :
    복소수 :
    문자열 :
    참, 거짓 : 
    순서가 있는 값들의 집합 : 
    읽기 전용 집합 : 
    중복되지 않는 값들의 집합 : 

11. 12의 4승에서 4의 12승을 뺀값의 절대값에서 23을 나눈 몫과 나머지를 구하시오

12. '14'와 34를 임의의 변수에 할당하고 결과값이 20이 되도록 출력해라.

13. a = 3을 프로그래밍적으로 해석해라

14. 변수 타입을 바꾸는 것을 표현한 용어를 적어라.


"""