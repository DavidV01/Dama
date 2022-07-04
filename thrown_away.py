from Stone import stone

def away(stones,thr_aw):
    for i in range(len(stones)):
        if stones[i].get_center()==[0,0]:
            thr_aw.append(stones[i].get_name())
    
    return thr_aw

def filt(stones,thrown):
    y=[]
    for i in range(len(stones)):
        if (stones[i].get_name()) in (thrown):                       
            y.append(i)

    for i in range(len(y)):
        stones.pop()          
    return stones
        


