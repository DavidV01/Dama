#from ast import Break
#from Stone import stone
#from C_M import center_mouse
from updt import screen_update
from Is_st import is_stone
#from Is_st import is_true
import pygame as pg
#from Plr import Player   #ošetřit, že jen ten hráč, co hraje hýbá se svými kameny

def Chosed(mouse_p,ws,bs,bg,scr,ch_stone,Pl_now,d,p_d,wq,bq,q_p_d):
    chosed=is_stone(ws,bs,mouse_p,ch_stone,wq,bq)       #vrátí, zda je ten kámen na stejný pozici, jako myš, vrátí kámen
    
    if (chosed.get_color())==(Pl_now.get_color()):     #zda má vybraný kámen stejnou bravu jako hráč
        if (p_d=={}) & (q_p_d=={}):
            if chosed.get_name() not in d:            
                return ch_stone
            elif (chosed.get_name() in d) & (chosed.get_name().startswith("D")):
                ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                pg.draw.circle(bg, 'red', mouse_p,40,20)          
                screen_update(scr,bg)
            else:
                ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                pg.draw.circle(bg, 'red', mouse_p,40)          
                screen_update(scr,bg)
                        #print(ch_stone[0])               
                
                return ch_stone
        elif q_p_d=={}:
            if chosed.get_name() not in p_d:
                return ch_stone
            elif (chosed.get_name() in p_d) & (chosed.get_name().startswith("D")):
                    ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                    pg.draw.circle(bg, 'red', mouse_p,40,20)          
                    screen_update(scr,bg)
            else:
                ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                pg.draw.circle(bg, 'red', mouse_p,40)          
                screen_update(scr,bg)
                            #print(ch_stone[0])
        else:
            if chosed.get_name() not in q_p_d:
                return ch_stone
            else:
                ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                pg.draw.circle(bg, 'red', mouse_p,40,20)          
                screen_update(scr,bg)
    return ch_stone