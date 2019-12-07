class IO:
    supportSrcs = ["console","File"]
    def read(src):
        if src not in IO.supportSrcs:
            return ("Class Test")
            #print("Not support", src)
        else:
            return ('Class Test ', src)
            #print ("Read from",src)

#print(IO.supportSrcs)

#IO.read("File")
#IO.read("Internet")
