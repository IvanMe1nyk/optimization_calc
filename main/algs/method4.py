import math
import random

def StrInLis(strin):
    lis=[]
    strin=strin+','
    while strin.count(',')>0:
        k=strin.index(',')
        temp=float(strin[0:k:])
        lis.append(temp)
        strin=strin[k+1::]
    return lis


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
        
def Add(a,b):
    c=list()
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

def Min(a,b):
    c=list()
    for i in range(len(a)):
        c.append(a[i]-b[i])
    return c

def Mod(lis):
    temp=0
    for i in range(len(lis)):
        temp=temp+lis[i]**2
    temp=math.sqrt(temp)
    return temp

def Mult(a,b):
    c=list()
    for i in range(len(b)):
        c.append(a*b[i])
    return c


sin=math.sin
cos=math.cos
tan=math.tan
Pi=math.pi
'''
dir="min"
f="2*x[0]**2+x[0]*x[1]+x[1]**2"
n=4
x=list()
x_old='0.5,1'
y=list()
z=list()
alpha=1
beta=0.5
M=300
N=100
t=1
R=0.001
'''
def alg(x_old,f,n,alpha,beta,M,N,t,R,dir):
    x_old=StrInLis(x_old)
    k=0
    j=0
    acc=list()
    eps=list()
    x=x_old
    f_x=eval(f)
    while True:
        acc_temp="k="+str(k)+", j="+str(j)
        acc.append(acc_temp)
        for i in range(n):
            eps.append((random.random()*2)-1)
        acc_temp="Створимо масив випадкових значень: "+str(eps)
        acc.append(acc_temp)
        y=Add(x,Mult(t,Mult(1/Mod(eps),eps)))
        acc_temp="Обчислимо нове значення для y: "+str(y)
        acc.append(acc_temp)
        eps=list()
        x=y
        f_y=eval(f)
        if Direc(f_y,f_x,dir)==True:
            z=Add(x,Mult(alpha,Min(y,x)))
            x=z
            acc_temp="Оскільки нове значення оптимальніше, ніж старе, обчислимо нове значення для z: "+str(z)
            acc.append(acc_temp)
            f_z=eval(f)
            if Direc(f_z,f_x,dir)==True:
                t=t*alpha
                k=k+1
                x_old=x
                acc_temp="Оскільки значення функції в точці z оптимальніше, ніж в точці x, зберігаємо це значення та обчислюємо нове значення величини кроку"
                acc.append(acc_temp)
                acc_temp="Перевіряємо умову завершення алгоритму: при k<N=>j=1, в іншому випадку алгоритм завершено"
                acc.append(acc_temp)
                if k<N:
                    j=1
                else:
                    break
                continue
        acc_temp="Нова опорна точка матиме координати: "+str(x)+", та значення функції в даній точці: "+str(eval(f))
        acc.append(acc_temp)
        x=x_old
        acc_temp="Перевіряємо умову завершення алгоритму: при j<M=>j=j+1, в іншому випадку проводиться додаткова перевірка"
        acc.append(acc_temp)
        if j<M:
            j=j+1
        elif j==M:
            acc_temp="Перевіряємо умову завершення алгоритму: при t>R=>j=1 та переобчислюється розмір кроку, в іншому випадку проводиться алгоритм завершується"
            acc.append(acc_temp)
            if t<=R:
                break
            else:
                t=t*beta
                j=1
        f_x=eval(f)
    acc_temp="Нова оптимальна точка матиме координати: "+str(x)+", та значення функції в даній точці: "+str(eval(f))
    acc.append(acc_temp)    
    return acc
