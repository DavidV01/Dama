from Stone import stone

def load_stones(ws,bs):
    for i in range(len(ws)):
        ws[i]=stone(ws[i],"white",(0,0),40)

    for i in range(len(bs)):
        bs[i]=stone(bs[i],"gray",(0,0),40)