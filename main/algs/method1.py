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

def Test(a,b):
    for i in a:
        if i>b:
            return False
    return True

def Mult(a,b):
    c=list()
    for i in range(len(b)):
        c.append(a*b[i])
    return c
    

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


def alg(x_start,f,delta,alpha,e,landa,dir):
    acc=list()
    x_start=StrInLis(x_start)
    delta=StrInLis(delta)
    x=x_start
    x_temp=x_start
    f_temp=eval(f)
    lim=0
    while Test(delta,e)==False :
        while lim<500:
            acc_temp='Ітерація '+str(lim+1)
            acc.append(acc_temp)
            for i in range(len(x)):
                acc_temp='Змінюємо '+str(i+1)+' змінну.'
                acc.append(acc_temp)
                f_i=eval(f)
                x[i]=x[i]+delta[i]
                f_k=eval(f)
                acc_temp='Нова точка матиме координати: '+str(x)+', та значення функції в даній точці f(x)='+str(f_k)
                acc.append(acc_temp)
                if Direc(f_k,f_i,dir)==False:
                    x[i]=x[i]-2*delta[i]
                    f_k=eval(f)
                    acc_temp='Оскільки значення функції змінилося в протилежну сорону до напрямку оптимізації, змінюємо змінну в протилежну сторону. Нова точка матиме такі координати: '+str(x)+', та значення функції в даній точці f(x)='+str(f_k)
                    acc.append(acc_temp)
                    if Direc(f_k,f_i,dir)==False:
                        x[i]=x[i]+delta[i]
                        f_k=eval(f)
                        acc_temp='Оскільки нове значення функції знову перебільшую початкове, повертаємося до початкового значення: '+str(x)
                        acc.append(acc_temp)
                    if i<len(x):
                        acc_temp='Переходимо до наступної змінної'
                        acc.append(acc_temp)
            acc_temp='Перевіряємо умову на закінчення циклу та зміну delta'
            acc.append(acc_temp)
            lim=lim+1
            if Direc(f_temp,f_k,dir)==True:
                x=x_temp
                acc_temp='Оскільки значення функції в попередній точнці більш оптимальне, ніж в новій, потріно зупинити цикл та переобчислити delta'
                acc.append(acc_temp)
                break
            else:
                f_temp=eval(f)
                y_temp=Add(x,Mult(landa,Min(x,x_temp)))
                x_temp,x=x,y_temp
                acc_temp='Оскільки значення функції в новійій точнці більш оптимальне, ніж в попередній, змінюємо контрольну точку та продовжуємо цикл'
                acc.append(acc_temp)
        acc_temp='Переобчислюємо delta та перевіряємо умову закінчення пошуку'
        acc.append(acc_temp)
        for i in range(len(delta)):
            if delta[i]>e:
                delta[i]=delta[i]/alpha
        acc_temp='Новий масив delta матиме наступний вигляд: ' +str(delta)
        acc.append(acc_temp)
    acc_temp='Алгоритм завершено, нова оптимальна точка матиме координати ' +str(x_temp)+', та значення функції в цій точці f= ' +str(f_k)
    acc.append(acc_temp)

    return acc