class Rectangle:
    def __init__(self, width, height):
        self.width= width
        self.height= height
    
    def set_width(self, width):
        self.width= width
        return self.width

    def set_height(self, height):
        self.height= height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def __str__(self):# pour affichage du nom de la classe
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_picture(self):
        number_lines= self.height
        number_etoiles= self.width
        affichage = []
       
        if number_lines > 50 or number_etoiles > 50:
            return 'Too big for picture.'

        else:
            for x in range(1, number_lines + 1):
                # * X nbre à afficher car print va à la ligne par défaut dans un for
              affichage.append('*'* number_etoiles)
              # l'utilisation de .join avec \n au début pour forcer l'assemblage en ligne
            shape = '\n'.join(affichage) + '\n'
            return shape
        
    def get_amount_inside(self, shape):
                nbre_largeur= self.width // shape.width
                nbre_longueur= self.height // shape.height
                return nbre_largeur * nbre_longueur

            

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):# pour affichage du nom de la classe
        return f'Square(side={self.width})'
        



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(Rectangle(15,10).get_amount_inside(Square(5)))
print(rect)
print(rect.get_picture())
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
