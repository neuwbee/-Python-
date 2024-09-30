list_1 = ['a', 'b', 'c', 'd']
list_2 = list(range(0,4,1))

for alphbet in list_1:
    for index in list_2:
        print(index, alphbet)

a=0
b=0
while a<10:
    print(a+b)
    b=b+a
    a = a+1

list_1 = 0
for i in range(1,10,2):
    list_1=list_1+i
    print(list_1)


i = 1
while i<9:
    i+=1
    print(str(i)+'단')
    y = 1
    while y<10:
        print(str(i)+'*'+str(y)+'='+str(i*y))
        
        y+=1

list_1 = 1
for i in range(1,9,1):
    list_1 = list_1+1
    print(str(list_1)+'단')
    
    list_2 = 1
    for y in range(1,10,1):
        print(str(list_1)+'*'+str(list_2)+'='+str(list_1*list_2))
        list_2=list_2+1


i = 1
while i<9:
    i+=1
    print(str(i)+'단')
    y=1
    while y<10:
        print(str(i)+'*'+str(y)+'='+str(i*y))
        y+=1

lunch_list = ['국밥', '돈까스', '김치찌개', '쌀국수', '햄버거']
i = 0
while i<len(lunch_list):
    print(lunch_list[i])
    i+=1

num = 1
for i in range(1,9,1):
    num+=1
    print(str(num)+'단')
    
    num_2 = 1
    for y in range(1,10,1):
        print(str(num)+'*'+str(num_2)+'='+str(num*num_2))  
    
        num_2+=1








    
    


    
