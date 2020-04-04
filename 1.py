################################## Tirth Patel(18BCE245) ########################################

test=int(input())
ans=[]
for t in range(1,test+1):
  n=int(input())
  matrix=[]
  for i in range(n):
    a=[]
    a=list(map(int,input().split()))
    matrix.append(a)

  trace=0
  row=0
  col=0
  
  for i in range(n):
    c=[]
    trace+=matrix[i][i]
    if(len(matrix[i])!=len(set(matrix[i]))):
      row+=1
    for j in range(n):
      c.append(matrix[j][i])
    if(len(c)!=len(set(c))):
      col+=1
  ans.append([trace,row,col])

for t in range(0,test):
  print("Case #{}: {} {} {}".format(t+1,ans[t][0],ans[t][1],ans[t][2]))

################################## Tirth Patel(18BCE245) ########################################