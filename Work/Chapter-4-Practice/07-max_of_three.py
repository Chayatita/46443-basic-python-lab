a = int(input())
b = int(input())
c = int(input())

if a > b or a > c :
    print(a)
elif b > c or b > a :
    print(b)
elif c > a or c > b :
    print(c)