debugvars=["a","b","c"]
def report(s:str):
    global debugvars
    l1=s+";"
    for n in range(len(debugvars)):
        l1=l1+str(debugvars[n])+"="+str(globals()[debugvars[n]])+","
    print(l1)
    

print("\x1bc\x1b[41;37m")
a=0
b=0
c=0
for c in range(8):
    a=c*2
    b=c*4 
    report("vars:")
