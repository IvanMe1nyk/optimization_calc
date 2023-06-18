from django.shortcuts import render
from .forms import MetGoldForm, MetPolPodForm, MetSvenForm, MetFibForm, MetKonfigForm,MetNapForm,MetRanForm,MetDefForm
from .algs.met_gold import alg as alg_gold
from .algs.met_pol_pod import alg as alg_pol_pod
from .algs.met_svenn import alg as alg_svenn
from .algs.met_fib import alg as alg_fib
from .algs.method1 import alg as alg_konf
from .algs.method2 import alg as alg_def
from .algs.method3 import alg as alg_nap
from .algs.method4 import alg as alg_ran
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def met_gold(request):
    f=None
    dir=None
    if request.method=='POST':
        form=MetGoldForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            a=float(form.cleaned_data['left'])
            b=float(form.cleaned_data['right'])
            exp=float(form.cleaned_data['exp'])
            dir=form.cleaned_data['dir']
            acc=alg_gold(a,b,exp,f,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_1_gold.html',context)
    else:
        form = MetGoldForm()
        context = {'form': form}
        return render(request, 'main/method_1_gold.html', context)


def met_pol_pod(request):
    f=None
    dir=None
    if request.method=='POST':
        form=MetPolPodForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            a=float(form.cleaned_data['left'])
            b=float(form.cleaned_data['right'])
            exp=float(form.cleaned_data['exp'])
            dir=form.cleaned_data['dir']
            acc=alg_pol_pod(a,b,exp,f,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_1_pol_pod.html',context)
    else:
        form = MetPolPodForm()
        context = {'form': form}
        return render(request, 'main/method_1_pol_pod.html', context)


def met_svenn(request):
    f=None
    dir=None
    if request.method=='POST':
        form=MetSvenForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            x=float(form.cleaned_data['x'])
            exp=float(form.cleaned_data['exp'])
            dir=form.cleaned_data['dir']
            acc=alg_svenn(x,exp,f,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_1_svenn.html',context)
    else:
        form = MetSvenForm()
        context = {'form': form}
        return render(request, 'main/method_1_svenn.html', context)

def met_fib(request):
    f=None
    dir=None
    if request.method=='POST':
        form=MetFibForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            a=float(form.cleaned_data['left'])
            b=float(form.cleaned_data['right'])
            exp=int(form.cleaned_data['exp'])
            dir=form.cleaned_data['dir']
            acc=alg_fib(a,b,exp,f,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_1_fib.html',context)
    else:
        form = MetFibForm()
        context = {'form': form}
        return render(request, 'main/method_1_fib.html', context)

def met_konfig(request):
    f=''
    dir=''
    x_start=''
    delta=''
    if request.method=='POST':
        form=MetKonfigForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            x_start=form.cleaned_data['x_start']
            delta=form.cleaned_data['delta']
            alpha=float(form.cleaned_data['alpha'])
            landa=float(form.cleaned_data['landa'])
            e=float(form.cleaned_data['exp'])
            dir=form.cleaned_data['dir']
            acc=alg_konf(x_start,f,delta,alpha,e,landa,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_2_1.html',context)
    else:
        form = MetKonfigForm()
        context = {'form': form}
        return render(request, 'main/method_2_1.html', context)




def met_nap(request):
    f=''
    dir=''
    x_start=''
    if request.method=='POST':
        form=MetNapForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            x_start=form.cleaned_data['x_start']
            n=int(form.cleaned_data['n'])
            e=float(form.cleaned_data['exp'])
            dir=form.cleaned_data['dir']
            acc=alg_nap(x_start,f,n,e,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_2_3.html',context)
    else:
        form = MetNapForm()
        context = {'form': form}
        return render(request, 'main/method_2_3.html', context)
    
    
def met_ran(request):
    f=''
    dir=''
    x_start=''
    if request.method=='POST':
        form=MetRanForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            x_start=form.cleaned_data['x_start']
            n=int(form.cleaned_data['nk'])
            M=int(form.cleaned_data['M'])
            N=int(form.cleaned_data['N'])
            alpha=float(form.cleaned_data['alpha'])
            beta=float(form.cleaned_data['beta'])
            t=float(form.cleaned_data['t'])
            R=float(form.cleaned_data['R'])
            dir=form.cleaned_data['dir']
            acc=alg_ran(x_start,f,n,alpha,beta,M,N,t,R,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_2_4.html',context)
    else:
        form = MetRanForm()
        context = {'form': form}
        return render(request, 'main/method_2_4.html', context)
    
def met_deform(request):
    f=''
    dir=''
    x_vershyny=''
    if request.method=='POST':
        form=MetDefForm(request.POST)
        if form.is_valid():
            form.save()
            f=form.cleaned_data['func']
            x_vershyny=form.cleaned_data['x_vershyny']
            n=int(form.cleaned_data['n'])
            alpha=float(form.cleaned_data['alpha'])
            beta=float(form.cleaned_data['beta'])
            e=float(form.cleaned_data['exp'])
            hamma=float(form.cleaned_data['hamma'])
            dir=form.cleaned_data['dir']
            acc=alg_def(x_vershyny,f,e,alpha,beta,hamma,n,dir)
            context={'acc':acc}
        else:
            error='Данні введені невірно перезавантажте сторінку'
            context={'error':error}
        return render(request,'main/method_2_2.html',context)
    else:
        form = MetDefForm()
        context = {'form': form}
        return render(request, 'main/method_2_2.html', context)