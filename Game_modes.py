#import csv
import pygame as pg
import itertools
from l_s import load_stones
from Pr_s import print_stones
from Pl_s import place_stones
from Stone import stone
from C_M import center_mouse
from updt import screen_update,destroy_stone
#from Is_st import is_stone
#from Is_st import is_true
from move import move_stone,move_again_w,move_again_b
from Plr import Player
from Is_st import is_true
from Chosed_stone import Chosed
from crt_tree import create_tree_b_l, create_tree_b_r,create_tree_w_l,create_tree_w_r,create_tree_w_c,create_tree_b_c
from thrown_away import away,filt
from center_l import center_list
from crt_tree import Uzel
from take import taking,tk_updt_w,tk_updt_b,c_c_w,c_c_b

def mode_pvp(w_s,b_s,Pls,t_a_b,t_a_w):
    #w_s=white_stones,b_s,black_stones,t_a_b=thrown_aw_b,t_a_w=thrown_aw_w,Pls=Players

        chosed_stone=[]  
        n_rct_pos=[0,0]        
        dictionary_w={}
        dictionary_b={}
        preference_d={}
        p=1           #kontrola zda jdu doprava, nebo doleva při kontrole středů
        l=2
        take=[]
        take_updt=[]
        jump=False
        next_plr=False    #další hráč nehraje, dokud neřeknu, že hraje

        #hráč, který je teď na tahu
        Player_now=Pls[0]


    #BĚH PROGRAMU
        #inicializuje všechny pygame moduly
        pg.init()                                          
        
        #barvy hrací plochy
        BLACK = pg.Color('black')
        WHITE = pg.Color('white')
        
        screen = pg.display.set_mode((840, 840))        #velikost okna
        clock = pg.time.Clock()

        colors = itertools.cycle((WHITE, BLACK))        #nastavení barev
        tile_size = 100                                 #velikost čtverce
        width, height = 8*tile_size, 8*tile_size        #velikost hrací plochy
        background = pg.Surface((width, height))        #tvorba pozadí, na které se dále vykreslí šachovnice    

        #vytvoření hrací plochy
        for y in range(0, height, tile_size):        
            for x in range(0, width, tile_size):            
                rect = (x, y, tile_size, tile_size)
                clr=next(colors)                       
                pg.draw.rect(background, clr, rect)
                
                #vykreslení kamenů
                for i in range(len(w_s)):
                    if w_s[i].get_center()==[0,0]:               #pokud má střed v (0,0), pak není ve hře => nevykreslí se
                      break 
                    else:
                        pg.draw.circle(background, 'white', w_s[i].get_center(),40)                

                for i in range(len(b_s)):
                    if b_s[i].get_center()==[0,0]:
                      break
                    else: 
                        pg.draw.circle(background, 'gray', b_s[i].get_center(),40)                
              
            next(colors)
        game_exit = False
    
        #pozadí a ohraničení
        screen_update(screen,background)  

        #vytvoř seznam všech středů pro figurky -> kontrola, která tam je "barva"
        center_list_w=center_list(w_s)
        center_list_b=center_list(b_s)
        print(center_list_w)
        print(center_list_b)

        #vytvoř tahy pro všechyn figurky     

        #TVORBA SLOVNÍKU PRO BÍLÉ KAMENY
        #projdu každý kámen
        for i in range(len(w_s)):

            #každý kámen projdu do nekonečna, jelikož může dělat další a další uzly v případě jiného kamene
            while True:
                batch=Uzel(w_s[i].get_name())
                center=w_s[i].get_center()
                center1=w_s[i].get_center()      #center1, protože spojové stromy to dodrbávají
                
                check=0        #kontrola pro střed desky -> pokud nebude místo ani doleva, ani doprava, tak break          
        
                #rozhodování, zda mohu od kamene doleva, či doprava.......done
                #chybí kontrola, zda už nejsem na konci sloupce
                #chybí, kdo hraje, dle toho strom, zatím pro bílé............i pro černé done
                #chybí tvorba další stromů, pokud budu brát
                #chybí braní

                #toto jen když jdu poprvé tínto algoritmem
                #levý kraj plochy
                if center[0]==50:
                    center[0]=center[0]+100
                    center[1]=center[1]-100      
                    
                    #kontrola pro braní, zda tam není kámen na tomto místě
                    if center in center_list_w: 
                        if w_s[i].get_name() in dictionary_w:                   
                            
                                dictionary_w.pop(w_s[i].get_name())                  
                        break   #tah neexistuje, takže kámen nebude v keys -> nepůjde táhnout

                    #pokud je tam černý kámen-> budu ho brát
                    elif center in center_list_b:
                        new_center=[0,0]
                        new_center[0]=center[0]+100
                        new_center[1]=center[1]-100  

                        if (new_center in center_list_w) or (new_center in center_list_b):                      
                            
                            break
                        
                        #vyberu jméno toho kamene, přes který skáču
                        take.append(taking(b_s,center))
                        
                        #taking(center,center_list_b,center_list_w,stne,dictionary,batch,take)
                        break
                    else:
                        #přidej uzel
                        batch.pridej_uzel(Uzel(center))
                        if w_s[i].get_name() not in dictionary_w.keys():
                            dictionary_w[f"{w_s[i].get_name()}"]=[]

                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                        else:
                            dictionary_w[f"{w_s[i].get_name()}"]=[]                         #po každém tahu znova přepsat
                            
                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)                   
                        break
                    
                #pravý kraj plochy
                elif center[0]==750:
                    center[0]=center[0]-100
                    center[1]=center[1]-100    

                    #kontrola pro braní, zda tam není kámen na tomto místě
                    if center in center_list_w: 
                        if w_s[i].get_name() in dictionary_w:                        
                                dictionary_w.pop(w_s[i].get_name())                    
                        break
                    #pokud je tam černý kámen-> budu ho brát
                    elif center in center_list_b:
                        new_center=[0,0]
                        new_center[0]=center[0]-100
                        new_center[1]=center[1]-100  

                        if (new_center in center_list_w) or (new_center in center_list_b):
                            
                            break
                        take.append(taking(b_s,center))
                        
                        break
                    else:
                        #přidej uzel
                        batch.pridej_uzel(Uzel(center))
                        if w_s[i].get_name() not in dictionary_w.keys():
                            dictionary_w[f"{w_s[i].get_name()}"]=[]

                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                        else:
                            dictionary_w[f"{w_s[i].get_name()}"]=[]
                            
                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)                    
                        break

                #ve středu plochy    
                else:
                    #doleva            
                    center[0]=center[0]-100
                    center[1]=center[1]-100

                    #kontrola pro braní, zda tam není kámen na tomto místě
                    if center in center_list_w:  
                        check+=1                                                    
                        pass
                    #pokud je tam černý kámen-> budu ho brát, toto ještě upravit, chybí přidání uzlu na digonále, když skáču
                    elif center in center_list_b:
                        new_center=[0,0]
                        new_center[0]=center[0]-100
                        new_center[1]=center[1]-100

                        if (new_center[0]<0) or (new_center[1]<50):
                            
                            break

                        elif (new_center in center_list_w) or (new_center in center_list_b):
                            
                            break
                        take.append(taking(b_s,center))
                        
                        break

                    else:
                        #přidej uzel
                        batch.pridej_uzel(Uzel(center))  
                        if w_s[i].get_name() not in dictionary_w.keys():
                            dictionary_w[f"{w_s[i].get_name()}"]=[]

                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                        else:
                            dictionary_w[f"{w_s[i].get_name()}"]=[]
                            
                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)                  
                        
                    
                    
                    #doprava
                    center1[0]=center1[0]+100
                    center1[1]=center1[1]-100    

                    if center1 in center_list_w:
                        if check==1:                            
                            if w_s[i].get_name() in dictionary_w:                                                            
                                dictionary_w.pop(w_s[i].get_name())
                        break                    
                        

                    #pokud je tam černý kámen-> budu ho brát, toto ještě upravit, chybí přidání uzlu na digonále, když skáču
                    elif center1 in center_list_b:
                        new_center=[0,0]
                        new_center[0]=center1[0]+100
                        new_center[1]=center1[1]-100
                        if (new_center[0]>750) or (new_center[1]<50):
                            
                            break  

                        elif (new_center in center_list_w) or (new_center in center_list_b):
                            
                            break
                        take.append(taking(b_s,center1))
                       
                        break

                    else:
                        #přidej uzel
                        batch.pridej_uzel(Uzel(center1))                     
                                        
                        if w_s[i].get_name() not in dictionary_w.keys():
                            dictionary_w[f"{w_s[i].get_name()}"]=[]

                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                        else:
                            dictionary_w[f"{w_s[i].get_name()}"]=[]
                            
                            for dite in batch.deti:                            
                                dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                        break
    
        print(dictionary_w)
        print(preference_d)
        print(f"na řadě je hráč: {Player_now.get_name()}")

        #běh okna/programu a eventy v něm
        while not game_exit:
            for event in pg.event.get():           #dostává, co se děje, hlavně trackuje pozici myši, zaznamená i stisknutí
                #print(event)                

                #pokud kliknu na křížek            
                if event.type == pg.QUIT:
                    game_exit = True 

                #pokud kliknu
                if event.type == pg.MOUSEBUTTONDOWN:            
                    mouse_position=list(pg.mouse.get_pos())
                    mouse_position=center_mouse(mouse_position)
                    #pokud se nerovna 0,0, tak nakresli červenej kruh s prostředkem(poté zkontroluje s kruhem)
                    

                    if mouse_position!=[0,0]:                                   #pokud jsem klikl na černý čtverec
                        bol=is_true(w_s,b_s,mouse_position)                      #is true vrací boolen, proto bol
                        

                        if (bol==True)&(chosed_stone==[]):   #pokud je kámen, a zároveň jsem zatím žádný jiný nevybral -> nemohu vybrat 2 kameny
                            if Player_now==Pls[0]:
                                chosed_stone=Chosed(mouse_position,w_s,b_s,background,screen,chosed_stone,Player_now,dictionary_w,preference_d)
                            else:
                                chosed_stone=Chosed(mouse_position,w_s,b_s,background,screen,chosed_stone,Player_now,dictionary_b,preference_d)
                            
                            
                            #nová pozice pro náhradu kruhu za čtverec, při změně pozice
                            n_rct_pos[0]=mouse_position[0]-50
                            n_rct_pos[1]=mouse_position[1]-50 
                            
                                                          
                        elif (chosed_stone!=[])&(bol==False):
                            if Player_now==Pls[0]:
                                next_plr=move_stone(mouse_position,background,screen,tile_size,chosed_stone,n_rct_pos,bol,next_plr,dictionary_w,preference_d)
                            else:
                                next_plr=move_stone(mouse_position,background,screen,tile_size,chosed_stone,n_rct_pos,bol,next_plr,dictionary_b,preference_d)
                            
                    print(f"další hráč {next_plr}")
                    
                    #rozhodování o hráčích
                    if (Player_now==Pls[0])&(next_plr==True):    #pokud hráč co hraje = hráči[0], a zároveň dostaneme pokyn z fce, že hraje další hráč, pak hraje další hráč
                        #odstranění černých kamenů, než se hráči změní
                        take_updt=[]
                        take_updt.append(tk_updt_w(chosed_stone[0].get_center(),take))        #vyberu jen ten kámen, který beru
                        
                        if take_updt[0]==0:
                            print(f" {Player_now.get_name()} vzal nic")
                        else: 
                            t_a_b.append(take_updt[0].get_name())
                            print(f" {Player_now.get_name()} vzal {take_updt[0].get_name()}")
                            destroy_stone(take_updt[0].get_center(),background)              #odstranění kamene z hrací plochy
                            screen_update(screen,background)
                            if take_updt[0].get_name() in dictionary_b.keys():
                                dictionary_b.pop(take_updt[0].get_name())
                                #odebrání z w_s
                            for i in range(len(b_s)):
                                if b_s[i].get_name()==take_updt[0].get_name():
                                    del b_s[i]
                                    break
                            jump=True
                        print(t_a_b)
                        print(dictionary_b)
                        print(preference_d)
                        
                        preference_d=move_again_w(chosed_stone[0],center_list_w,preference_d,center_list_b,batch,w_s,l,p)
                        
                        print(preference_d)
                        
                        
                        if (preference_d!={}) & (jump==True):                            
                            for i in range(len(preference_d)):
                                center_ch=c_c_w(chosed_stone[0],preference_d)          #abych dostal střed druhýho kamene
                                print(center_ch)
                                take.append(taking(b_s,center_ch))
                            chosed_stone.pop(0)
                            next_plr=False                            
                            continue
                        else:                  
                            
                            chosed_stone.pop(0)
                            Player_now=Pls[1]
                            #po každém tahu aktualizace středů kamenů
                            center_list_w=center_list(w_s)
                            center_list_b=center_list(b_s)
                            preference_d={}
                            take=[]

                            #po každém tahu aktualizace slovníku
                            #TVORBA PRO ČERNÉ KAMENY, SLOVNÍK
                            #projdu každý kámen
                            for i in range(len(b_s)):

                                #každý kámen projdu do nekonečna, jelikož může dělat další a další uzly v případě jiného kamene
                                while True:
                                    batch=Uzel(b_s[i].get_name())
                                    center=b_s[i].get_center()
                                    center1=b_s[i].get_center()      #center1, protože spojové stromy to dodrbávají
                                        
                                    check=0     
                                    check_adding=False                     #kontrola pro  přidávání do pref seznamu, jelikož python je mrdka a pamatuje si to, co bylo ke klíči v jiným slovníku
                                    jump=False
                            
                                    #rozhodování, zda mohu od kamene doleva, či doprava.......done
                                    #chybí kontrola, zda už nejsem na konci sloupce
                                    #chybí, kdo hraje, dle toho strom, zatím pro bílé
                                    #chybí tvorba další stromů, pokud budu brát

                                    #toto jen když jdu poprvé tínto algoritmem
                                    #levý kraj plochy
                                    if center[0]==50:
                                        center[0]=center[0]+100
                                        center[1]=center[1]+100      
                                        
                                        #kontrola pro braní, zda tam není kámen na tomto místě
                                        if center in center_list_b: 
                                            if b_s[i].get_name() in dictionary_b:                        
                                                    dictionary_b.pop(b_s[i].get_name())                    
                                            break   #tah neexistuje, takže kámen nebude v keys -> nepůjde táhnout
                                        #pokud je tam černý kámen-> budu ho brát
                                        elif center in center_list_w:
                                            new_center=[0,0]
                                            new_center[0]=center[0]+100
                                            new_center[1]=center[1]+100                                                                            

                                            if (new_center in center_list_w) or (new_center in center_list_b):                                            
                                                
                                                break  

                                            preference_d=create_tree_b_l(b_s[i],w_s,new_center,preference_d,center_list_w,batch) 
                                            if b_s[i].get_name() in dictionary_b.keys():
                                                dictionary_b.pop(b_s[i].get_name())                                      
                                            take.append(taking(w_s,center))                                     

                                            #delete_Stone()              #odstranění kamene z hrací plochy
                                            
                                            break
                                        else:
                                            #přidej uzel
                                            batch.pridej_uzel(Uzel(center))
                                            if b_s[i].get_name() not in dictionary_b.keys():
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]                         #po každém tahu znova přepsat
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)                   
                                            break
                                        
                                    #pravý kraj plochy
                                    elif center[0]==750:
                                        center[0]=center[0]-100
                                        center[1]=center[1]+100    

                                        #kontrola pro braní, zda tam není kámen na tomto místě
                                        if center in center_list_b: 
                                            if b_s[i].get_name() in dictionary_b:
                                                
                                                    dictionary_b.pop(b_s[i].get_name())                   
                                            break
                                        #pokud je tam černý kámen-> budu ho brát
                                        elif center in center_list_w:
                                            new_center=[0,0]
                                            new_center[0]=center[0]-100
                                            new_center[1]=center[1]+100                                          

                                            if (new_center in center_list_w) or (new_center in center_list_b):
                                                
                                                break
                                            preference_d=create_tree_b_r(b_s[i],w_s,new_center,preference_d,center_list_w,batch) 
                                            if b_s[i].get_name() in dictionary_b.keys():
                                                dictionary_b.pop(b_s[i].get_name())
                                            take.append(taking(w_s,center))
                                            
                                            #delete_Stone()              #odstranění kamene z hrací plochy
                                            
                                            
                                            
                                            break
                                        else:
                                            #přidej uzel
                                            batch.pridej_uzel(Uzel(center))
                                            if b_s[i].get_name() not in dictionary_b.keys():
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)                    
                                            break

                                    #ve středu plochy    
                                    else:
                                        #doleva            
                                        center[0]=center[0]-100
                                        center[1]=center[1]+100

                                        #kontrola pro braní, zda tam není kámen na tomto místě
                                        if center in center_list_b: 
                                            check+=1                                  
                                            pass
                                        #pokud je tam černý kámen-> budu ho brát, toto ještě upravit, chybí přidání uzlu na digonále, když skáču
                                        elif center in center_list_w:
                                            new_center=[0,0]
                                            new_center[0]=center[0]-100
                                            new_center[1]=center[1]+100

                                            if (new_center[0]<50) or (new_center[1]>750):
                                                
                                                pass 

                                            elif (new_center in center_list_w) or (new_center in center_list_b):
                                                
                                                pass
                                            else:
                                                preference_d=create_tree_b_c(b_s[i],w_s,new_center,preference_d,center_list_w,batch,l) 
                                                if b_s[i].get_name() in dictionary_b.keys():
                                                    dictionary_b.pop(b_s[i].get_name())
                                                take.append(taking(w_s,center))                                        
                                                pass

                                        else:
                                            #přidej uzel
                                            check_adding=True
                                            batch.pridej_uzel(Uzel(center))
                                            if b_s[i].get_name() not in dictionary_b.keys():
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)              
                                            
                                        
                                        
                                        #doprava
                                        center1[0]=center1[0]+100
                                        center1[1]=center1[1]+100    

                                        if center1 in center_list_b:
                                            if check==1:
                                                if b_s[i].get_name() in dictionary_b:                           
                                                        dictionary_b.pop(b_s[i].get_name())                     
                                            break                   
                                            

                                        #pokud je tam černý kámen-> budu ho brát, toto ještě upravit, chybí přidání uzlu na digonále, když skáču
                                        elif center1 in center_list_w:
                                            new_center=[0,0]
                                            new_center[0]=center1[0]+100
                                            new_center[1]=center1[1]+100
                                            if (new_center[0]>750) or (new_center[1]>750):
                                                
                                                break  

                                            elif (new_center in center_list_w) or (new_center in center_list_b):
                                                
                                                break                                        
                                            
                                            preference_d=create_tree_b_c(b_s[i],w_s,new_center,preference_d,center_list_w,batch,p)  
                                            if check_adding==True:
                                                del preference_d[b_s[i].get_name()][0]
                                            if b_s[i].get_name() in dictionary_b.keys():
                                                dictionary_b.pop(b_s[i].get_name())                                                                             
                                            take.append(taking(w_s,center1))
                                            
                                            break

                                        else:
                                            #přidej uzel
                                            batch.pridej_uzel(Uzel(center1))                     
                                                            
                                            if b_s[i].get_name() not in dictionary_b.keys():
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_b[f"{b_s[i].get_name()}"]=[]
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_b[f"{b_s[i].get_name()}"].append(dite.data)
                                            break
                            print(dictionary_b)
                            print(preference_d)
                            print(f"na řadě je hráč: {Player_now.get_name()}")
                            for j in range(len(take)):
                                print(f" {Player_now.get_name()} může brát {take[j].get_name()}")
                            next_plr=False
                            


                    elif ((Player_now==Pls[1])&(next_plr==True)):                       
                        
                        take_updt=[]
                        take_updt.append(tk_updt_b(chosed_stone[0].get_center(),take))
                        
                        if take_updt[0]==0:
                                print(f" {Player_now.get_name()} vzal nic") 
                        else:
                                t_a_w.append(take_updt[0].get_name())
                                print(f" {Player_now.get_name()} vzal {take_updt[0].get_name()}")
                                destroy_stone(take_updt[0].get_center(),background)              #odstranění kamene z hrací plochy
                                screen_update(screen,background)

                                if take_updt[0].get_name() in dictionary_w.keys():
                                    dictionary_w.pop(take_updt[0].get_name())
                                    #odebrání z w_s
                                for i in range(len(w_s)):
                                    if w_s[i].get_name()==take_updt[0].get_name():
                                        del w_s[i]
                                        break
                                    jump=True

                        print(t_a_w)
                        print(dictionary_w)
                        
                        
                        preference_d=move_again_b(chosed_stone[0],center_list_w,preference_d,center_list_b,batch,b_s,l,p)
                        
                        print(preference_d)
                        
                        
                        if (preference_d!={}) & (jump==True):                            
                            for i in range(len(preference_d)):
                                center_ch=c_c_b(chosed_stone[0],preference_d)          #abych dostal střed druhýho kamene
                                
                                take.append(taking(w_s,center_ch))
                            chosed_stone.pop(0)
                            next_plr=False                            
                            continue                                                 

                        else:
                            chosed_stone.pop(0)
                            Player_now=Pls[0]
                            
                            center_list_w=center_list(w_s)
                            center_list_b=center_list(b_s)
                            preference_d={}
                            take=[]

                            #TVORBA SLOVNÍKU PRO BÍLÉ KAMENY
                            #projdu každý kámen
                            for i in range(len(w_s)):

                                #každý kámen projdu do nekonečna, jelikož může dělat další a další uzly v případě jiného kamene
                                while True:
                                    batch=Uzel(w_s[i].get_name())
                                    center=w_s[i].get_center()
                                    center1=w_s[i].get_center()      #center1, protože spojové stromy to dodrbávají
                                                    
                                    check=0        #kontrola pro střed desky -> pokud nebude místo ani doleva, ani doprava, tak break 
                                    check_adding=False   
                                    jump=False      
                            
                                    #rozhodování, zda mohu od kamene doleva, či doprava.......done
                                    #chybí kontrola, zda už nejsem na konci sloupce
                                    #chybí, kdo hraje, dle toho strom, zatím pro bílé............i pro černé done
                                    #chybí tvorba další stromů, pokud budu brát
                                    #chybí braní

                                    #toto jen když jdu poprvé tínto algoritmem
                                    #levý kraj plochy
                                    if center[0]==50:
                                        center[0]=center[0]+100
                                        center[1]=center[1]-100      
                                        
                                        #kontrola pro braní, zda tam není kámen na tomto místě
                                        if center in center_list_w: 
                                            if w_s[i].get_name() in dictionary_w:                   
                                                
                                                    dictionary_w.pop(w_s[i].get_name())                  
                                            break   #tah neexistuje, takže kámen nebude v keys -> nepůjde táhnout

                                        #pokud je tam černý kámen-> budu ho brát
                                        elif center in center_list_b:
                                            new_center=[0,0]
                                            new_center[0]=center[0]+100
                                            new_center[1]=center[1]-100                                         

                                            if (new_center in center_list_w) or (new_center in center_list_b):
                                                
                                                break   
                                            preference_d=create_tree_w_l(w_s[i],w_s,new_center,preference_d,center_list_w,batch) 
                                            if w_s[i].get_name() in dictionary_w.keys():
                                                dictionary_w.pop(w_s[i].get_name())                                    
                                            #vyberu jméno toho kamene, přes který skáču
                                            take.append(taking(b_s,center))                              
                                                
                                            #delete_Stone()              #odstranění kamene z hrací plochy
                                            
                                            
                                            
                                            break
                                        else:
                                            #přidej uzel
                                            batch.pridej_uzel(Uzel(center))
                                            if w_s[i].get_name() not in dictionary_w.keys():
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]                         #po každém tahu znova přepsat
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)                   
                                            break
                                        
                                    #pravý kraj plochy
                                    elif center[0]==750:
                                        center[0]=center[0]-100
                                        center[1]=center[1]-100    

                                        #kontrola pro braní, zda tam není kámen na tomto místě
                                        if center in center_list_w: 
                                            if w_s[i].get_name() in dictionary_w:                        
                                                    dictionary_w.pop(w_s[i].get_name())                    
                                            break
                                        #pokud je tam černý kámen-> budu ho brát
                                        elif center in center_list_b: 
                                            new_center=[0,0]
                                            new_center[0]=center[0]-100
                                            new_center[1]=center[1]-100                                        

                                            if (new_center in center_list_w) or (new_center in center_list_b):
                                                
                                                break  
                                            preference_d=create_tree_w_r(w_s[i],w_s,new_center,preference_d,center_list_w,batch) 
                                            if w_s[i].get_name() in dictionary_w.keys():
                                                dictionary_w.pop(w_s[i].get_name())                                     
                                            take.append(taking(b_s,center))                                      
                                            break

                                        else:
                                            #přidej uzel
                                            batch.pridej_uzel(Uzel(center))
                                            if w_s[i].get_name() not in dictionary_w.keys():
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)                    
                                            break

                                    #ve středu plochy  
                                    
                                    else:
                                        #doleva            
                                        center[0]=center[0]-100
                                        center[1]=center[1]-100
                                        

                                        #kontrola pro braní, zda tam není kámen na tomto místě
                                        if center in center_list_w:  
                                            check+=1                                                    
                                            pass
                                        #pokud je tam černý kámen-> budu ho brát, toto ještě upravit, chybí přidání uzlu na digonále, když skáču
                                        elif center in center_list_b:
                                            new_center=[0,0]
                                            new_center[0]=center[0]-100
                                            new_center[1]=center[1]-100

                                            if (new_center[0]<50) or (new_center[1]<50):
                                                
                                                pass 

                                            elif (new_center in center_list_w) or (new_center in center_list_b):
                                                check+=1
                                                pass 
                                            else:
                                                preference_d=create_tree_w_c(w_s[i],w_s,new_center,preference_d,center_list_b,batch,l) 
                                                if w_s[i].get_name() in dictionary_w.keys():
                                                    dictionary_w.pop(w_s[i].get_name())                                     
                                                take.append(taking(b_s,center))
                                            
                                                pass

                                        else:
                                            #přidej uzel
                                            check_adding=True
                                            batch.pridej_uzel(Uzel(center))  
                                            if w_s[i].get_name() not in dictionary_w.keys():
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)                  
                                            
                                        
                                        
                                        #doprava
                                        center1[0]=center1[0]+100
                                        center1[1]=center1[1]-100
                                        

                                        if center1 in center_list_w:
                                            if check==1:
                                                if w_s[i].get_name() in dictionary_w:                            
                                                        dictionary_w.pop(w_s[i].get_name())
                                            break                    
                                            

                                        #pokud je tam černý kámen-> budu ho brát, toto ještě upravit, chybí přidání uzlu na digonále, když skáču
                                        elif center1 in center_list_b:  
                                            new_center=[0,0]
                                            new_center[0]=center1[0]+100
                                            new_center[1]=center1[1]-100
                                            if (new_center[0]>750) or (new_center[1]<50):
                                                
                                                break  

                                            elif (new_center in center_list_w) or (new_center in center_list_b):
                                                
                                                break    
                                            preference_d=create_tree_w_c(w_s[i],w_s,new_center,preference_d,center_list_b,batch,p) 
                                            if check_adding==True:
                                                del preference_d[w_s[i].get_name()][0]
                                            if w_s[i].get_name() in dictionary_w.keys():
                                                dictionary_w.pop(w_s[i].get_name())                                  
                                            take.append(taking(b_s,center1))
                                            
                                            break

                                        else:
                                            #přidej uzel
                                            batch.pridej_uzel(Uzel(center1))                     
                                                            
                                            if w_s[i].get_name() not in dictionary_w.keys():
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]

                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                                            else:
                                                dictionary_w[f"{w_s[i].get_name()}"]=[]
                                                
                                                for dite in batch.deti:                            
                                                    dictionary_w[f"{w_s[i].get_name()}"].append(dite.data)
                                            break
                            print(dictionary_w)
                            print(preference_d)
                            print(f"na řadě je hráč: {Player_now.get_name()}")
                            for j in range(len(take)):
                                print(f" {Player_now.get_name()} může brát {take[j].get_name()}")
                            next_plr=False
                            
                            

            pg.display.flip()                        #zobrazí display
            clock.tick(30)                          #zjistit, nemusí tu být  (pro plynulejší běh programu)      

        pg.quit()