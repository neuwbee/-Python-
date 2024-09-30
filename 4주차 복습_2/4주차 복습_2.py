#구구단
i = 1
while i<9:
    i+=1
    print(str(i)+'단')
    y = 0
    while y<9:
        y+=1
        print(str(i)+'*'+str(y)+'='+str(i*y))

num = 1
for i in range(1,9,1):
    num+=1
    print(str(num)+'단')
    num_2 = 0
    for y in range(1,10,1):
        num_2+=1
        print(str(num)+'*'+str(num_2)+'='+str(num*num_2))

num = int(input("숫자를 입력하시오."))

total_num=0
i=0

while i<=num:
    total_num+=i
    
    print(total_num)
    i+=1

num = int(input("숫자의 개수를 입력하시오."))
rev = 0

for i in range(num):
    





i = int(input("숫자를 입력하세요. : "))
y = 0
while i:
    y+=int(input("숫자를 입력하시오. : "))
    if i==0: break