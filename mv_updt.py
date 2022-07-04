import pygame as pg

def move_update():
    pg.init()
    scr.fill((60, 70, 90))               #barva pozadí    
    scr.blit(bg, (20, 20))
    #pg.font.init()
    #nastavení písmen a čísel hrací plochy
    myfont = pg.font.SysFont('Comic Sans MS', 15)
    pismena = ["A","B","C","D","E","F","G","H"]
    poz=70
    for i in pismena:
        textsurface = myfont.render(f"{i}", False, (0,0,0))
        scr.blit(textsurface,(poz,0))
        poz=poz+100

    poz=50
    for i in range(8,0,-1):        
        textsurface = myfont.render(f'{i}', False, (0,0,0))
        scr.blit(textsurface,(10,poz))
        poz=poz+100
    pass