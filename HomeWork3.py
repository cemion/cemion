
messeg = input("ведите строку: ")

if len(messeg) > 3:
    print("задача 1 -1 ", messeg[2:3])
else:
    print("задача 1 -1 длинна строки меньше 3 елементов")

# print("задача 1 -2 ", messeg[-2:-1])
# print("задача 1 -3 ", messeg[0:6])
# print("задача 1 -4 ", messeg[0:-3])
# print("задача 1 -5 ", messeg[2::2])
# print("задача 1 -6 ", messeg[1::2])
# print("задача 1 -7 ", messeg[::-1])
# print("задача 1 -8 ", messeg[::-2])
# print("задача 1 -9 ", len(messeg))
for i in range((len(messeg) + 1) // 2):
         messeg1 = messeg[1:] + messeg[0]
print("задача 2", messeg1)

i=0
print("задача 3-1")
while i < 10:
    i +=1
    print(i)

print("задача 3-2")
x=20
while x > 0:
    print(x)
    x -=1
print("задача 4-1")
while len(messeg) > 0:
    print(messeg)
    messeg = messeg[0:-1]
messeg =[1,2,3,4,5,(1,2,3)]
print("задача 4-2")
while len(messeg) > 0:
    print(messeg)
    messeg.pop(-1)
messegg = [1,5,6,7,5,5,8,7,6]
print("задача 4-3")
while len(messegg) > 1:
    messegg.sort()
    messegg.pop(-1)
    print(messegg)
stroka = ("We, are not what we should be!")
print("задача 4-4",len(stroka.split(' ')))
print("задача 4-5", stroka.replace(',', ''))
print("задача 4-6")
words = stroka.split()
qqq = words.sort()
for word in words:
     print(word)
print("задача 5-1")

def is_year_leap(year):
    if (not year % 4 and year % 100) or not year % 400:
        print('True')
    else:
        print('False')
is_year_leap(24)

def triangl(a,b,c):
    if  a + b <= c or a+c<=b or b+c<=a :
        print("задача 5-2", " False")
    else:
        print("задача 5-2", " True")
triangl(12,10,10)
def triangl_typ(a,b,c):
    if  a + b <= c or a+c<=b or b+c<=a :
         print("задача 6-1", " False")
    else:

         if a == b or a == c or b == c:
             print("задача 6-1", " равносторонний")
         elif a == b or b == c:
                  print("задача 6-1", " Равнобедренный")
         else:
                  print("задача 6-1", " Разносторонний")
triangl_typ(10,10,12)
def second(*args):


    x=list(set(args))
    x.sort()
    print("задача 7-1", x[1])
second(1,2,1,4,33,7,8,9)
def la_la_la(a=3,b=3,c=0):
    la = "la"
    stroka_la = (la+"-") * b
    stroka_la=stroka_la[0:-1]
    if c==1:
        stroka_la= stroka_la+"!\n"
    elif c==0:
        stroka_la = stroka_la + ".\n"
    print(stroka_la*a)
la_la_la(2,4,0)
