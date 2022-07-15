from Stone import stone,Queen

def load_stones(ws,bs):
    for i in range(len(ws)):
        ws[i]=stone(ws[i],"white",(0,0),40)

    for i in range(len(bs)):
        bs[i]=stone(bs[i],"gray",(0,0),40)

def load_queens(w_q,b_q):
    for i in range(len(w_q)):
        w_q[i]=Queen(w_q[i],"white",(0,0),40)

    for i in range(len(b_q)):
        b_q[i]=Queen(b_q[i],"gray",(0,0),40)
