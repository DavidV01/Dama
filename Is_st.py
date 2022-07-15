from Stone import stone


def is_stone(ws,bs,mouse_pos,ch,w_qu,b_qu):
    for i in range(len(bs)):
        if bs[i].get_center()==mouse_pos:
            return bs[i]
    for i in range(len(ws)):
        if ws[i].get_center()==mouse_pos:
            return ws[i]
    for i in range(len(w_qu)):
        if w_qu[i].get_center()==mouse_pos:
            return w_qu[i]
            
    for i in range(len(b_qu)):
        if b_qu[i].get_center()==mouse_pos:
            return b_qu[i]
    return ch

def is_true(ws,bs,mouse_pos,w_qu,b_qu):
    for i in range(len(bs)):
        if bs[i].get_center()==mouse_pos:
            return True
    for i in range(len(ws)):
        if ws[i].get_center()==mouse_pos:
            return True
    for i in range(len(w_qu)):
        if w_qu[i].get_center()==mouse_pos:
            return True
    for i in range(len(b_qu)):
        if b_qu[i].get_center()==mouse_pos:
            return True
    return False
    

def is_there(center,ws,bs):
    for i in range(12):
        if bs[i].get_center()==center:
            return True
        elif ws[i].get_center()==center:
            return True
        else:
            return False

