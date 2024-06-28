from zespolone import*
tracer(0)
rysuj_siatke()
#rysuj_osie()
a=3
b=4
c=6
d=8
A=Zespolona(0,0)
B=Zespolona(c,0)
C=przeciecie(Okrag(A,b),Okrag(B,a))[0]

P=przeciecie(Okrag(A,d),Okrag(B,d))[1]
Q=przeciecie(Okrag(A,d/c*b),Okrag(C,d/c*b))[0]
R=przeciecie(Okrag(C,d/c*a),Okrag(B,d/c*a))[1]


rysuj_odcinek(A,B)
rysuj_odcinek(B,C)
rysuj_odcinek(C,A)
rysuj_odcinek(A,P)
rysuj_odcinek(B,P)
rysuj_odcinek(A,Q)
rysuj_odcinek(C,Q)
rysuj_odcinek(B,R)
rysuj_odcinek(C,R)

A.rysuj("A","blue")
B.rysuj("B","blue")
C.rysuj("C","blue")
P.rysuj("P","blue")
Q.rysuj("Q","blue")
R.rysuj("R","blue")

input()
