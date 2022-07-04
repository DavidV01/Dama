#import csv
import pygame as pg
import itertools
from l_s import load_stones
from Pr_s import print_stones
from Pl_s import place_stones
from Stone import stone
from C_M import center_mouse
from updt import screen_update
#from Is_st import is_stone
#from Is_st import is_true
from move import move_stone
from Plr import Player
from Is_st import is_true
from Chosed_stone import Chosed

#stále neřeším dámu

def main():
    #názvy pro kameny
    w_stones = ["W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12"]
    b_stones = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12"] 
    chosed_stone=[]  
    n_rct_pos=[0,0]
    Players=[]

    next_plr=False    #další hráč nehraje, dokud neřeknu, že hraje

    while True:
        #zatím vše napíšu do mainu, pak rozdělit do listů!!!
        #proti komu chci hrát?
        player_question=input("Proti komu chete hrát? Pokud chcete hrát proti Botovi, napište PVE, pokud chete hrát s druhým hráčem napište PVP: ")

        #rozhodování
        if player_question=="PVP":
            pl_w_name = input("Zadej jméno 1./bílého hráče: ")
            Players.append(Player(pl_w_name,"white"))

            pl_b_name = input("Zadej jméno 2./černého hráče: ")
            Players.append(Player(pl_b_name,"gray"))
            break
        elif player_question=="PVE":
            break    
            
    #hráč, který je teď na tahu
    Player_now=Players[0]

    load_stones(w_stones,b_stones)

    
    #kontrola položení kamenů, zda je v csv vše správně atd.
    if place_stones(w_stones,b_stones)==True:
                 

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
                rectangle=pg.draw.rect(background, clr, rect)
                
                #vykreslení kamenů
                for i in range(12):
                    if w_stones[i].get_center()==[0,0]:               #pokud má střed v (0,0), pak není ve hře => nevykreslí se
                      break 
                    else:
                        pg.draw.circle(background, 'white', w_stones[i].get_center(),40)                

                for i in range(12):
                    if b_stones[i].get_center()==[0,0]:
                      break
                    else: 
                        pg.draw.circle(background, 'gray', b_stones[i].get_center(),40)                
              
            next(colors)
        game_exit = False
    
        #pozadí a ohraničení
        screen_update(screen,background)       

        #běh okna/programu a eventy v něm
        while not game_exit:
            for event in pg.event.get():           #dostává, co se děje, hlavně trackuje pozici myši, zaznamená i stisknutí
                #print(event)

                print(f"na řadě je hráč: {Player_now.get_name()}")

                #pokud kliknu na křížek            
                if event.type == pg.QUIT:
                    game_exit = True 

                #pokud kliknu
                if event.type == pg.MOUSEBUTTONDOWN:            
                    mouse_position=list(pg.mouse.get_pos())
                    mouse_position=center_mouse(mouse_position)
                    #pokud se nerovna 0,0, tak nakresli červenej kruh s prostředkem(poté zkontroluje s kruhem)

                    if mouse_position!=[0,0]:                                   #pokud jsem klikl na černý čtverec
                        bol=is_true(w_stones,b_stones,mouse_position)                      #is true vrací boolen, proto bol

                        if (bol==True)&(chosed_stone==[]):   #pokud je kámen, a zároveň jsem zatím žádný jiný nevybral -> nemohu vybrat 2 kameny
                            chosed_stone=Chosed(mouse_position,w_stones,b_stones,background,screen,chosed_stone,Player_now)
                            #nová pozice pro náhradu kruhu za čtverec, při změně pozice
                            n_rct_pos[0]=mouse_position[0]-50
                            n_rct_pos[1]=mouse_position[1]-50 
                                                          
                        elif (chosed_stone!=[])&(bol==False):
                            next_plr=move_stone(mouse_position,background,screen,tile_size,chosed_stone,n_rct_pos,bol,next_plr)
                            chosed_stone.pop(0)   #čištění vybraného kamene na prázdnou množinu

                    #rozhodování o hráčích
                    if (Player_now==Players[0])&(next_plr==True):    #pokud hráč co hraje = hráči[0], a zároveň dostaneme pokyn z fce, že hraje další hráč, pak hraje další hráč
                        Player_now=Players[1]
                        next_plr=False
                    elif (Player_now==Players[1])&(next_plr==True):
                        Player_now=Players[0]
                        next_plr=False

            pg.display.flip()                        #zobrazí display
            clock.tick(30)                          #zjistit, nemusí tu být  (pro plynulejší běh programu)      

        pg.quit()  
        
if __name__=="__main__":
    main()