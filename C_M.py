def center_mouse(m_pos):
    m_pos[0]=m_pos[0]-20
    m_pos[1]=m_pos[1]-20
    #změna jen pokud klikne na černý čtverec, pro kontrolu pozice -> později kontrola se středem kruhu/kamene)
    #1.řádek
    if (100<m_pos[0]<200)&(0<m_pos[1]<100):
        m_pos=[150,50]
    elif (300<m_pos[0]<400)&(0<m_pos[1]<100):
        m_pos=[350,50]
    elif (500<m_pos[0]<600)&(0<m_pos[1]<100):
        m_pos=[550,50] 
    elif (700<m_pos[0]<800)&(0<m_pos[1]<100):
        m_pos=[750,50]   
     
    #2.řádek
    elif (0<m_pos[0]<100)&(100<m_pos[1]<200):
        m_pos=[50,150]
    elif (200<m_pos[0]<300)&(100<m_pos[1]<200):
        m_pos=[250,150]
    elif (400<m_pos[0]<500)&(100<m_pos[1]<200):
        m_pos=[450,150] 
    elif (600<m_pos[0]<700)&(100<m_pos[1]<200):
        m_pos=[650,150]

    #3.řádek 
    elif (100<m_pos[0]<200)&(200<m_pos[1]<300):
        m_pos=[150,250]
    elif (300<m_pos[0]<400)&(200<m_pos[1]<300):
        m_pos=[350,250]
    elif (500<m_pos[0]<600)&(200<m_pos[1]<300):
        m_pos=[550,250] 
    elif (700<m_pos[0]<800)&(200<m_pos[1]<300):
        m_pos=[750,250]

    #4. řádek
    elif (0<m_pos[0]<100)&(300<m_pos[1]<400):
        m_pos=[50,350]
    elif (200<m_pos[0]<300)&(300<m_pos[1]<400):
        m_pos=[250,350]
    elif (400<m_pos[0]<500)&(300<m_pos[1]<400):
        m_pos=[450,350] 
    elif (600<m_pos[0]<700)&(300<m_pos[1]<400):
        m_pos=[650,350]

    #5.řádek 
    elif (100<m_pos[0]<200)&(400<m_pos[1]<500):
        m_pos=[150,450]
    elif (300<m_pos[0]<400)&(400<m_pos[1]<500):
        m_pos=[350,450]
    elif (500<m_pos[0]<600)&(400<m_pos[1]<500):
        m_pos=[550,450] 
    elif (700<m_pos[0]<800)&(400<m_pos[1]<500):
        m_pos=[750,450]

    #6. řádek
    elif (0<m_pos[0]<100)&(500<m_pos[1]<600):
        m_pos=[50,550]
    elif (200<m_pos[0]<300)&(500<m_pos[1]<600):
        m_pos=[250,550]
    elif (400<m_pos[0]<500)&(500<m_pos[1]<600):
        m_pos=[450,550] 
    elif (600<m_pos[0]<700)&(500<m_pos[1]<600):
        m_pos=[650,550]

    #7.řádek 
    elif (100<m_pos[0]<200)&(600<m_pos[1]<700):
        m_pos=[150,650]
    elif (300<m_pos[0]<400)&(600<m_pos[1]<700):
        m_pos=[350,650]
    elif (500<m_pos[0]<600)&(600<m_pos[1]<700):
        m_pos=[550,650] 
    elif (700<m_pos[0]<800)&(600<m_pos[1]<700):
        m_pos=[750,650]

    #8. řádek
    elif (0<m_pos[0]<100)&(700<m_pos[1]<800):
        m_pos=[50,750]
    elif (200<m_pos[0]<300)&(700<m_pos[1]<800):
        m_pos=[250,750]
    elif (400<m_pos[0]<500)&(700<m_pos[1]<800):
        m_pos=[450,750] 
    elif (600<m_pos[0]<700)&(700<m_pos[1]<800):
        m_pos=[650,750]
    else:
        m_pos=[0,0]
        
    return m_pos