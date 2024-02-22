def codes(*varss):
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
       
        spl=vars[0].split("~")
        
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                sreturn=sreturn+str(ss)
            else:
                if len(ss)>1:
                    
                    sreturn=sreturn+ss

 
            if n<lens-1:
                vv=n+1
                ss=vars[vv]
                iii:int=int(ss)
                
                sreturn=sreturn+str(chr(iii))
    return sreturn
def printcodes(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(codes(vars))        
         
print("\x1bc\x1b[41;37m")
printcodes("hello world~0~1~2 #####",33,33,10)
