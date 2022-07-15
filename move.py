#from ast import Break
#from Stone import stone
from sympy import true
from C_M import center_mouse
from updt import screen_update
#from Is_st import is_stone
#from Is_st import is_true
import pygame as pg
#from Plr import Player   
from chck_mv import check_move
from crt_tree import create_tree_b_l, create_tree_b_r,create_tree_w_l,create_tree_w_r,create_tree_w_c,create_tree_b_c,Uzel



def move_stone(mouse_p,bg,scr,tile_s,ch_stone,new_rct_pos,bol,next_player,d,p_d,q_p_d): 

        if (ch_stone!=[])&(bol==False):          #pokud už mám vybraný kámen a hodlám udělat tah -> kliknu na pole bez kamene
            
            ch_mv=check_move(mouse_p,d,ch_stone,p_d,q_p_d) #TADY NĚKDE OŠETŘIT, JAK MOC SE MOHU HÝBAT -> FCE NAPŘ.: CHECK_MOVE!!!!!
            if ch_mv ==False:
                next_player=False
                return next_player
            rect = (new_rct_pos[0],new_rct_pos[1], tile_s, tile_s)  
            if ch_stone[0].get_name().startswith("D"):
                pg.draw.rect(bg, 'black', rect)
                pg.draw.circle(bg, ch_stone[0].get_color(), mouse_p,40,20)                                 
                ch_stone[0].center(mouse_p)   #chosed.center(mouse_p)
                screen_update(scr,bg)
                next_player=True
            else:
                pg.draw.rect(bg, 'black', rect)
                pg.draw.circle(bg, ch_stone[0].get_color(), mouse_p,40)                                 
                ch_stone[0].center(mouse_p)   #chosed.center(mouse_p)
                screen_update(scr,bg)
                next_player=True 
              
        return next_player   


def move_again_w(stone,c_l_w,p_d,c_l_b,batch,w_stones,l,p):
    p_d={}
    center=stone.get_center()
    center1=stone.get_center()

    #levý kraj
    if center[0]==50:
        center[0]=center[0]+100
        center[1]=center[1]-100
        if center in c_l_b:
            new_center=[0,0]
            new_center[0]=center[0]+100
            new_center[1]=center[1]-100                                         

            if (new_center in c_l_w) or (new_center in c_l_b):
                return p_d           
            else:
                p_d=create_tree_w_l(stone,w_stones,new_center,p_d,c_l_b,batch)
                return  p_d
    #pravý kraj
    elif center[0]==750:
        center[0]=center[0]-100
        center[1]=center[1]-100

        if center in c_l_b: 
            new_center=[0,0]
            new_center[0]=center[0]-100
            new_center[1]=center[1]-100                                        

            if (new_center in c_l_w) or (new_center in c_l_b):
                return p_d
            else:
                p_d=create_tree_w_r(stone,w_stones,new_center,p_d,c_l_b,batch)
                return p_d   
    #ve středu plochy  
                                    
    else:
        #doleva            
        center[0]=center[0]-100
        center[1]=center[1]-100  

        if center in c_l_b:
            new_center=[0,0]
            new_center[0]=center[0]-100
            new_center[1]=center[1]-100

            if (new_center[0]<50) or (new_center[1]<50):
                                                
                pass 

            elif (new_center in c_l_w) or (new_center in c_l_b):
                                                
                pass         
            else:
                p_d=create_tree_w_c(stone,w_stones,new_center,p_d,c_l_b,batch,l)
                pass

        #doprava
        center1[0]=center1[0]+100
        center1[1]=center1[1]-100
                           
        if center1 in c_l_b:
            new_center=[0,0]
            new_center[0]=center1[0]+100
            new_center[1]=center1[1]-100                                         

            if (new_center in c_l_w) or (new_center in c_l_b):
                                                
               return p_d
            elif (new_center[0]>750) or (new_center[1]<50):
                                                
                return p_d
            else:
                p_d=create_tree_w_c(stone,w_stones,new_center,p_d,c_l_b,batch,p)
                return p_d 

   
    return p_d

