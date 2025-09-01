import copy
import random

class Hat:
    def __init__(self, **contents):
# ** pour les cas des arguments avec clés (kwargs)
        self.contents= []
        for color, number in contents.items(): #.items pour transformer les éléments de la liste en pairs 
            for _ in range(number):
                self.contents.append(color)
    
    def draw(self, number):
        if number >= len(self.contents):
            toutes_les_billes= self.contents.copy()
            self.contents.clear()

            return toutes_les_billes
#.copy() c'est pour retourner une copie du pointeur vers la liste car étant plus sûr
        
        else:
            billes_enlevees= random.sample(self.contents,k= number)

            for bille in billes_enlevees:
                self.contents.remove(bille)

            return billes_enlevees


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    compteur= 0
    for _ in range(num_experiments):
        est_succes= True
        hat_copy= copy.deepcopy(hat)
# deepcopy juste pour une copie totale
        billes_tirees= hat_copy.draw(num_balls_drawn)

        for color, nbre_attendu in expected_balls.items():
# faire une boucle sur un dictionnaire avec deux variables est beaucoup plus simple
            nbre_obtenu= billes_tirees.count(color)
            if nbre_obtenu < nbre_attendu:
                est_succes= False
                break

        if est_succes:    
            compteur += 1
    
    probabilite = compteur / num_experiments

    return probabilite

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.draw(5))
hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
