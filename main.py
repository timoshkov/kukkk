

#Задание 1
a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")


#Задание 2
meaning = [5,8,9,7,3,2,4,1,6]
meaning2 = 1
while meaning2 < len(meaning):
     for i in range(len(meaning)-meaning2):
          if meaning[i] > meaning[i+1]:
               meaning[i],meaning[i+1] = meaning[i+1],meaning[i]
     meaning2 += 1
print(meaning)


#Задание 3
def names(cur):
    most = cur[0]
    for i in range(1, len(cur)):
     if cur[i] > most:
      most = cur[i]
    return most
list = [1,2,3,4,5,6,7,8,9,10]
mostel = names(list)
print(mostel)


#Задание 4
def name(a):
    if a == 1 or a == 2:
        return 1
    return name(a - 1) + name(a - 2)
b = int(input())
print(name(b))


#Задание 5
s= ['tshhs','stdhsth','tshhs']
c=0
a=0
for i in s:
  if s.count(i)>=c:
   c=s.count(i)
a=i
print(a)