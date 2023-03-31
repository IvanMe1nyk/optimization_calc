import math


def StrInLis(strin,n):
    lis=[[]]
    i=0
    strin=strin+','
    while strin.count(',')>0:
        k=strin.index(',')
        temp=float(strin[0:k:])
        if len(lis[i])<n:
            lis[i].append(temp)
        else:
            lis.append([])
            i=i+1
            lis[i].append(temp)
        strin=strin[k+1::]
    return lis
            
    
    
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

def Test(x_vershyny ,x_center ,f):
    x=x_center
    fc=eval(f)
    temp=0
    for i in x_vershyny:
        x=i
        fun=eval(f)
        temp=temp+(fun-fc)**2
    temp=math.sqrt(temp/len(x_vershyny))
    return temp

def MinMax(x_vershyny ,f,dir):
    temp=list()
    ret=list()
    for x in x_vershyny:
        fun=eval(f)
        temp.append(fun)
    k=temp.index(min(temp))
    ret.append(k)
    k=temp.index(max(temp))
    ret.append(k)
    if dir=="min":
        n=max(temp)
    else:
        n=min(temp)
    for i in range(len(temp)):
        if temp[i]==n:
            temp[i]=temp[ret[0]]
    if dir=="min":
        k=temp.index(max(temp))
    else:
        ret[0],ret[1]=ret[1],ret[0]
        k=temp.index(min(temp))
    ret.append(k)
    return ret

def Mult(a,b):
    c=list()
    for i in range(len(b)):
        c.append(a*b[i])
    return c

def Center(x_vershyny,a):
    x=list()
    for i in range(len(x_vershyny)-1):
        x.append(0)
    for i in range(len(x_vershyny)):
        if i!=a:
            x=Add(x,x_vershyny[i])
    x=Mult(1/(len(x_vershyny)-1),x)
    return x

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


def alg(x_vershyny,f,e,alpha,beta,hamma,n,dir):
    acc=list()
    x_vershyny=StrInLis(x_vershyny,n)
    lim=0
    min_max=MinMax(x_vershyny,f,dir)
    x_center=Center(x_vershyny,min_max[1])
    x=x_vershyny[min_max[1]]
    f_h=eval(f)
    x=x_vershyny[min_max[0]]
    f_l=eval(f)
    x=x_vershyny[min_max[2]]
    f_s=eval(f)
    while Test(x_vershyny,x_center,f)>e and lim<200:
        acc_temp="Визначаємо найкращу, найгіршу, другу найгіршу точку та середню многогранника:"
        acc.append(acc_temp)
        acc_temp="Найкраща точка: "+str(x_vershyny[min_max[0]])+";"
        acc.append(acc_temp)
        acc_temp="Найгірша точка: "+str(x_vershyny[min_max[1]])+";"
        acc.append(acc_temp)
        acc_temp="Друга найгіршу точка: "+str(x_vershyny[min_max[2]])+"."
        acc.append(acc_temp)
        acc_temp="Середнє точка: "+str(x_center)+"."
        acc.append(acc_temp)
        x_v=Add(x_center,Mult(alpha,Min(x_center,x_vershyny[min_max[1]])))
        x=x_v
        f_v=eval(f)
        acc_temp="Проводимо операцію відбиття, нова точка матиме кординати: "+str(x_v)+"."
        acc.append(acc_temp)
        acc_temp="Перевіряємо умову:"
        acc.append(acc_temp)
        if Direc(f_v,f_l,dir)==True:
            x_r=Add(x_center,Mult(hamma,Min(x_v,x_center)))
            x=x_r
            acc_temp="Якщо нова точка оптимальніша за найкращу, то проводимо операцію розтягнення, нова точка матиме кординати: "+str(x_r)+"."
            acc.append(acc_temp)
            f_r=eval(f)
            acc_temp="Перевіряємо умову:"
            acc.append(acc_temp)
            if Direc(f_r,f_l,dir)==True:
                acc_temp="Якщо нова точка оптимальніша за найкращу, то вона замінює найгіршу точку"
                acc.append(acc_temp)
                x_vershyny[min_max[1]]=x_r
            else:
                acc_temp="Якщо нова точка менш оптимальна за найкращу, тоді точка отримана після операції відбиття замінює найгіршу точку"
                acc.append(acc_temp)
                x_vershyny[min_max[1]]=x_v
        elif Direc(f_s,f_v,dir)==True and Direc(f_v,f_h,dir)==True:
            x_s=Add(x_center,Mult(beta,Min(x_vershyny[min_max[1]],x_center)))
            x_vershyny[min_max[1]]=x_s
            acc_temp="Якщо нова точка по оптимальності знаходиться між найгіршою та другою найгіршою, то проводимо операцію стиску, та замінюємо на неї найгіршу точку. Нова точка матиме кординати: "+str(x_s)+"."
            acc.append(acc_temp)
        elif Direc(f_l,f_v,dir)==True and Direc(f_v,f_s,dir)==True:
            x_vershyny[min_max[1]]=x_v
            acc_temp="Якщо нова точка по оптимальності знаходиться між найкращою та другою найгіршою, то замінюємо на неї найгіршу точку."
            acc.append(acc_temp)
        elif Direc(f_v,f_h,dir)==False:
            acc_temp="Якщо нова точка менш оптимальна ніж найгірша, то проводимо операцію редукції."
            acc.append(acc_temp)
            for i in range(len(x_vershyny)):
                x_vershyny[i]=Add(x_vershyny[min_max[0]],Mult(0.5,Min(x_vershyny[i],x_vershyny[min_max[0]])))
            acc_temp="Після редукції вершини многогранника матимуть наступні координати: "+str(x_vershyny)
            acc.append(acc_temp)
        min_max=MinMax(x_vershyny,f,dir)
        x_center=Center(x_vershyny,min_max[1])
        x=x_vershyny[min_max[1]]
        f_h=eval(f)
        x=x_vershyny[min_max[0]]
        f_l=eval(f)
        x=x_vershyny[min_max[2]]
        f_s=eval(f)
        lim=lim+1
        acc_temp="Перевіряємо умову похибки, при виконанні завершуємо алгоритм."
        acc.append(acc_temp)
    acc_temp="Нова оптимальна точка має координати: "+str(x_vershyny[min_max[0]])+", значення функції в цій точці:"+str(f_l)
    acc.append(acc_temp)
    return acc
#print(x_vershyny[min_max[0]])
#print(f_l)