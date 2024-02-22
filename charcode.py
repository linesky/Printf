def charcodes(*varss):
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
       
        spl=vars[0].split("[")
        
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                sreturn=sreturn+str(ss)
           
            else:
                if 0==0:
                    kkk=ss.split("]")
                    
                    llll=chr(int(kkk[0]))
                    
                    if len(kkk)>1:
                        sreturn=sreturn+str(llll)+str(kkk[1])
                   
 
           
    return sreturn


def printcharcodes(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(charcodes(vars))        
         
print("\x1bc\x1b[41;37m")

for nn in range(10):
    printcharcodes("hello world[033]XXX[034]xxx[010]mmmm")
