


def taking(stones,center):
    for j in range(len(stones)):                                
        if stones[j].get_center()==center:
            tk=stones[j]

    return tk

def tk_updt_b(stone_center,tk):       #tk=množina tohu, co mohu brát, tato fce mi řekne, co ze dvou beru
    tk_updt=0
    new_center=[0,0]
    new_center[0]=stone_center[0]+100
    new_center[1]=stone_center[1]-100
    
    for i in range(len(tk)):
        
        if tk[i].get_center()==new_center:
            tk_updt=tk[i]

    new_center=[0,0]
    new_center[0]=stone_center[0]-100
    new_center[1]=stone_center[1]-100
    
    for i in range(len(tk)):
        
        if tk[i].get_center()==new_center:
            tk_updt=tk[i]

    return tk_updt

def tk_updt_w(stone_center,tk):       #tk=množina tohu, co mohu brát, tato fce mi řekne, co ze dvou beru
    tk_updt=0
    new_center=[0,0]
    new_center[0]=stone_center[0]-100
    new_center[1]=stone_center[1]+100
    for i in range(len(tk)):
        if tk[i].get_center()==new_center:
            tk_updt=tk[i]
            

    new_center=[0,0]
    new_center[0]=stone_center[0]+100
    new_center[1]=stone_center[1]+100

    for i in range(len(tk)):
        if tk[i].get_center()==new_center:
            tk_updt=tk[i]

    return tk_updt


def c_c_w(stone,p_d):
    x=0   
    center=stone.get_center()
    name=stone.get_name() 
      
    if center[0]==50:
            center[0]=center[0]+100
            center[1]=center[1]-100

    elif center[0]==750:
            center[0]=center[0]-100
            center[1]=center[1]-100
        
    else:
            x=p_d[name][0][0]-center[0]
            center[1]=center[1]-100
            if x<0:
                center[0]=center[0]-100
            else:
                center[0]=center[0]+100



    return center

def c_c_b(stone,p_d):
    x=0   
    center=stone.get_center()
    name=stone.get_name() 
      
    if center[0]==50:
            center[0]=center[0]+100
            center[1]=center[1]+100

    elif center[0]==750:
            center[0]=center[0]-100
            center[1]=center[1]+100
        
    else:
            x=p_d[name][0][0]-center[0]
            center[1]=center[1]+100
            if x<0:
                center[0]=center[0]-100
            else:
                center[0]=center[0]+100



    return center
