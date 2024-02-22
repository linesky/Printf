def fvars(*varss):
    svars=list(*varss)
    
    sreturn:str=""
    vars:list=[]
    for n in svars:
        vars=vars+[str(n)]
    
  
    lens=len(vars)
    
    
    
    i:int=0
    if lens==0:
        ii=0

    if 0==0:
       
        spl=vars[0].split("{")
        
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                sreturn=sreturn+str(ss)
           
            else:
                if 0==0:
                    kkk=ss.split("}")
                    
                    llll=globals()[kkk[0]]
                    
                    if len(kkk)>1:
                        sreturn=sreturn+str(llll)+str(kkk[1])
                   
 
           
    return sreturn


def printvars(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(fvars(vars))        
         
print("\x1bc\x1b[41;37m")
hello="#####"
for nn in range(10):
    printvars("hello world {hello} {nn} \n")
