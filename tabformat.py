def centers(s:str,i:int):
    xx:int=i
    
    xxx:int=len(s)

    xx=xx-xxx
    
    if xx<0:
        xx=0
    xxx:str=" "
    xxx=xxx*xx
    
    xxx=xxx+s
    
    print(xxx)
print("\x1bc\x1b[41;37m")
for i in range(10):
    centers("*"*(i*2),80)
