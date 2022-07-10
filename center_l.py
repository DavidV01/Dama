from Stone import stone

def center_list(stones):
    list=[]
    for i in range(len(stones)):
        list.append(stones[i].get_center())

    return list