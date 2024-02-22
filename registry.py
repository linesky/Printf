def tofile(f1:str,f2:str):
    ff=open(f2,"r")
    heads=ff.read()
    ff.close()
    heads=heads.replace("\r\n","\n")
    heads=heads.replace("\r","n")
    heads=heads.replace("\n","\x00\x01")
    heads=heads.replace("=","\x00")
    heads=heads.replace("\\n","\n")
    heads=heads.replace("\\r","\r")
    heads=heads.replace("\\t","\t")
    heads=heads.replace("\\v","\v")
    heads=heads+"\x02"
    ff=open(f1,"w")
    ff.write(heads)
    ff.close()


print("\x1bc\x1b[41;37m")
tofile("registry.dat","registry.txt")