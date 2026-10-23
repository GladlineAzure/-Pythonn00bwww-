a,b,c,d=map(int,input().split())
e=a*60
f=c*60
g=-(e+b)+(f+d)
x=g//60
y=g%60
print(x,":",y,sep="")