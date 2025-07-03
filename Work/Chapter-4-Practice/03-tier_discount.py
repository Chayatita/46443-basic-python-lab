H = float(input()) 

if H >= 2000 :
    print (H - (H*0.15))
elif 2000 > H >= 1000 :
    print (H - (H*0.10))
elif 1000 > H >= 500 :
    print (H - (H*0.05))
else :
    print(H)