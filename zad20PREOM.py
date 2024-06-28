from zespolone import*
from time import*
tracer(0)
#tracer(1)
#speed(0)

for alpha in range(0,360):
    alfa=alpha/12
    #rysuj_siatke()
    #rysuj_osie()
    A=Zespolona(-10,-10)
    B=Zespolona(10,-10)
    C=wielokat_foremny(A,B,3)[2]
    p1=Prosta(A,obrot(B,A,rad_to_zesp(degree_to_rad(alfa))))
    #p1.rysuj()
    p2=Prosta(B,obrot(A,B,rad_to_zesp(degree_to_rad(alfa-30))))
    #p2.rysuj()
    P=przeciecie(p1,p2)

    Ap=obrot(A,C,rad_to_zesp(degree_to_rad(60)))
    Bp=obrot(B,C,rad_to_zesp(degree_to_rad(60)))
    Cp=obrot(C,C,rad_to_zesp(degree_to_rad(60)))
    Pp=obrot(P,C,rad_to_zesp(degree_to_rad(60)))





    rysuj_odcinek(A,B)
    rysuj_odcinek(B,C)
    rysuj_odcinek(C,A)
    rysuj_odcinek(A,P)
    rysuj_odcinek(B,P)
    rysuj_odcinek(C,P)

    rysuj_odcinek(Ap,Bp,"cyan")
    rysuj_odcinek(Bp,Cp,"cyan")
    #rysuj_odcinek(Cp,Ap,"cyan")
    rysuj_odcinek(Ap,Pp,"cyan")
    rysuj_odcinek(Bp,Pp,"cyan")
    rysuj_odcinek(Cp,Pp,"cyan")

    rysuj_odcinek(P,Pp,"red")

    A.rysuj("A","blue")
    B.rysuj("B","blue")
    C.rysuj("C","blue")
    P.rysuj("P","blue")

    #Ap.rysuj("A'","cyan")
    Bp.rysuj("B'","cyan")
    #Cp.rysuj("C'","cyan")
    Pp.rysuj("P'","cyan")

    tracer(1)
    sleep(0.01)
    clear()
    tracer(0)
