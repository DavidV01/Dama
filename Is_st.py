from Stone import stone


def is_stone(ws,bs,mouse_pos,ch):
    for i in range(12):
        if bs[i].get_center()==mouse_pos:
            return bs[i]
        if ws[i].get_center()==mouse_pos:
            return ws[i]
    return ch

def is_true(ws,bs,mouse_pos):
    for i in range(12):
        if bs[i].get_center()==mouse_pos:
            return True
        if ws[i].get_center()==mouse_pos:
            return True
    return False