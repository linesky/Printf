def sprintfs(*varss):
    svars=list(*varss)
    
    sreturn:str=""
    vars:list=[]
    for n in svars:
        vars=vars+[str(n)]
    
  
    lens=len(vars)
    
    
    
    i:int=0
    if lens==0:
        ii=0

    if lens==1:
        sreturn=sreturn+str(vars[0])

    else:
        spl=vars[0].split("%")
        
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                sreturn=sreturn+str(ss)
            else:
                if len(ss)>1:
                    
                    sreturn=sreturn+str(ss[1:])

 
            if n<lens-1:
                ss=vars[n+1]
                sreturn=sreturn+str(ss)
    return sreturn
def printfs(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(sprintfs(vars))        
         
print("\x1bc\x1b[41;37m")
for nn in range(10):
    printfs("hello world %s %s \n",nn,"#####")
