


def taking(stones,queens,center):
    for j in range(len(stones)): 
                                      
        if stones[j].get_center()==center:
            tk=stones[j]
    for i in range(len(queens)):
        
        if (queens[i].get_center()==center):            
            tk=queens[i]

    return tk

def queen_take_updt(st_center,tk):
    x=0
    y=0
    center=st_center
    help=[]
    
    for i in range(len(tk)):
        help.append(tk[i].get_center())
           
    while True:
        #skočil jsem doleva nahoru, najdu první střed na diagonále v opačném směru        
        x=center[0]+100
        y=center[1]+100
            
        #print(tk[i].get_center())
        if [x,y] in help:       #pokud je to v taku vrať ten prvek 
            for i in range(len(tk)):
                if [x,y]==tk[i].get_center():       
                    return tk[i]
        #kraj plochy
        elif (x==750) or (y==750):
                
            break
        center=[x,y]
    
    center=st_center
          
    while True:
         #skočil jsem doprava dolu, najdu první střed na diagonále v opačném směru        
        x=center[0]-100
        y=center[1]-100
        
        
        if [x,y] in help:
            for i in range(len(tk)):
                
                if [x,y]==tk[i].get_center():        
                    return tk[i]
        #kraj plochy
        elif (x==50) or (y==50):
                
            break
        center=[x,y]
    
    center=st_center    
          
    while True:
        #skočil jsem doleva dolu, najdu první střed na diagonále v opačném směru        
        x=center[0]+100
        y=center[1]-100
                       
        if [x,y] in help:
            for i in range(len(tk)):
                
                if [x,y]==tk[i].get_center():        
                    return tk[i]
        #kraj plochy
        elif (x==750) or (y==50):
                
            break
        center=[x,y]

    center=st_center
           
    while True:
        #skočil jsem doleva nahoru, najdu první střed na diagonále v opačném směru        
        x=center[0]-100
        y=center[1]+100
            
        #print(tk[i].get_center())
        if [x,y] in help:
            for i in range(len(tk)):
                
                if [x,y]==tk[i].get_center():        
                    return tk[i]
        #kraj plochy
        elif (x==50) or (y==750):
                
            break  
        center=[x,y]


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
            return center

    elif center[0]==750:
            center[0]=center[0]-100
            center[1]=center[1]-100
            return center

    else:
            x=p_d[name][0][0]-center[0]
           # print(f"x= {x}")
            center[1]=center[1]-100
            if x<0:
                center[0]=center[0]-100
            else:
                center[0]=center[0]+100
            #print(f"center = {center}")
            return center



    

def c_c_b(stone,p_d):
    x=0   
    center=stone.get_center()
    name=stone.get_name() 
      
    if center[0]==50:
            center[0]=center[0]+100
            center[1]=center[1]+100
            return center

    elif center[0]==750:
            center[0]=center[0]-100
            center[1]=center[1]+100
            return center

    else:
            x=p_d[name][0][0]-center[0]
            center[1]=center[1]+100
            if x<0:
                center[0]=center[0]-100
            else:
                center[0]=center[0]+100

            return center


def where_jump(ch_stone,tk):
    center=ch_stone[0].get_center()
    tk_center=tk[0].get_center()
    x=0      #pomocná proměnná na souřadnice x
    y=0      #na souřadnice y

    x=center[0]-tk_center[0]
    y=center[1]-tk_center[1]
    print(center)
    print(tk_center)

    #4 možnosti, up_right, down_right, up_left, down_left -> budu vracet kam šla dáma
    #doprava nahoru
    if (x>0) & (y<0):
        return "up_right"
    elif (x>0)&(y>0):
        return "down_right"
    elif (x<0)&(y<0):
        return "up_left"
    elif (x<0)&(y>0):
        return "down_left"
    else:
        return "něco se dojebalo"
