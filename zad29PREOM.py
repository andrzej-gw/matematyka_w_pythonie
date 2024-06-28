from zespolone import*
tracer(0)
A=Zespolona(-5,-3)
B=Zespolona(5,-3)
C=Zespolona(-2,7)

Ap=rzut(A,Prosta(B,C))
Bp=rzut(B,Prosta(C,A))
Cp=rzut(C,Prosta(A,B))


rysuj_odcinek(A,B)
rysuj_odcinek(B,C)
rysuj_odcinek(C,A)
rysuj_odcinek(A,Ap)
rysuj_odcinek(B,Bp)
rysuj_odcinek(C,Cp)

A.rysuj("A","blue")
B.rysuj("B","blue")
C.rysuj("C","blue")
Ap.rysuj("A'","blue")
Bp.rysuj("B'","blue")
Cp.rysuj("C'","blue")



input()
