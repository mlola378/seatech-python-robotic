from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def debut_mission(self, mission):
        pass

    @abstractmethod
    def arret_mission(self, mission):
        pass
    

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def voler(self):
        pass

    @abstractmethod
    def atterir(self):
        pass

    

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def avancer(self):
        pass

    @abstractmethod
    def arret_vehicule(self):
        pass
    

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def plonger(self):
        pass

    @abstractmethod
    def surface(self):
        pass

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def debut_mission(self, mission):
        print("Début de la mission en l'air :", mission)

    def voler(self):
        print("Envole du véhicule")

    def atterir(self):
        print("Atterissage du véhicule")

    def arret_mission(self):
        print("Arrêt de la mission en l'air")
    pass

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def debut_mission(self, mission):
        print("Début de la mission dans l'eau :", mission)

    def plonger(self):
        print("Plongeon du véhicule dans l'eau")

    def surface(self):
        print("Remonte du véhicule à la surface")

    def arret_mission(self):
        print("Arrêt de la mission dans l'eau")
    pass

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    def debut_mission(self, mission):
        print("Début de la mission au sol :", mission)

    def avancer(self):
        print("Avance du véhicule au sol")

    def arret_vehicule(self):
        print("Arrêt du véhicule au sol")

    def arret_mission(self):
        print("Arrêt de la mission au sol")
    pass


if __name__ == '__main__':
    uav = UAV()
    uav.debut_mission('fais exploser les Marsiens')
    uav.voler()
    uav.atterir()
    uav.arret_mission()
    print()

    ugv = UGV()
    ugv.debut_mission('recupère de la monnaie')
    ugv.avancer()
    ugv.arret_vehicule()
    ugv.arret_mission()
    print()

    uuv = UUV()
    uuv.debut_mission('tue les méchants')
    uuv.plonger()
    uuv.surface()
    uuv.arret_mission()
    print()