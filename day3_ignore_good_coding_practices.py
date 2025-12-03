import sys
for z in 1,11:
 t=0
 for l in sys.argv[1].split("\n"):
  s=""
  for i in range(z,-1,-1):
   f,c,u,q=int(l[0]),1,l[1:-i] if i!=0 else l[1:],0
   for j in u:
    f,q=(int(j),c) if(int(j)>f) else (f,q)
    c+=1
   s,l=s+str(f),l[q+1:]
  t+=int(s)
 print(t)
