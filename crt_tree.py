from Stone import stone
from Is_st import is_there
#from take import taking


#STROM PRO KAŽDOU FIGURU!!!!!!!!!!!!!!  
class Uzel():

    def __init__(self, data):
        self.data = data
        self.deti = []

    def pridej_uzel(self, uzel):
        self.deti.append(uzel)

#zatím jen pro bílé....i pro černé done
#seznam středů...........done
def create_tree_b_l(stone,other_stones,center,d,c_l_w,batch):    

    while True: #nekonečná tvorba uzlů, ukončena v programu        
        print(stone.get_name())
        print(center)
        
        if center[1]==750:   #pokud jsem na konci, nemohu skákat dál, budu se měnit na dámu, tak přidej do slovníku tah
            batch.pridej_uzel(Uzel(center))
            if stone.get_name() not in d.keys():
                d[f"{stone.get_name()}"]=[]

                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)
                
            else:
                d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                            
                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)                   
            break


        else:
            batch.pridej_uzel(Uzel(center))
            if stone.get_name() not in d.keys():
                d[f"{stone.get_name()}"]=[]

                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)
                
            else:
                d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                            
                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)                   
            break

    return d


def create_tree_b_r(stone,other_stones,center,d,c_l_w,batch):
    while True: 

        batch.pridej_uzel(Uzel(center))
        if stone.get_name() not in d.keys():
            d[f"{stone.get_name()}"]=[]

            for dite in batch.deti:                            
                d[f"{stone.get_name()}"].append(dite.data)
                    
        else:
            d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                                
            for dite in batch.deti:                            
                d[f"{stone.get_name()}"].append(dite.data)                   
        break

    return d




def create_tree_b_c(stone,other_stones,center,d,c_l_w,batch,r):
        new_center=[0,0]
        if r==1:
                new_center[0]=center[0]-100
                new_center[1]=center[1]-100
        elif r==2:
                new_center[0]=center[0]+100
                new_center[1]=center[1]-100
        
    
        while True:            
            
            if new_center in c_l_w:
                
                if center[1]==750 or center[0]==750 or center[0]==50:   #pokud jsem na konci, nemohu skákat dál, budu se měnit na dámu, tak přidej do slovníku tah
                        batch.pridej_uzel(Uzel(center))
                        if stone.get_name() not in d.keys():
                            d[f"{stone.get_name()}"]=[]

                            for dite in batch.deti:                            
                                d[f"{stone.get_name()}"].append(dite.data)
                            
                        else:
                            d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                                        
                            for dite in batch.deti:                            
                                d[f"{stone.get_name()}"].append(dite.data)                   
                        break

                batch.pridej_uzel(Uzel(center))
                if stone.get_name() not in d.keys():
                    d[f"{stone.get_name()}"]=[]

                    for dite in batch.deti:                            
                        d[f"{stone.get_name()}"].append(dite.data)
                            
                else:
                    d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                                        
                    for dite in batch.deti:                            
                        d[f"{stone.get_name()}"].append(dite.data)                   
                break
            else:
                break
        return d

def create_tree_w_l(stone,other_stones,center,d,c_l_b,batch):    

    while True: #nekonečná tvorba uzlů, ukončena v programu        
               
        
            batch.pridej_uzel(Uzel(center))
            if stone.get_name() not in d.keys():
                d[f"{stone.get_name()}"]=[]

                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)
                
            else:
                d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                            
                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)                   
            break

    return d


def create_tree_w_r(stone,other_stones,center,d,c_l_b,batch):

    while True: 

        if center[1]==50:   #pokud jsem na konci, nemohu skákat dál, budu se měnit na dámu, tak přidej do slovníku tah
            batch.pridej_uzel(Uzel(center))
            if stone.get_name() not in d.keys():
                d[f"{stone.get_name()}"]=[]

                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)
                
            else:
                d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                            
                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)                   
            break

        batch.pridej_uzel(Uzel(center))
        if stone.get_name() not in d.keys():
            d[f"{stone.get_name()}"]=[]

            for dite in batch.deti:                            
                d[f"{stone.get_name()}"].append(dite.data)
                    
        else:
            d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                                
            for dite in batch.deti:                            
                d[f"{stone.get_name()}"].append(dite.data)                   
        break

    return d

def create_tree_w_c(stone,other_stones,center,d,c_l_b,batch,r):

    while True:
        new_center=[0,0]
        if r==1:
            new_center[0]=center[0]-100
            new_center[1]=center[1]+100
        elif r==2:
            new_center[0]=center[0]+100
            new_center[1]=center[1]+100
        
        
        if new_center in c_l_b:
            #print("ha")
            if center[1]==50 or center[0]==750 or center[0]==50:   #pokud jsem na konci, nemohu skákat dál, budu se měnit na dámu, tak přidej do slovníku tah
                    batch.pridej_uzel(Uzel(center))
                    if stone.get_name() not in d.keys():
                        d[f"{stone.get_name()}"]=[]

                        for dite in batch.deti:                            
                            d[f"{stone.get_name()}"].append(dite.data)
                        
                    else:
                        d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                                    
                        for dite in batch.deti:                            
                            d[f"{stone.get_name()}"].append(dite.data)                   
                    break

            batch.pridej_uzel(Uzel(center))
            if stone.get_name() not in d.keys():
                d[f"{stone.get_name()}"]=[]

                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)
                        
            else:
                d[f"{stone.get_name()}"]=[]                         #po každém tahu znova přepsat
                                                    
                for dite in batch.deti:                            
                    d[f"{stone.get_name()}"].append(dite.data)                   
            break
        else:
            break
    return d