def move_again_b(stone,c_l_w,p_d,c_l_b,batch,w_queentones,l,p):
    p_d={}
    center=stone.get_center()
    center1=stone.get_center()

    #levý kraj
    if center[0]==50:
        center[0]=center[0]+100
        center[1]=center[1]+100
        if center in c_l_w:
            new_center=[0,0]
            new_center[0]=center[0]+100
            new_center[1]=center[1]+100                                         

            if (new_center in c_l_w) or (new_center in c_l_b):
                return p_d           
            else:
                p_d=create_tree_b_l(stone,w_queentones,new_center,p_d,c_l_w,batch)
                return  p_d
    #pravý kraj
    elif center[0]==750:
        center[0]=center[0]-100
        center[1]=center[1]+100

        if center in c_l_w: 
            new_center=[0,0]
            new_center[0]=center[0]-100
            new_center[1]=center[1]+100                                        

            if (new_center in c_l_w) or (new_center in c_l_b):
                return p_d
            else:
                p_d=create_tree_b_r(stone,w_queentones,new_center,p_d,c_l_w,batch)
                return p_d   
    #ve středu plochy  
                                    
    else:
        #doleva            
        center[0]=center[0]-100
        center[1]=center[1]+100  

        if center in c_l_w:
            new_center=[0,0]
            new_center[0]=center[0]-100
            new_center[1]=center[1]+100

            if (new_center[0]<50) or (new_center[1]>750):
                                                
                pass  

            elif (new_center in c_l_w) or (new_center in c_l_b):
                                                
                pass          
            else:
                p_d=create_tree_b_c(stone,w_queentones,new_center,p_d,c_l_w,batch,l)
                pass

        #doprava
        center1[0]=center1[0]+100
        center1[1]=center1[1]+100                     
        if center1 in c_l_w:
            new_center=[0,0]
            new_center[0]=center1[0]+100
            new_center[1]=center1[1]+100                                         

            if (new_center in c_l_w) or (new_center in c_l_b):
                                                
               return p_d
            elif (new_center[0]>750) or (new_center[1]>750):
                                                
                return p_d
            else:
                p_d=create_tree_b_c(stone,w_queentones,new_center,p_d,c_l_w,batch,p)
                return p_d 

   
    return p_d

#pohyb dámy bez braní figurek, její možné tahy 
def queens_move(wh_queen,c_l_w,c_l_b):
    pref_d={}
    dict={}
    #diagonály, na kterých hraje král
    #směr doprava nahoru
    legendary_route = [[50,750],[150,650],[250,550],[350,450],[450,350],[550,250],[650,150],[750,50]]     #jediná roh roh diagonála

    super_rare_route_r_down = [[250,750],[350,650],[450,550],[550,450],[650,350],[750,250]]                     #cesta pod hl. diagonálou
    super_rare_route_r_up = [[50,550],[150,450],[250,350],[350,250],[450,150],[550,50]]                         #cesta nad hl. diagonálou atd...

    uncommon_route_r_down = [[450,750],[550,650],[650,550],[750,450]]
    uncommon_route_r_up = [[50,350],[150,250],[250,150],[350,50]]

    pleb_route_r_down = [[650,750],[750,650]]
    pleb_route_r_up = [[50,150],[150,50]]

    #směr doleva dolu
    epic_route_l_down = [[50,150],[150,250],[250,350],[350,450],[450,550],[550,650],[650,750]]
    epic_route_l_up = [[150,50],[250,150],[350,250],[450,350],[550,450],[650,550],[750,650]]

    rare_route_l_down = [[50,350],[150,450],[250,550],[350,650],[450,750]]
    rare_route_l_up = [[350,50],[450,150],[550,250],[650,350],[750,450]]

    common_route_l_down = [[50,550],[150,650],[250,750]]
    common_route_l_up = [[550,50],[650,150],[750,250]]




    if pref_d=={}:
        dict = load_to_dict(wh_queen,legendary_route,dict,c_l_w,c_l_b)

        dict = load_to_dict(wh_queen,super_rare_route_r_down,dict,c_l_w,c_l_b)
        dict = load_to_dict(wh_queen,super_rare_route_r_up,dict,c_l_w,c_l_b)

        dict = load_to_dict(wh_queen,uncommon_route_r_down,dict,c_l_w,c_l_b)
        dict = load_to_dict(wh_queen,uncommon_route_r_up,dict,c_l_w,c_l_b)

        dict = load_to_dict(wh_queen,pleb_route_r_down,dict,c_l_w,c_l_b)
        dict = load_to_dict(wh_queen,pleb_route_r_up,dict,c_l_w,c_l_b)

        dict = load_to_dict(wh_queen,epic_route_l_down,dict,c_l_w,c_l_b)
        dict = load_to_dict(wh_queen,epic_route_l_up,dict,c_l_w,c_l_b)

        dict = load_to_dict(wh_queen,rare_route_l_down,dict,c_l_w,c_l_b)
        dict = load_to_dict(wh_queen,rare_route_l_up,dict,c_l_w,c_l_b)

        dict = load_to_dict(wh_queen,common_route_l_down,dict,c_l_w,c_l_b)
        dict = load_to_dict(wh_queen,common_route_l_up,dict,c_l_w,c_l_b)    


    return dict
    
