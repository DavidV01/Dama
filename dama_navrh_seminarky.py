import csv
import pygame as pg
import itertools

class stone:
    def __init__(self,name,color, center, radius, press=False):
        self._name = name
        self._center = center
        self._radius = radius
        self._press=press
        self._color=color
    
    def move(self, press):   #celkově vyřešit, pokud pozice myši v oblasti čtverce, kde je kruh se správnym středem, atd., atd.
        pass
    
    def vypis(self):
        print(str(self._name))
        print(list(self._center))
        print(str(self._radius))
        print(str(self._press))
        print(str(self._color))
        return "\n"

    def center(self,center):
        self._center=center
    
    def get_center(self):
        return(list(self._center))

class Queen:   #dáma, nevim, jak to nazvat
  def __innit__(self):    #narvat přes dědičnost stone, jedinej def move bude jinej a bude umět víc
    pass

class board:               #ve videu bylo, va našem návrhu asi nebude potřeba!
  def __innit__(self):
    pass
  
def is_win():      #kontrola výhry
  pass


def rules():      #fce, co kontroluje, kdo hraje, zda vybírá správný kámen/dámu, zda ten pohyb je legální => rozdělit na jednotlivý fce, jedna fce, jedna kontrola něčeho
  pass

def input_player():    #zeptá se hráče, zda hraje proti 2. hráči, či AI, ale toho se mu vytvoří soupeř, výběr barev(možná zase fce na to)
  pass

def AI():              #pro AI asi nebude potřeba class, jen fce, která bude volat ostatní, jako např.: random vyber kámen, random vyber pohyb, kterej udělám => vše bude muset kontrolovat pravidla
  pass

def load_stones(ws,bs):
    for i in range(len(ws)):
        ws[i]=stone(ws[i],"white",(0,0),40)

    for i in range(len(bs)):
        bs[i]=stone(bs[i],"white",(0,0),40)

def print_stones(ws,bs):
    for i in ws:
        print(stone.vypis(i))

    for i in bs:
        print(stone.vypis(i))
    
    return True


def place_stones(ws,bs):       #už asi veškerá kontrola hotova, chce to někoho, kdo to bude testovat
    filename="dama4.csv"
    available_positions=["a7","a5","a3","a1","b8","b6","b4","b2","c7","c5","c3","c1","d8","d6","d4","d2","e7","e5","e3","e1","f8","f6","f4","f2","g7","g5","g3","g1","h8","h6","h4","h2"]     #pozice, kde mohou být kameny
    used_positions=[]           #pro kontrolu použitých polí

    #nastavení a7 atd. centr pozice, pro vykreslení kamene na hrací plochu
    center_positions={"a7": (50,150),
                      "a5": (50,350),
                      "a3": (50,550),
                      "a1": (50,750),
                      "b8": (150,50),
                      "b6": (150,250),
                      "b4": (150,450),
                      "b2": (150,650),
                      "c7": (250,150),
                      "c5": (250,350),
                      "c3": (250,550),
                      "c1": (250,750),
                      "d8": (350,50),
                      "d6": (350,250),
                      "d4": (350,450),
                      "d2": (350,650),
                      "e7": (450,150),
                      "e5": (450,350),
                      "e3": (450,550),
                      "e1": (450,750),
                      "f8": (550,50),
                      "f6": (550,250),
                      "f4": (550,450),
                      "f2": (550,650),
                      "g7": (650,150),
                      "g5": (650,350),
                      "g3": (650,550),
                      "g1": (650,750),
                      "h8": (750,50),
                      "h6": (750,250),
                      "h4": (750,450),
                      "h2": (750,650)
                      }

    #pomocné proměnné, pro pohyb v class stone
    b_count=0
    w_count=0

    #otevření csv
    with open(filename,"r") as csvfile:
        csvreader =list(csv.reader(csvfile,delimiter=';'))    
    
        #chyba vstupu csv
        if len(csvreader)>25:                                             #špatný formát (veliksot) souboru
            raise Exception("špatný vstup csv!")
            
        for i in range(1,len(csvreader)):                       
            #kontrola kamenů
            if ((csvreader[i][0] in available_positions)&(csvreader[i][0] not in used_positions) & (csvreader[i][1]=="w")):       #v pořádku, políčko ano, barva ano, too políčko není použité
                ws[w_count].center(center_positions[csvreader[i][0]])                #pokud list out of range, jen vyhodit chybu, máme max 12 kamenů, pokud víc, je to automaticky chyba
                w_count=w_count+1
                used_positions.append(csvreader[i][0])
            elif ((csvreader[i][0] in available_positions)&(csvreader[i][0] not in used_positions)& (csvreader[i][1]=="b")):         #v pořádku, políčko ano, barva ano                
                bs[b_count].center(center_positions[csvreader[i][0]])
                b_count=b_count+1
                used_positions.append(csvreader[i][0])
            else:                
                raise Exception("špatný vstup csv!")
                        
        return True


def main():
    #názvy pro kameny
    w_stones = ["W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12"]
    b_stones = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12"]

    load_stones(w_stones,b_stones)

    print_stones(w_stones,b_stones)

    if place_stones(w_stones,b_stones)==True:    
        print_stones(w_stones,b_stones)

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
                    print(w_stones[i].get_center())
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
        screen.fill((60, 70, 90))               #barva pozadí    
        screen.blit(background, (20, 20))       #velikost ohraničení

        #nastavení písmen a čísel hrací plochy
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 15)
        pismena = ["A","B","C","D","E","F","G","H"]
        poz=70
        for i in pismena:
            textsurface = myfont.render(f"{i}", False, (0,0,0))
            screen.blit(textsurface,(poz,0))
            poz=poz+100

        poz=50
        for i in range(8,0,-1):        
            textsurface = myfont.render(f'{i}', False, (0,0,0))
            screen.blit(textsurface,(10,poz))
            poz=poz+100

        #běh okna/programu a eventy v něm
        while not game_exit:
            for event in pg.event.get():           #dostává, co se děje, hlavně trackuje pozici myši, zaznamená i stisknutí
                print(event)            
                if event.type == pg.QUIT:
                    game_exit = True        

            pg.display.flip()                        #zobrazí display
            clock.tick(30)                          #zjistit, nemusí tu být  (pro plynulejší běh programu)      

        pg.quit()  
            
        print_stones(w_stones,b_stones)


if __name__=="__main__":
    main()