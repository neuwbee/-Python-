
y = 0
a = []
while True:
   i = int(input("숫자를 입력하시오."))
   a.append(i)
   
   y+=i
    
   if i==0:
      break
a.pop(-1)
print(a)
print(y)

q = int(input("숫자의 개수를 입력하시오. : "))
w = 0
r = 0
e = []
for i in range(q):
   w=int(input("숫자를 입력하시오. : "))
   r+=w
   e.append(w)
print(e)
print(r/q)

a =[]
list_0 = [1, 2, 3, 4, 5]
for i in list_0:
   a.append(i**2)
print(a)



   
   

    