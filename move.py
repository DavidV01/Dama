import pygame as pg

def move_stone(mouse_p,ws,bs,bg,scr,tile_s,ch_stone,new_rct_pos):     #ch_stone a new_rct_pos musim volat, protože si je musím pamatovat globálně, abych se na ně mohl odkázat znovu
    
    if mouse_p!=[0,0]:                                   #pokud jsem klikl na černý čtverec
        bol=is_true(ws,bs,mouse_p)                      #is true vrací boolen, proto bol

        if (bol==True)&(ch_stone==[]):                    #pokud je kámen, a zároveň jsem zatím žádný jiný nevybral -> nemohu vybrat 2 kameny
            chosed=is_stone(ws,bs,mouse_p,ch_stone)       #vrátí, zda je ten kámen na stejný pozici, jako myš
            ch_stone.append(chosed)                             #přidej vybranej stone do seznamu, pro kontrolu
                                                                                                 
            #pokud jsem něco přidal do seznamu chosed a ten kámen neni vybrán
            pg.draw.circle(bg, 'red', mouse_p,40)            
            new_rct_pos[0]=mouse_p[0]-50
            new_rct_pos[1]=mouse_p[1]-50                               #nová pozice pro náhradu kruhu za čtverec, při změně pozice
            print(f"pozice myši: {mouse_p}")
            print(f"čtverec: {new_rct_pos}")
            screen_update(scr,bg)
            print(ch_stone[0])   
            return ch_stone,new_rct_pos                        
                                                     
        elif (ch_stone!=[])&(bol==False):          #pokud už mám vybraný kámen a hodlám udělat tah -> kliknu na pole bez kamene
            rect = (new_rct_pos[0],new_rct_pos[1], tile_s, tile_s)
            pg.draw.rect(bg, 'black', rect)
            pg.draw.circle(bg, 'gray', mouse_p,40)                                 
            ch_stone[0].center(mouse_p)   #chosed.center(mouse_p)
            ch_stone.pop(0)
            screen_update(scr,bg)   
        
    return ch_stone,new_rct_pos