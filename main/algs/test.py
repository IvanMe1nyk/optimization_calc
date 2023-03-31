import method4
dir="min"
f="x[0]**2+x[1]**2"
n=2
x=list()
x_old='2,1'
y=list()
z=list()
alpha=1
beta=0.5
M=30
N=10
t=1
R=0.001
acc=method4.alg(x_old,f,n,alpha,beta,M,N,t,R,dir)
for i in acc:
    print(i)
    