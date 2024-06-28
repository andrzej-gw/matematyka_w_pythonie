def f(x):
    return ((2-x)/(2+x))**(1/5)
def pochodna(x,dx):
    return (f(x+dx)-f(x))/(dx)
