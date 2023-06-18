import math


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

def Poshuk(x_old,p,exp,f,dir):
    x=x_old
    for i in range(len(p)):
        if p[i]!=0:
            n=i
            break
    e=abs(p[n])
    f_old=eval(f)
    while exp<e:
        x[n]=x[n]+e
        f_new=eval(f)
        if Direc(f_new,f_old,dir)==False:
            x[n]=x[n]-2*e
            f_new=eval(f)
            if Direc(f_new,f_old,dir)==False:
                x[n]=x[n]+e
                e=e/2
            elif Direc(f_new,f_old,dir)==True:
                f_old=f_new
        elif Direc(f_new,f_old,dir)==True:
            f_old=f_new
            if f_new==f_old:
                x[n]=x[n]-e
                e=e/2
    return x


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

def Test(x_new ,x_old):
    temp=0
    for i in range(len(x_new)):
        temp=temp+(x_old[i]-x_new[i])**2
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
e=math.e
exp=math.exp
sqrt=math.sqrt
pow=math.pow
'''
dir="min"
f="4*(x[0]-5)**2+(x[1]-6)**2+(x[2]-7)**2+(x[3]-8)**2"
n=4
e=0.1
y=list()
x_old='9,9,10,11'
x_new=list()
p=list()'''
def alg(x_old,f,n,e,dir):
    acc=list()
    p=list()
    y=list()
    x_old=StrInLis(x_old)
    iterator=0
    for i in range(n+1):
        p.append([])
        for j in range(n):
            if i-1==j:
                p[i].append(1)
            else:
                p[i].append(0)
    p[0]=p[n]
    y.append(x_old)
    acc_temp="Обчислимо значання для y(0)="+str(y[0])
    acc.append(acc_temp)
    lim=0
    while lim<500:
        temp=Poshuk(y[iterator],p[iterator],e,f,dir)
        y.append(temp)
        acc_temp="Обчислимо значання для y("+str(iterator+1)+")="+str(y[iterator+1])
        acc.append(acc_temp)
        acc_temp="Перевіряємо умови завершення обчислень:"
        acc.append(acc_temp)
        if iterator<n-1:
            iterator=iterator+1
            acc_temp="Оскільки i<n-1, збільшуємо і на 1"
            acc.append(acc_temp)
        elif iterator==n-1:
            acc_temp="Оскільки i=n-1, Перевіряємо додаткову умову:"
            acc.append(acc_temp)
            if y[n]==y[0]:
                acc_temp="Оскільки y[n]=y[0], новою оптимальною токою стає y[n]"
                acc.append(acc_temp)
                x_new=y[n]
                break
            else:
                acc_temp="Оскільки y[n] не дорвнює y[0], збільшуємо і на 1"
                acc.append(acc_temp)
                iterator=iterator+1
        elif iterator==n:
            lim=lim+1
            acc_temp="Оскільки i=n, Перевіряємо додаткову умову:"
            acc.append(acc_temp)
            if y[n+1]==y[1]:
                acc_temp="Оскільки y[n+1]=y[1], новою оптимальною токою стає y[n+1]"
                acc.append(acc_temp)
                x_new=y[n+1]
                break
            else:
                acc_temp="Оскільки y[n+1] не дорвнює y[1], проводимо додаткові перевірки:"
                acc.append(acc_temp)
                x_new=y[n+1]
                y.clear()
                y.append(x_new)
                if Test(x_new,x_old)<e:
                    acc_temp="Умова похибки виконана, новою оптимальною токою стає y[n+1],алгоритм завершується"
                    acc.append(acc_temp)
                    break
                else:
                    p[0]=Min(y[n+1],y[1])
                    for i in range(1,n,1):
                        p[i]=p[i+1]
                    p[n]=p[0]
                    acc_temp="Умова похибки не виконана, переобчислюється масив p: "+str(p)
                    acc.append(acc_temp)
                    iterator=0
    x=x_new
    acc_temp="Нова оптимальна точка матиме координати: "+str(x_new)+", та значення функції в даній точці: "+str(eval(f))
    acc.append(acc_temp)    
    return acc
