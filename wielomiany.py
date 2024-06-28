def wartosc_wielomianu(a,b):
    result=0
    pom=1
    for i in a:
        result+=i*pom
        pom*=b
    return result
def print_wielomian(a):
    p=True
    for i in range(len(a)-1,-1,-1):
        if(a[i]==a[i]//1):
            a[i]=int(a[i])
        if(a[i]!=0):
            if(p):
                p=False
                if(a[i]<0):
                    print("-",end="")
            else:
                if(a[i]>0):
                    print("+",end="")
                else:
                    print("-",end="")
            if(abs(a[i])!=1 or i==0):
                print(str(abs(a[i])),end="")
            if(i>1):
                print("x^"+str(i),end="")
            elif(i==1):
                print("x",end="")
    if(p):
        print("0",end="")
def wielomian(s):
    s=s.split("+")
    for i in range(len(s)):
        s[i]=s[i].split("-")
    result=[]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(len(s[i][j])==0):
                continue
            if(j==0):
                znak=1
            else:
                znak=-1
            pom=s[i][j].split("x")
            if(len(pom)==1):
                p=0
                a=int(pom[0])*znak
            else:
                if(pom[0]==""):
                    a=znak
                else:
                    a=int(pom[0])*znak
                if(pom[1]==""):
                    p=1
                else:
                    p=int(pom[1][1:])
            while(len(result)<=p):
                result.append(0)
            result[p]+=a
    return result
def dodawanie_wielomianow(a,b):
    result=[]
    i=0
    while(i<len(a) or i<len(b)):
        result.append(0)
        if(i<len(a)):
            result[i]+=a[i]
        if(i<len(b)):
            result[i]+=b[i]
        i+=1
    #print("dodawanie",a,b,result)
    while(len(result)>0 and result[len(result)-1]==0):
        del result[len(result)-1]
    return result
def mnozenie_wielomianow(a,b):
    result=[]
    for i in range(len(a)+len(b)):
        result.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i+j]+=a[i]*b[j]
    return result
def zlozenie_wielomianow(a,b):
    result=[]
    for i in range(len(a)+len(b)):
        result.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i*j]+=a[i]*(b[j]**i)
    return result
def dzielenie_wielomianow(a,b):
    q=[]
    while(len(a)>=len(b)):
        p=[]
        for i in range(len(a)-len(b)):
            p.append(0)
        p.append(a[len(a)-1]/b[len(b)-1])
        q=dodawanie_wielomianow(q,p)
        a=dodawanie_wielomianow(a,mnozenie_wielomianow([-1],mnozenie_wielomianow(p,b)))
        #print("dzielenie")
        #print_wielomian(q)
        #print_wielomian(a)
        #print()
    return (q,a)
def nwd_wielomianow(a,b):
    if(len(b)>len(a)):
        c=a
        a=b
        b=c
    #print("nwd",a,b)
    if(b==[]):
        for i in range(len(a)):
            a[i]*=1/a[len(a)-1]
        return a
    return nwd_wielomianow(dzielenie_wielomianow(a,b)[1],b)
def szukaj_pierwiastkow_wymiernych(f,precision=0.0001):
    L=[]
    ul=[]
    a0=abs(f[0])
    an=f[len(f)-1]
    for i in range(1,a0+1):
        if(a0%i==0):
            for j in range(1,an+1):
                if(an%j==0):
                    L.append([-i/j,1])
                    L.append([i/j,1])
                    ul.append([i,j])
                    ul.append([-i,j])
    #print(L)
    #print(ul)
    pier=[]
    i=0
    while(i<len(L)):
        if(len(f)<=1):
            break
        r=dzielenie_wielomianow(f,L[i])[1]
        ok=True
        for j in r:
            if(abs(j)>precision):
                ok=False
        if(ok):
            pier.append([-L[i][0],ul[i][0],ul[i][1]])
            f=dzielenie_wielomianow(f,L[i])[0]
        else:
            i+=1
    for i in range(len(pier)):
        if(pier[i][0]==pier[i][0]//1):
            pier[i][0]=int(pier[i][0])
    for i in pier:
        print("(x-"+str(i[0]),end=")")
    if(len(f)==1 and f[0]!=1):
        print("*("+int(f[0])+")")
    if(len(f)>1):
        print("*(",end="")
        print_wielomian(f)
        print(")")
    else:
        print("")
    return [pier,f]
print("""Witaj w prostym kalkulatorze wielomianow:
Jest on dopiero w fazie testow, wiec moze posiadac bledy, jesli na jakis
natrafisz to najlepiej mnie poinformuj (jedrekgwiazda@gmail.com).

Program zapisuje wielomiany w postaci list, w ktorych na i-tym miejscu trzymany
jest wspolczynnik stojacy przy x^i. Mozesz korzystac z tej surowej formy, albo
uzyc funkcji print_wielomian(a), ktora jako argument przyjmuje wielomian w
postaci listy i wypisuje \"normalny\"(np. print_wielomian([1,0,5,-1]) => "-x^3+5x^2+1"). Dostepna jest takze funkcja wielomian,
ktora jako parametr przyjmuje napis, ktory jest \"normalny\" i zwraca go w postaci
listy (np. wielomian("-x^3+5x^2+1") => [1, 0, 5, -1])""")
