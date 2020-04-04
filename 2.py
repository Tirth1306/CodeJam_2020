################################## Tirth Patel(18BCE245) ########################################

test=int(input())
answer=[]

for i in range(test):
  l=[int(a) for a in str(input())]
  s=""
  e=""
  h=l[0]
  for i in range(len(l)):
    j=0
    flag=0
    if(i==0):
      while(j<l[i]):
        s=s+"("
        e=e+")"
        j+=1

      s=s+str(l[i])
      h=l[i]
      continue
    if(h==l[i]):
      s+=str(l[i])
      continue
    elif(h!=l[i]):
      if(h>l[i]):
        flag=0
        s+=e[0:h-l[i]]
        e=e[h-l[i]:]
        h=l[i]
        s+=str(l[i])
        continue
      elif(h<l[i]):
        flag=1

    if(flag==1):
      x=l[i]-h
    else:
      x=l[i]
    while(j<x):
      s+="("
      
      e+=")"
      j+=1
    
    s+=str(l[i])
    h=l[i]
  s+=e
  answer.append(s)
  

for i in range(test):
  print("Case #{}: {}".format(i+1,answer[i]))

################################## Tirth Patel(18BCE245) ########################################