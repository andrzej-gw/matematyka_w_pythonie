from random import*
p=0
q=0
while True:
    a=random()
    b=random()
    c=random()
    ok=False
    for _ in range(3):
        if (b+1-a)%1<=0.5 and (c+1-a)%1<=0.5:
            ok=True
            break
        d=c
        c=b
        b=a
        a=d
    if ok:
        p+=1
    q+=1
    if(q%1000000==0):
        print(p/q,p,q)
