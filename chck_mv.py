

def check_move(mouse_p,dictionary,ch_stone,p_d,q_p_d):
   
    if ch_stone == []:
        return False

    name=ch_stone[0].get_name() 
    if q_p_d=={}: 
        if p_d =={}:   
            if mouse_p in dictionary[name]:
                return True
            else:
                return False
        elif mouse_p in p_d[name]:
            return True
    elif mouse_p in q_p_d[name]:
        return True
    return False
