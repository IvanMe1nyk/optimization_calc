import math

def func(n,f):
    x=n
    fx=eval(f)
    return fx

def Direc(f1,f2,dir):
    if dir=="max":
        if f1>=f2:
            return True
        else:
            return False
    elif dir=="min":
        if f1<=f2:
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

def alg(x,exp,f,dir):
    acc=list()
    lim=['-inf','inf']
    acc_temp="Початкові межі рівні +/- нескінченість: "+str(lim)
    acc.append(acc_temp)
    x0=x
    i=0
    acc_temp="Перевіряємо зміну значення функції в залежності від кроку та проводимо першу зміну межі:"
    acc.append(acc_temp)

    if func(x0-exp,f)<=func(x0,f)<=func(x0+exp,f):
        exp=exp*(-1)
        lim[1]=x
        acc_temp="Виконується умова: f(x-k) оптимальніша ніж f(x) та f(x) оптимальніша ніж f(x+k), нові межі матимуть такий вигляд: "+str(lim)
        acc.append(acc_temp)
    elif func(x0-exp,f)>=func(x0,f)>=func(x0+exp,f):
        exp=abs(exp)
        lim[0]=x
        acc_temp="Виконується рівність: f(x+k) оптимальніша ніж f(x) та f(x) оптимальніша ніж f(x-k), нові межі матимуть такий вигляд: "+str(lim)
        acc.append(acc_temp)
    else:
        lim[0]=x0-exp
        lim[1]=x0+exp
        acc_temp="Виконується умова: f(x) оптимальніша ніж f(x-k) та f(x) оптимальніша ніж f(x+k), нові межі матимуть такий вигляд: "+str(lim)
        acc.append(acc_temp)
    acc_temp="За умови що одна межа невизначена починаємо цикл для знаходження іншої межі, в іншому випадку цикл завершено"
    acc.append(acc_temp)
    while (type(lim[0])==str) or (type(lim[1])==str):
        x1=x0+exp*pow(2,i)
        acc_temp="Обчислюємо нову опорну точку, x_new="+str(x1)
        acc.append(acc_temp)
        acc_temp="Перевіряємо умову на зміну межі:"
        acc.append(acc_temp)
        if exp>0:
            if Direc(func(x1,f),func(x0,f),dir)==True:
                lim[0]=x1
                acc_temp="Виконується умова: f(x_new) оптимальніша ніж f(x) нові межі матимуть такий вигляд: "+str(lim)
                acc.append(acc_temp)
            else:
                lim[1]=x1
                acc_temp="Виконується умова: f(x) оптимальніша ніж f(x_new) нові межі матимуть такий вигляд: "+str(lim)
                acc.append(acc_temp)
        else:
            if Direc(func(x1,f),func(x0,f),dir)==True:
                lim[1]=x1
                acc_temp="Виконується умова: f(x_new) оптимальніша ніж f(x) нові межі матимуть такий вигляд: "+str(lim)
                acc.append(acc_temp)
            else:
                lim[0]=x1
                acc_temp="Виконується умова: f(x) оптимальніша ніж f(x_new) нові межі матимуть такий вигляд: "+str(lim)
                acc.append(acc_temp)
        x0=x1
        i=i+1
    acc_temp="Оптимальний інтервал невизначеності матиме межі: "+str(lim)
    acc.append(acc_temp)
    return acc
