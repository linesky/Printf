def fpar(*varss):
    svars=list(*varss)
    
    sreturn:str=""
    vars:list=[]
    for n in svars:
        vars=vars+[str(n)]
    
  
    lens=len(vars)
    
    
    
    i:int=0
    if lens==0:
        ii=0
    sreturn=str(vars[0])
    if lens==1:
        sreturn=str(vars[0])

    else:
        lens2=lens
        for n in range(1,lens2):
                ss=str(vars[n])
                sreturn=sreturn.replace("$"+str(n-1),ss)

 
    return sreturn
def printfpar(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(fpar(vars))        
         
print("\x1bc\x1b[41;37m")
for nn in range(10):
    printfpar("hello world $0 ----- $1 \n",nn,"#####")
