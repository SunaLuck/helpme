import math

def lab_fn(a,b,c):
    d=float(b*b - 4*a*c)
    if d<0:
        return (int(0),float(0),float(0))
    else:
        x_1=float((b+math.sqrt(d))/(2*a))
        x_2=float((b-math.sqrt(d))/(2*a))
        return (int(1),x_1,x_2)

print("Введите параметры уравнения ax^2 + bx + c:")
a=float(input("Введите a:\n"))
b=float(input("Введите b:\n"))
c=float(input("Введите c:\n"))
has_roots,x_1,x_2 = lab_fn(a,b,c)
if has_roots==0:
    print("Уравнение не имеет корней")
else:
    print("Корни уравнения {a}*x^2 + {b}*x + {c} это {x_1} и {x_2}")