#vyhoď políčko, kde stojí
def load_to_dict(w_queen,route,d,c_l_w,c_l_b):

    #pro každou dámu ze seznamu dam
    for i in range(len(w_queen)):                       #testovací, poté len(w_queen)
        
        #pokud je královna v seznamu cesty
        if w_queen[i].get_center() in route:

            start = where_from(w_queen[i],route,c_l_w,c_l_b) #odkud
            end = where_to(w_queen[i],route,c_l_w,c_l_b) #kam
            #print(start)
            #print(end)
            #aby začínala s prázdným seznamem
            if w_queen[i].get_name() not in d.keys():
                d[f"{w_queen[i].get_name()}"]=[]            

            for j in range(start,end):
                #skipni, kde stojím                    
                if route[j]==w_queen[i].get_center():
                    pass                                          
                else:
                    d[f"{w_queen[i].get_name()}"].append(route[j])
           

    return d

#odkud
def where_from(w_qu,route,c_l_w,c_l_b):
    x=0    #odkud
    check=0
    
    for i in range(len(route)):
        if route[i] in c_l_w:    #pokud je tam bílá, je mi to jedno
            for j in range(len(c_l_w)):
                check=w_qu.get_center()[0]-c_l_w[j][0]
                if (route[i]==c_l_w[j]) & (check>0):
                    x=i+1    #abych začínal od dalšího prvku
        #pokud je tam černá, zjistím, zda za ní něco není
        elif route[i] in c_l_b:
            for j in range(len(c_l_b)):     #možná lkepší do while
                
                check=w_qu.get_center()[0]-c_l_b[j][0]
                
                if (route[i]==c_l_b[j]) & (check>0):            
                    x=i+1                    
              
    return x


def where_to(w_qu,route,c_l_w,c_l_b):
    x=0
    check=0
    for i in range(len(route)):
        if route[i] in c_l_w:
            for j in range(len(c_l_w)):
                check=w_qu.get_center()[0]-c_l_w[j][0]
                
                if (route[i]==c_l_w[j]) & (check<0):
                    x=i   #abych začínal od předešlého prvku
                    break
        elif route[i] in c_l_b:
            for j in range(len(c_l_b)):
                
                check=w_qu.get_center()[0]-c_l_b[j][0]
                
                if (route[i]==c_l_b[j]) & (check<0):
                    x=i  #abych začínal od předešlého prvku
                    break
        
        if check<0:            
            return x

    return len(route)  

