x,y,c=map(float,input().split())
l,r=0,min(x,y)
for _ in range(20):t=(l+r)/2;l,r=[[t,r],[l,t]][(x*x-t*t)**-.5+(y*y-t*t)**-.5>1/c]
print(t)