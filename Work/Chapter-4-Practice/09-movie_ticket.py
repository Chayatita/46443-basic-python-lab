age = int(input())
weeks = int(input())
t = 0

if age < 13 :
    t = 100
    if weeks == 6 or weeks == 7 :
        print((t) + 50)
elif (13 < age <= 180) :
    t = 180
    if weeks == 6 or weeks == 7 :
        print(t + 50)
elif t == 60 :
    t = 120
    if weeks == 6 or weeks == 7 :
        print((t) + 50)
else :
    print(t)