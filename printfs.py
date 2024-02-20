def printfs(*varss:list):
    
    
    vars:list=[]
    for n in varss:
        vars=vars+[n]
    
  
    lens=len(vars)
    
    
    
    i:int=0
    if lens==0:
        ii=0

    if lens==1:
        print(vars[0])

    else:
        spl=vars[0].split("%")
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                print(ss,end="")
            else:
                if len(ss)>1:
                    
                    print(ss[1:],end="")

 
            if n<lens-1:
                ss=vars[n+1]
                print(ss,end="")
           
         
print("\x1bc\x1b[41;37m")
for nn in range(10):
    printfs("hello world %s %s \n",nn,"#####")
