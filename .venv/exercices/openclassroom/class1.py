class Rectangle:
    def __init__(self,length,width,color ="red"):
        self.length = length
        self.width = width
        self.color= color
        
    def area(self):
        return self.length * self.width
    
    @classmethod
    def area2(cls,l,w):
        return l * w
    
    @staticmethod
    def area3(l,w):
        return l * w
        

rect = Rectangle(5,3,'#ff0000')
print(rect.area())

print(Rectangle.area2(4,2))
print(Rectangle.area3(7,40))

