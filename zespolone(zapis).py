#To do list:
#styczne <- przecinanie sie okregow i prostych <- okrag jako klasa
#inwersja prostych i okregow i odcinkow
#jednokladnosc prostych i okregow i odcinkow
#rysowanie funkcji
from turtle import*
from math import*
class Zespolona:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        if self.y==0:
            return str(self.x)
        if self.x!=0:
            res=str(self.x)
        else:
            res=""
        if self.y>0 and self.x!=0:
            res+='+'
        elif self.y<0:
            res+='-'
        if abs(self.y)!=1:
            res+=str(abs(self.y))
        res+="i"
        return res
    #def __call__(self):
    #    print (str(self.x)+"+"+str(self.y)+"i")
    def rysuj(self,nazwa=None,kolor="black"):
        pu()
        goto(self.x*skala,self.y*skala)
        pd()
        color(kolor)
        dot(10)
        fd(5)
        pu()
        if nazwa!=None:
            write(nazwa)
        home()
    def sprzezenie(self):
        return Zespolona(self.x,-self.y)
    def __abs__(self):
        return sqrt(self.x**2+self.y**2)
    
    def __eq__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return self.x==other.x and self.y==other.y
    def __ne__(self,other):
        return not self==other
    def __add__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return Zespolona(self.x+other.x,self.y+other.y)
    def __radd__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return Zespolona(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return Zespolona(self.x-other.x,self.y-other.y)
    def __rsub__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return Zespolona(other.x-self.x,other.y-self.y)
    def __mul__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return Zespolona(self.x*other.x-self.y*other.y,self.x*other.y+other.x*self.y)
    def __rmul__(self,other):
        if not isinstance(other, Zespolona):
            other=Zespolona(other,0)
        return Zespolona(self.x*other.x-self.y*other.y,self.x*other.y+other.x*self.y)
    def __truediv__(self,other):
        if isinstance(other,Zespolona) and other.y==0:
            other=other.x
        if not isinstance(other, Zespolona):
            if self.x%other==0:
                a=self.x//other
            else:
                a=self.x/other
            if self.y%other==0:
                b=self.y//other
            else:
                b=self.y/other
            return Zespolona(a,b)
        return (self*other.sprzezenie())/(other*other.sprzezenie())
    def __rtruediv__(self,other):
        tmp=self
        self=other
        other=tmp
        if isinstance(other,Zespolona) and other.y==0:
            other=other.x
        if not isinstance(other, Zespolona):
            if self.x%other==0:
                a=self.x//other
            else:
                a=self.x/other
            if self.y%other==0:
                b=self.y//other
            else:
                b=self.y/other
            return Zespolona(a,b)
        return (self*other.sprzezenie())/(other*other.sprzezenie())
    def __pow__(self,other):
        if isinstance(other, Zespolona) and other.y==0:
            other=other.x
        res=1
        for i in range(other):
            res*=self
        for i in range(-other):
            res/=self
        return res
    def __rpow__(self,other):
        tmp=self
        self=other
        other=tmp
        if isinstance(other, Zespolona) and other.y==0:
            other=other.x
        res=1
        for i in range(other):
            res*=self
        for i in range(-other):
            res/=self
        return res
    def __pos__(self):
        return self
    def __neg__(self):
        return 0-self
    def __invert__(self):
        self.y*=-1
        return self
class Prosta:
    def __init__(self,A=None,B=None,a=None,b=None):
        if a!=None:
            self.a=a
            self.b=b
            return
        if A==B:
            print("Ten sam punkt.")
            A/=0
        if (B-A).x==0:
            self.a=696969
            self.b=A.x
            return
        if (B-A).y%(B-A).x==0:
            self.a=(B-A).y//(B-A).x
        else:
            self.a=(B-A).y/(B-A).x
        self.b=A.y-A.x*self.a
    def __str__(self):
        if self.a==0:
            return str(self.b)
        res=""
        if self.a<0:
            res+="-"
        if abs(self.a)!=1:
            res+=str(abs(self.a))
        res+="x"
        if self.b==0:
            return res
        if self.b>0:
            res+="+"
        res+=str(self.b)
        return res
    def rysuj(self,kolor="black",grubosc=3):
        pu()
        color(kolor)
        pensize(grubosc)
        if self.a==696969:
            goto(self.b*skala,-wysokosc/2)
            pd()
            goto(self.b*skala,wysokosc/2)
            pu()
            home()
            return
        if self.a==0:
            goto(-szerokosc/2,self.b*skala)
            pd()
            goto(szerokosc/2,self.b*skala)
            pu()
            home()
            return
        if -szerokosc/skala/2*self.a+self.b>wysokosc/skala/2:
            y1=wysokosc/skala/2
            x1=(y1-self.b)/self.a
        elif -szerokosc/skala/2*self.a+self.b<-wysokosc/skala/2:
            y1=-wysokosc/skala/2
            x1=(y1-self.b)/self.a
        else:
            x1=-szerokosc/skala/2
            y1=x1*self.a+self.b
        goto(x1*skala,y1*skala)
        pd()
        if szerokosc/skala/2*self.a+self.b>wysokosc/skala/2:
            y1=wysokosc/skala/2
            x1=(y1-self.b)/self.a
        elif szerokosc/skala/2*self.a+self.b<-wysokosc/skala/2:
            y1=-wysokosc/skala/2
            x1=(y1-self.b)/self.a
        else:
            x1=szerokosc/skala/2
            y1=x1*self.a+self.b
        goto(x1*skala,y1*skala)
        pu()
        home()
class Okrag:
    def __init__(self,O,r):
        self.O=O
        self.r=r
    def __str__(self):
        return "O: "+str(self.O)+" r: "+str(self.r)
    def rysuj(self,kolor="black",grubosc=3):
        pu()
        goto((self.O+self.r).x*skala,(self.O+self.r).y*skala)
        pd()
        lt(90)
        color(kolor)
        pensize(grubosc)
        circle(self.r*skala)
        pu()
        home()
skala=50
szerokosc=2600
wysokosc=1400
def zmien_skale(x):
    global skala
    skala=x
def rysuj_osie():
    pd()
    pensize(2)
    color("black")
    fd(szerokosc/2)
    bk(szerokosc)
    fd(szerokosc/2)
    lt(90)
    fd(wysokosc/2)
    bk(wysokosc)
    fd(wysokosc/2)
    rt(90)
    write(" 0")
    for i in range(szerokosc//2//skala):
        fd(skala)
        rt(90)
        fd(2)
        bk(4)
        fd(2)
        lt(90)
        write(" "+str(i+1))
    home()
    for i in range(szerokosc//2//skala):
        bk(skala)
        rt(90)
        fd(2)
        bk(4)
        fd(2)
        lt(90)
        write(str(-i-1))
    home()
    lt(90)
    for i in range(wysokosc//2//skala):
        fd(skala)
        rt(90)
        fd(2)
        write(" "+str(i+1))
        bk(4)
        fd(2)
        lt(90)
    home()
    lt(90)
    for i in range(wysokosc//2//skala):
        bk(skala)
        rt(90)
        fd(2)
        write(str(-i-1))
        bk(4)
        fd(2)
        lt(90)
    home()
def rysuj_siatke():
    pd()
    pensize(1)
    color('lightgrey')
    for i in range(szerokosc//2//skala):
        fd(skala)
        lt(90)
        fd(wysokosc/2)
        bk(wysokosc)
        fd(wysokosc/2)
        rt(90)
    home()
    for i in range(szerokosc//2//skala):
        fd(-skala)
        lt(90)
        fd(wysokosc/2)
        bk(wysokosc)
        fd(wysokosc/2)
        rt(90)
    home()
    lt(90)
    for i in range(wysokosc//2//skala):
        fd(skala)
        rt(90)
        fd(szerokosc/2)
        bk(szerokosc)
        fd(szerokosc/2)
        lt(90)
    home()
    lt(90)
    for i in range(wysokosc//2//skala):
        bk(skala)
        rt(90)
        fd(szerokosc/2)
        bk(szerokosc)
        fd(szerokosc/2)
        lt(90)
    home()
def rysuj_odcinek(A,B,kolor="black",grubosc=3):
    color(kolor)
    pensize(grubosc)
    pu()
    goto(A.x*skala,A.y*skala)
    pd()
    goto(B.x*skala,B.y*skala)
    pu()
    home
def rysuj_okrag(O,R,kolor="black",grubosc=3):
    pu()
    goto((O+R).x*skala,(O+R).y*skala)
    pd()
    lt(90)
    color(kolor)
    pensize(grubosc)
    circle(R*skala)
    pu()
    home()
def przeciecie(a,b):
    if isinstance(a,Prosta) and isinstance(b,Prosta):
        if a==b:
            print("Te same proste.")
            a=5/0
        if a.a==b.a:
            print("Nie przecinaja sie.")
            a=5/0
        return Zespolona((b.b-a.b)/(a.a-b.a),(a.a*b.b-a.b*b.a)/(a.a-b.a))
    if isinstance(a,Okrag) and isinstance(b,Okrag):
        o1=a
        o2=b
        #sprawdzic czy sie w ogole przecinaja lub styczne
        if o1==o2:
            print("Te same okręgi.")
            a=5/0
        if abs(o2.O-o1.O)>o1.r+o2.r: #rozlaczne zewnetrznie
            return []
        if o1.r<o2.r:
            tmp=o1
            o1=o2
            o2=tmp
        if o1.r>abs(o2.O-o1.O)+o2.r: #rozlaczne wewnetrznie
            return []
        if abs(o2.O-o1.O)==o1.r+o2.r: #styczne zewnetrznie
            return [(o1.O+o2.O)/2]
        if o1.r>abs(o2.O-o1.O)+o2.r: #styczne wewnetrznie
            return [(o2.O-o1.O)/abs(o2.O-o1.O)*o1.r+o1.O]
        a=o1.r
        b=o2.r
        c=abs(o1.O-o2.O)
        alpha=acos((a*a+b*b-c*c)/(2*a*b))
        P1=(o2.O-o1.O)*alpha/abs(o2.O-o1.O)*o1.r+o1.O
        P2=(o2.O-o1.O)*(-alpha)/abs(o2.O-o1.O)*o1.r+o1.O
        return [P1,P2]
	if isinstance(a,Prosta) and isinstance(b,Okrag):
		tmp=a
		a=b
		b=tmp
    if isinstance(a,Okrag) and isinstance(b,Prosta):
		o=a
        p=b
        d=odleglosc_punktu_od_prostej(o.O,p)
        if d==o.r:
			return [rzut(o.O,p)]
		if d>o.r:
			return []
		if d<o.r:
			M=rzut(o.O,p)
			a=sqrt(o.O*o.O-d*d)
			P1=(o.O-M)*Zespolona(0,1)*a/d+M
			P2=(o.O-M)*Zespolona(0,-1)*a/d+M
			return [P1,P2]
    print("Jeszcze nie umiemy przecinac innych rzeczy niz proste i okregi.")
    a=5/0
def kat(A,B,C):
    A-=B
    C-=B
    A/=abs(A)
    C/=abs(C)
    C/=A
    return C
def zesp_to_rad(z):
    if z.x==0 and z.y==0:
        print("Nie da sie wyznaczyc kata.")
        z=5/0
    if z.y!=0:
        return 2*atan(z.y/(sqrt(z.x**2+z.y**2)+z.x))
    return pi
def rad_to_degree(alpha):
    return alpha/(2*pi)*360
def degree_to_rad(alpha):
    return alpha/360*2*pi
def rad_to_zesp(alpha):
    return Zespolona(cos(alpha),sin(alpha))
def obrot(A,O,kat):
    return (A-O)*kat+O
def symetralna_odcinka(A,B):
    M=(A+B)/2
    return Prosta(M,obrot(A,M,rad_to_zesp(pi/2)))
def srodek_okregu_opisanego(A,B,C):
    #print(((C.y-A.y)*(abs(B)**2-abs(A)**2)-(B.y-A.y)*(abs(C)**2-abs(A)**2))/2*((B.x-A.x)*(C.y-A.y)-(C.x-A.x)*(B.y-A.y)))
    p1=symetralna_odcinka(A,B)
    p2=symetralna_odcinka(A,C)
    return przeciecie(p1,p2)
def promien_okregu_opisanego(A,B,C):
    O=srodek_okregu_opisanego(A,B,C)
    return abs(O-A)
def okrag_opisany(A,B,C):
    return Okrag(srodek_okregu_opisanego(A,B,C),promien_okregu_opisanego(A,B,C))
def pole_trojkata(A,B,C):
    A-=C
    B-=C
    return abs(A.x*B.y-A.y*B.x)/2
def pole_wielokata(wierzcholki):
    res=0
    for i in range(1,len(wierzcholki)-1):
        res+=pole_trojkata(wierzcholki[0],wierzcholki[i],wierzcholki[i+1])
    return abs(res)
def prosta_rownolegla(A,p):
    if p.a==696969:
        p.b=A.x
        return p
    p.b=A.y-A.x*p.a
    return p
def prosta_prostopadla(A,p):
    if p.a==0:
        p1=Prosta(a=696969,b=A.x)
    elif p.a==696969:
        p1=Prosta(a=0,b=A.y)
    else:
        p1=Prosta(a=-1/p.a,b=A.y+A.x/p.a)
    return p1
def rzut(A,p):
    p1=prosta_prostopadla(A,p)
    return przeciecie(p,p1)
def odleglosc_punktu_od_prostej(A,p):
    return abs(A-rzut(A,p))
def odbicie(A,p):
    S=rzut(A,p)
    return S+S-A
def dwusieczna(A,B,C):
    if C!=None:
        G=obrot(A,B,rad_to_zesp(zesp_to_rad(kat(A,B,C))/2))
        return Prosta(G,B)
##    p1=A
##    p2=B
##    if p1==p2:
##        print("To ta sama prosta.")
##        p1=5/0
##    if p1.a==p2.a:
##        print("Proste sa rownolegle.")
##        p1=5/0
##    if p1.b==696969:
##        tmp=p1
##        p1=p2
##        p2=tmp
##    if p1.a==696969:    
def srodek_okregu_wpisanego(A,B,C):
    p1=dwusieczna(A,B,C)
    p2=dwusieczna(A,C,B)
    return przeciecie(p1,p2)
def promien_okregu_wpisanego(A,B,C):
    o=srodek_okregu_wpisanego(A,B,C)
    return abs(o-rzut(o,Prosta(A,B)))
def okrag_wpisany(A,B,C):
    return Okrag(srodek_okregu_wpisanego(A,B,C),promien_okregu_wpisanego(A,B,C))
def wielokat_foremny(A,B,n):
    z=rad_to_zesp(degree_to_rad(360/n))
    res=[A,B]
    for i in range(n-2):
        C=(B-A)*z+B
        res.append(C)
        A=B
        B=C
    return res
def jednokladnosc(A,O,k):
    return (A-O)*k+O

# tracer(0)
# rysuj_siatke()
# rysuj_osie()
# A=Zespolona(-14,4)
# B=Zespolona(1,1)
# C=Zespolona(1,-4)
# rysuj_odcinek(A,B)
# rysuj_odcinek(B,C)
# rysuj_odcinek(A,C)
# o1=okrag_opisany(A,B,C)
# o1.rysuj("red",2)
# symetralna_odcinka(A,B).rysuj("red",2)
# symetralna_odcinka(A,C).rysuj("red",2)
# symetralna_odcinka(C,B).rysuj("red",2)
# o1.O.rysuj("O","red")
# A.rysuj("A","blue")
# B.rysuj("B","blue")
# C.rysuj("C","blue")
# dwusieczna(A,B,C).rysuj("green")
# dwusieczna(A,C,B).rysuj("green")
# o2=okrag_wpisany(A,B,C)
# o2.rysuj("green",2)
# o2.O.rysuj("o","green")
