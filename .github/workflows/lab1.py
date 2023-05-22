import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b**2 - 4*a*c #считаем дискриминант

if discriminant > 0: #если дискриминант > 0

    x1 = (-b + math.sqrt(discriminant)) / (2*a) #первый корень
    x2 = (-b - math.sqrt(discriminant)) / (2*a) #второй корень
    print("Корни уравнения: ", x1, x2)
elif discriminant == 0: #если дискриминант = 0
    x = -b / (2*a)
    print("Корни уравнения: ", x)
else: #дискриминант меньше нуля
    discr = -b / (2*a)  
    cron = math.sqrt(-discriminant) / (2*a)
    print("Корни уравнения: ", complex(discr, cron), complex(discr, -cron))
