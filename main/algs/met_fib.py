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
        
def fib(k):
    k1=k2=1
    for i in range(k):
        k3=k1+k2
        k1=k2
        k2=k3
    if k!=0 and k!=1:
        return k3
    else:
        return 1


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
    for i in range(exp):
        acc_temp="Крок "+str(i)
        acc.append(acc_temp)
        x1=(fib(exp-1-i)/fib(exp+1-i))*(b-a)+a
        x2=(fib(exp-i)/fib(exp+1-i))*(b-a)+a
        acc_temp="Обчислюємо значення x_1= "+str(x1)
        acc.append(acc_temp)
        acc_temp="Обчислюємо значення x_2= "+str(x2)
        acc.append(acc_temp)
        acc_temp="Проводимо перевірку:"
        acc.append(acc_temp)
        if Direc(func(x1,f),func(x2,f),dir)==True:
            a=a
            b=x2
            acc_temp="Оскільки значення функції в точці x_1 оптимальніше ніж в точці x_2, нові межі матимуть такий вигляд: ("+str(a)+", "+str(b)+")"
            acc.append(acc_temp)
        else:
            a=x1
            b=b
            acc_temp="Оскільки значення функції в точці x_2 оптимальніше ніж в точці x_1, нові межі матимуть такий вигляд: ("+str(a)+", "+str(b)+")"
            acc.append(acc_temp)
    acc_temp="Новий інтервал невизначеності матиме такий вигляд: ("+str(a)+", "+str(b)+")"
    acc.append(acc_temp)
    acc_temp="Оптимальної точкою буде середина інтервалу x="+str((b+a)/2)+", та значення функції в цій точці f(x)="+str(func((b+a)/2,f))
    acc.append(acc_temp)
    return acc