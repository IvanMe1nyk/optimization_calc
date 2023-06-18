import math

def func(n,f):
    x=n
    fx=eval(f)
    return fx

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

a=-100
b=100
exp=0.001
f='x**2'
dir='min'
def alg(a,b,exp,f,dir):
    acc=list()
    z1=0.382
    z2=1-z1
    while abs(b-a)>exp:
        x1=a+z1*(b-a)
        x2=a+z2*(b-a)
        acc_temp='Обчислюємо значення функції в точці: x1='+str(x1)+', f(x1)='+str(func(x1,f))
        acc.append(acc_temp)
        acc_temp='Обчислюємо значення функції в точці: x2='+str(x2)+', f(x2)='+str(func(x2,f))
        acc.append(acc_temp)
        acc_temp='Виконуємо перевірку: '
        acc.append(acc_temp)
        if Direc(func(x2,f),func(x1,f),dir)==True:
            acc_temp='Якщо f(x2) оптимальніше ніж f(x1), то ліва межа пересувається в х1, х1 в х2, а х2 переобчислюється'
            acc.append(acc_temp)
            a=x1
            x1=x2
            x2=a+z2*(b-a)
        else:
            acc_temp='Якщо f(x1) оптимальніше ніж f(x2), то права межа пересувається в х2, х2 в х1, а х1 переобчислюється'
            acc.append(acc_temp)
            b=x2
            x2=x1
            x1=a+z1*(b-a)
        acc_temp='Нові межі відрізка: a='+str(a)+', b='+str(b)
        acc.append(acc_temp)
    acc_temp='Нова оптимальна точка: x='+str((b+a)/2)+', f(x)='+str(func((b+a)/2,f))
    acc.append(acc_temp)
    return acc

