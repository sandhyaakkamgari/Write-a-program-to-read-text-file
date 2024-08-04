import sys,random
with open(sys.argv[1],"r") as f:
    f.seek(0,2)                 # seek to end of file
    bytes = f.tell()
    f.seek(int(bytes*random.random()))

    # Now seek forward until beginning of file or we get a \n
    while True:
        f.seek(-2,1)
        ch = f.read(1)
        if ch=='\n': break
        if f.tell()==1: break

    # Now get a line
    print f.readline()