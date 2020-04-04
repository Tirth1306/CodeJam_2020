################################## Tirth Patel(18BCE245) ########################################

test=int(input())
answer=[]

for t in range(test):

  time=[]
  n=int(input())
  c=0
  j=0
  str=["" for x in range(n)]
  for i in range(n):
    a,b=map(int,input().split())
    time.append((a,i,b))

  time.sort(key=lambda x:x[0])
  
  for a,i,b in time:
    

    if(j<=a):
      j=b
      str[i]="J"

    elif(c<=a):
      c=b
      str[i]="C"

    else:
      str="IMPOSSIBLE"
      break

  answer.append("".join(str))

for i in range(test):
  print("Case #{}: {}".format(i+1,answer[i]))
  

################################## Tirth Patel(18BCE245) ########################################
