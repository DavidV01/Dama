#import csv
import pygame as pg
import itertools
from l_s import load_stones,load_queens
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
from Game_modes import mode_pvp

#STÁLE NEŘEŠÍM DÁMU!!!!!!!!!!!!!!

def main():
    #názvy pro kameny
    w_stones = ["W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12"]
    w_queens = ["DW1","DW2","DW3","DW4","DW5","DW6"]      #dáma je ze 2 kamenů, max 6 dam, v programu budu počítat zaměnu jednoho kamene za dámu -> konec jakmile len(vyhozených) bude 12

    b_stones = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12"]   
    b_queens = ["DB1","DB2","DB3","DB4","DB5","DB6"]

    Players=[]
    thrown_aw_b=[]
    thrown_aw_w=[]    
   

    

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
            
    
    #načtu kameny jako entity se svým jménem a základní pozicí (0,0)
    load_stones(w_stones,b_stones)

    load_queens(w_queens,b_queens)   

    
    #kontrola položení kamenů, zda je v csv vše správně atd.
    if place_stones(w_stones,b_stones,w_queens,b_queens)==True:
        
        #vyhození kamenů, co nejsou ve hře
        thrown_aw_w=away(w_stones,thrown_aw_w)
        thrown_aw_b=away(b_stones,thrown_aw_b)

        print(thrown_aw_w)
        print(thrown_aw_b)

        #filtrování kamenů tak, aby zbyl jen ty, co jsou ve hře
        #pro ně udělat stromy
        w_stones=filt(w_stones,thrown_aw_w)
        b_stones=filt(b_stones,thrown_aw_b) 

              


        #načtení PVP modu
        if player_question=="PVP":
            mode_pvp(w_stones,b_stones,Players,thrown_aw_b,thrown_aw_w,w_queens,b_queens)
        else:
            print("konec hry")
          
        
if __name__=="__main__":
    main()