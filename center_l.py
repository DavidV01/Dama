from Stone import stone

def center_list(stones,queens):
    list=[]
    for i in range(len(stones)):
        list.append(stones[i].get_center())

    for i in range(len(queens)):
        list.append(queens[i].get_center())
        
    return list