def move_again_b_q(b_q,queen_pref_d,center_list_b,center_list_w):
    queen_pref_d={}
    #doleva nahoru od středu dámy
    for i in range(len(b_q)):
        hop=False
        batch=Uzel(b_q[i].get_name())
        list_n=[]
        x=0    #pomocné prom
        y=0
        center=[0,0]
        center=b_q[i].get_center()
                                
        while True:
                                    
            if center==[0,0]:
                break
            elif (center[0]==50) or (center[1]==750):
                break
                                    
            x=center[0]-100
            y=center[1]-100
                                    
            #pokud kraj plochy
            if (x<50) or (y<50):
                                        
                break
                                    #pokud černá
            elif [x,y] in center_list_b:
                break
                                    #pokud bílá
            elif (hop==True) & ([x,y] not in center_list_w):
                                            #print(center)
                                            
                    if [x,y] not in list_n:
                        list_n.append([x,y])
                                            
                        center=[x,y]
            elif ([x,y] in center_list_w) & (hop==False):
                center1=[0,0]
                center1[0]=x-100
                center1[1]=y-100
                                        
                                        
                if (center1[0]<50) or (center1[1]<50):
                    break
                elif (center1 in center_list_b) or (center1 in center_list_w):
                    break
                                        
                else:                                            
                    hop=True
                                            
                    list_n.append(center1)
                    center=[x,y]

            elif ([x,y] in center_list_w) & (hop==True):                                        
                    break 
            center=[x,y]
                                
            if list_n != []: 
                if  b_q[i].get_name() not in queen_pref_d.keys():
                                        
                    queen_pref_d[b_q[i].get_name()]=[]
                                        
                    for j in range(len(list_n)):            
                        queen_pref_d[b_q[i].get_name()].append(list_n[j]) 
                else:
                    for j in range(len(list_n)): 
                        queen_pref_d[b_q[i].get_name()].append(list_n[j])      
     
            #doprava dolu od středu dámy
    for i in range(len(b_q)):
        hop=False
        batch=Uzel(b_q[i].get_name())
        list_n=[]
        x=0    #pomocné prom
        y=0
        center=[0,0]
        center=b_q[i].get_center()
                                
        while True:
                                    
            if center==[0,0]:
                break
            elif (center[0]==750) or (center[1]==750):
                break
                                    
            x=center[0]+100
            y=center[1]+100
                                    
            #pokud kraj plochy
            if (x>750) or (y>750):
                                        
                break
            #pokud černá
            elif [x,y] in center_list_b:
                break
            #pokud bílá
            elif (hop==True) & ([x,y] not in center_list_w):
                     #print(center)
                                            
                    if [x,y] not in list_n:
                        list_n.append([x,y])
                                            
                    center=[x,y]
            elif ([x,y] in center_list_w) & (hop==False):
                center1=[0,0]
                center1[0]=x+100
                center1[1]=y+100
                                        
                                        
                if (center1[0]>750) or (center1[1]>750):
                    break
                elif (center1 in center_list_b) or (center1 in center_list_w):
                    break
                                        
                else:                                            
                    hop=True
                                            
                    list_n.append(center1)
                center=[x,y]

            elif ([x,y] in center_list_w) & (hop==True):                                        
                break 
            center=[x,y]
                                
        if list_n != []: 
            if  b_q[i].get_name() not in queen_pref_d.keys():
                                        
                queen_pref_d[b_q[i].get_name()]=[]
                                        
                for j in range(len(list_n)):            
                    queen_pref_d[b_q[i].get_name()].append(list_n[j]) 
            else:
                for j in range(len(list_n)): 
                    queen_pref_d[b_q[i].get_name()].append(list_n[j])      
              
                                            
                            
    #doprava nahoru od středu dámy                         
    for i in range(len(b_q)):
        hop=False
        batch=Uzel(b_q[i].get_name())
        list_n=[]
        x=0    #pomocné prom
        y=0
        center=[0,0]
        center=b_q[i].get_center()
                                
        while True:
                                    
            if center==[0,0]:
                break
            elif (center[0]==50) or (center[1]==750):
                break
                                    
            x=center[0]+100
            y=center[1]-100
                                    
            #pokud kraj plochy
            if (x>750) or (y<50):
                                        
                break
            #pokud černá
            elif [x,y] in center_list_b:
                break
            #pokud bílá
            elif (hop==True) & ([x,y] not in center_list_w):
                    #print(center)
                                            
                    if [x,y] not in list_n:
                        list_n.append([x,y])
                                            
                    center=[x,y]
            elif ([x,y] in center_list_w) & (hop==False):
                center1=[0,0]
                center1[0]=x+100
                center1[1]=y-100
                                        
                                        
                if (center1[0]>750) or (center1[1]<50):
                    break
                elif (center1 in center_list_b) or (center1 in center_list_w):
                    break
                                        
                else:                                            
                    hop=True
                                            
                    list_n.append(center1)
                center=[x,y]

            elif ([x,y] in center_list_w) & (hop==True):                                        
                break 
            center=[x,y]
                                
        if list_n != []: 
            if  b_q[i].get_name() not in queen_pref_d.keys():
                                        
                queen_pref_d[b_q[i].get_name()]=[]
                                        
                for j in range(len(list_n)):            
                    queen_pref_d[b_q[i].get_name()].append(list_n[j]) 
            else:
                for j in range(len(list_n)): 
                    queen_pref_d[b_q[i].get_name()].append(list_n[j])  
                                                          
    #doleva dolu od středu dámy
    for i in range(len(b_q)):
        hop=False
        batch=Uzel(b_q[i].get_name())
        list_n=[]
        x=0    #pomocné prom
        y=0
        center=[0,0]
        center=b_q[i].get_center()
                                
        while True:
                                    
            if center==[0,0]:
                break
            elif (center[0]==50) or (center[1]==750):
                break
                                    
            x=center[0]-100
            y=center[1]+100
                                    
            #pokud kraj plochy
            if (x<50) or (y>750):
                                        
                break
            #pokud černá
            elif [x,y] in center_list_b:
                break
            #pokud bílá
            elif (hop==True) & ([x,y] not in center_list_w):
                    #print(center)
                                            
                    if [x,y] not in list_n:
                        list_n.append([x,y])
                                            
                    center=[x,y]
            elif ([x,y] in center_list_w) & (hop==False):
                center1=[0,0]
                center1[0]=x-100
                center1[1]=y+100
                                        
                                        
                if (center1[0]<50) or (center1[1]>750):
                    break
                elif (center1 in center_list_b) or (center1 in center_list_w):
                    break
                                        
                else:                                            
                    hop=True
                                            
                    list_n.append(center1)
                center=[x,y]

            elif ([x,y] in center_list_w) & (hop==True):                                        
                break 
            center=[x,y]
                                
        if list_n != []: 
            if  b_q[i].get_name() not in queen_pref_d.keys():
                                        
                queen_pref_d[b_q[i].get_name()]=[]
                                        
                for j in range(len(list_n)):            
                    queen_pref_d[b_q[i].get_name()].append(list_n[j]) 
            else:
                for j in range(len(list_n)): 
                    queen_pref_d[b_q[i].get_name()].append(list_n[j])

    return queen_pref_d
