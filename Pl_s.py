import csv
from Stone import stone

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