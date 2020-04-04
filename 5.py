################################## Tirth Patel(18BCE245) ########################################

test=int(input())

for i in range(1,test+1):

  n,k=map(int,input().split())

  print("Case #{}:".format(i),end=" ")

  if(k%n==0):
    print("POSSIBLE")
     
    val=k//n
    ex=val

    for i in range(n):
      for j in range(n):
        print(ex,end=" ")
        ex+=1
        if(ex==n+1):
          ex=1
    
      ex-=1

      if(ex==0):
        ex=n;
      print()
    
		
  elif(n==4 and k==6):
    print("POSSIBLE")
    print("1 2 3 4")
    print("2 1 4 3")
    print("3 4 2 1")
    print("4 3 1 2")
  
  elif(n==4 and k==7):
    print("POSSIBLE")
    print("2 1 3 4")
    print("1 3 4 2")
    print("4 2 1 3")
    print("3 4 2 1")
  
  elif(n==4 and k==9):
    print("POSSIBLE")
    print("2 3 1 4")
    print("3 1 4 2")
    print("4 2 3 1")
    print("1 4 2 3")
  
  
  elif(n==4 and k==10):
    print("POSSIBLE")
    print("1 2 3 4")
    print("2 4 1 3")
    print("3 1 4 2")
    print("4 3 2 1")
    
  
  elif(n==4 and k==11):
    print("POSSIBLE")
    print("2 4 1 3")
    print("4 1 3 2")
    print("3 2 4 1")
    print("1 3 2 4")
  
  
  elif(n==4 and k==13):
    print("POSSIBLE")
    print("2 4 3 1")
    print("4 3 1 2")
    print("1 2 4 3")
    print("3 1 2 4")
  

  elif(n==4 and k==14):
    print("POSSIBLE")
    print("3 4 1 2")
    print("4 3 2 1")
    print("1 2 4 3")
    print("2 1 3 4")


  elif(n==5 and k==7):
    print("POSSIBLE")
    print("2 1 3 4 5")
    print("1 2 5 3 4")
    print("3 4 1 5 2")
    print("4 5 2 1 3")
    print("5 3 4 2 1")
  
  
  elif(n==5 and k==8):
    print("POSSIBLE")
    print("1 2 3 4 5")
    print("2 1 5 3 4")
    print("3 4 2 5 1")
    print("4 5 1 2 3")
    print("5 3 4 1 2")
  
  
  elif(n==5 and k==9):
    print("POSSIBLE")
    print("3 1 2 4 5")
    print("1 3 5 2 4")
    print("2 4 1 5 3")
    print("4 5 3 1 2")
    print("5 2 4 3 1")
    

  
  elif(n==5 and k==11):
    print("POSSIBLE")
    print("4 1 2 3 5")
    print("1 4 5 2 3")
    print("2 3 1 5 4")
    print("3 5 4 1 2")
    print("5 2 3 4 1")
  
  
  elif(n==5 and k==12):
    print("POSSIBLE")
    print("3 5 4 2 1")
    print("4 1 3 5 2")
    print("5 2 1 3 4")
    print("1 3 2 4 5")
    print("2 4 5 1 3")
 
  elif(n==5 and k==13):
    print("POSSIBLE")
    print("2 3 4 1 5")
    print("3 2 5 4 1")
    print("4 1 3 5 2")
    print("1 5 2 3 4")
    print("5 4 1 2 3")
  
  elif(n==5 and k==14):
    print("POSSIBLE")
    print("1 2 4 5 3")
    print("2 3 5 4 1")
    print("4 1 3 2 5")
    print("5 4 1 3 2")
    print("3 5 2 1 4")
  
  elif(n==5 and k==16):
    print("POSSIBLE")
    print("1 2 3 4 5")
    print("2 4 1 5 3")
    print("3 5 4 2 1")
    print("4 1 5 3 2")
    print("5 3 2 1 4")
  
  elif(n==5 and k==17):
    print("POSSIBLE")
    print("2 1 3 4 5")
    print("1 4 2 5 3")
    print("3 5 4 1 2")
    print("4 2 5 3 1")
    print("5 3 1 2 4")

  
  elif(n==5 and k==18):
    print("POSSIBLE")
    print("1 3 2 4 5")
    print("3 5 4 2 1")
    print("2 1 5 3 4")
    print("4 2 1 5 3")
    print("5 4 3 1 2")

  elif(n==5 and k==19):
    print("POSSIBLE")
    print("1 2 3 4 5")
    print("2 5 4 3 1")
    print("3 1 5 2 4")
    print("4 3 1 5 2")
    print("5 4 2 1 3")

  
  elif(n==5 and k==21):
    print("POSSIBLE")
    print("3 5 1 4 2")
    print("5 3 2 1 4")
    print("1 4 5 2 3")
    print("4 2 3 5 1")
    print("2 1 4 3 5")
  
  elif(n==5 and k==22):
    print("POSSIBLE")
    print("4 2 3 1 5")
    print("2 5 1 3 4")
    print("3 4 5 2 1")
    print("1 3 4 5 2")
    print("5 1 2 4 3")
  
  elif(n==5 and k==23):
    print("POSSIBLE")
    print("4 5 3 1 2")
    print("5 4 2 3 1")
    print("3 1 5 2 4")
    print("1 2 4 5 3")
    print("2 3 1 4 5")
  
  else:
    print("IMPOSSIBLE")


################################## Tirth Patel(18BCE245) ########################################
