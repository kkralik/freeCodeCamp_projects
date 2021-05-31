class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
        
    def set_width(self, w):
        self.width = w
        
    def set_height(self, h):
        self.height = h
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def get_area(self):
        return self.get_width()*self.get_height()
    
    def get_perimeter(self):
        return 2*self.get_width() + 2*self.get_height()

    def get_diagonal(self):
        return ((self.get_width()**2 + self.get_height()**2)** 0.5)

    def get_picture(self):
        if self.get_height() > 50 or self.get_width() > 50:
            return "Too big for picture."
        else:
            pic = ''
            for h in range(self.get_height()):
                pic += "{0:*<{w}}\n".format('', w = self.get_width())
            return pic
    
    def get_amount_inside(self, other):
        side_by_side = self.get_width() // other.get_width()
        besides = self.get_height() // other.get_height()
        return side_by_side * besides
        
    def __str__(self):
        s = "Rectangle(width={0}, height={1:})".format(self.get_width(), self.get_height())
        return s
        

class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)
        
    def set_side(self,s):
        self.side = s
        self.width = s
        self.height = s
    
    def get_side(self):
        return self.side
        
    def set_width(self, width):
        self.set_side(width)
        
    def set_height(self, height):
        self.set_side(height)
    
    def __str__(self):
        s = "Square(side={0:})".format(self.get_side())
        return s
