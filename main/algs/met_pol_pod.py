import math

def Direc(f1,f2,dir):
    if dir=="max":
        if f1>f2:
            return True
        else:
            return False
    elif dir=="min":
        if f1<f2:
            return True
        else:
            return False
        
sin=math.sin
cos=math.cos
tan=math.tan
Pi=math.pi
e=math.e
exp=math.exp
sqrt=math.sqrt
pow=math.pow

def alg(a,b,exp,f,dir):
    acc=list()
    x_m=(b+a)/2
    x=x_m
    f_m=eval(f)
    while abs(b-a)>exp:
        acc_temp='Обчислимо значення функції на середині відрізку: x='+str(x_m)+', f='+str(f_m)
        acc.append(acc_temp)
        x1=a+(b-a)/4
        x=x1
        f1=eval(f)
        x2=b-(b-a)/4
        x=x2
        f2=eval(f)
        acc_temp='Обчислимо значення функції на першій четверті відрізку: x='+str(x1)+', f='+str(f1)
        acc.append(acc_temp)
        acc_temp='Обчислимо значення функції на третій четверті відрізку: x='+str(x2)+', f='+str(f2)
        acc.append(acc_temp)
        acc_temp='Проведемо перевірку:'
        acc.append(acc_temp)
        if Direc(f1,f_m,dir)==True:
            acc_temp='Якщо значення на першій четверті оптимальніше ніж на середині, то права межа зміщуєть до середини відрізку'
            acc.append(acc_temp)
            b=x_m
            x_m=x1
        elif Direc(f2,f_m,dir)==True:
            acc_temp='Якщо значення на третій четверті оптимальніше ніж на середині, то ліва межа зміщуєть до середини відрізку'
            acc.append(acc_temp)
            a=x_m
            x_m=x2
        else:
            acc_temp='Якщо значення на середині відрізку оптимальніше ніж на першій та третій четверті, то права межа зміщуєть до третьої четверті, а ліва до першої'
            acc.append(acc_temp)
            a=x1
            b=x2
        acc_temp='Новий відрізок: a='+str(a)+', b='+str(b)
        acc.append(acc_temp)
    x=(a+b)/2        
    acc_temp='Оптимальне значення на відрізку: x='+str(x)+', f(x)='+str(eval(f))
    acc.append(acc_temp)
    return acc