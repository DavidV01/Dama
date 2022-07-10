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
from crt_tree import create_tree_b_l, create_tree_b_r,create_tree_w_l,create_tree_w_r,create_tree_w_c,create_tree_b_c


def move_stone(mouse_p,bg,scr,tile_s,ch_stone,new_rct_pos,bol,next_player,d,p_d): 

        if (ch_stone!=[])&(bol==False):          #pokud už mám vybraný kámen a hodlám udělat tah -> kliknu na pole bez kamene
            
            ch_mv=check_move(mouse_p,d,ch_stone,p_d) #TADY NĚKDE OŠETŘIT, JAK MOC SE MOHU HÝBAT -> FCE NAPŘ.: CHECK_MOVE!!!!!
            if ch_mv ==False:
                next_player=False
                return next_player
            rect = (new_rct_pos[0],new_rct_pos[1], tile_s, tile_s)    
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

def move_again_b(stone,c_l_w,p_d,c_l_b,batch,b_stones,l,p):
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
                p_d=create_tree_b_l(stone,b_stones,new_center,p_d,c_l_w,batch)
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
                p_d=create_tree_b_r(stone,b_stones,new_center,p_d,c_l_w,batch)
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
                p_d=create_tree_b_c(stone,b_stones,new_center,p_d,c_l_w,batch,l)
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
                p_d=create_tree_b_c(stone,b_stones,new_center,p_d,c_l_w,batch,p)
                return p_d 

   
    return p_d
        
    