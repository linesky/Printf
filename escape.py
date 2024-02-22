def escapes(s:str)->str:
    sreturn=s.replace("#n","\n")
    sreturn=sreturn.replace("#r","\r")
    sreturn=sreturn.replace("#t","\t")
    sreturn=sreturn.replace("#f","\f")
   
    return sreturn

print("\x1bc\x1b[41;37m")
s1="hello world#thello world#nhello world#n"
print(s1)
print(escapes(s1))