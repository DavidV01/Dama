class stone:
    def __init__(self,name,color, center, radius):
        self._name = name
        self._center = center
        self._radius = radius        
        self._color=color    
    
    
    def vypis(self):
        print(str(self._name))
        print(list(self._center))
        print(str(self._radius))        
        print(str(self._color))
        return "\n"

    def get_name(self):
        return self._name
   

    def center(self,center):
        self._center=center
    
    def get_center(self):
        return(list(self._center))

    def get_color(self):
        return self._color