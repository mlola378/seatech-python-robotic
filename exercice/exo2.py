from exo1 import Robot
import time


class Human():   
    # Human class content here
    __sexe = None
    __manger = []
    
    
    def __init__(self, sexe):
        self.__sexe = sexe
    

    def manger(self, aliment):   
        if type(aliment) is str:
            aliment = [aliment]
        self.__manger += aliment
        print("J'ai mangé",' et'.join(aliment))

    def digest(self):
        for i in range (len(self.__manger)):
            print('Digestion de %s'%(self.__manger[i]))
        

    def presentation(self):
        print('Je suis un cyborg, je suis %s'%(self.__sexe))



class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)



if __name__ == '__main__':
    cyborg = Cyborg('Mr Robot', 'un homme')

    cyborg.status()
    cyborg.boot()
    cyborg.presentation()
    cyborg.charge()
    cyborg.status()
    cyborg.manger('brocolie')
    cyborg.manger(["pizza à l'ananas", 'métal'])
    cyborg.digest()
    cyborg.status()