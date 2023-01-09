import time 

ROBOT_COUNT = 0


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __speaches = {'boot':'Bonjour', 'shutdown':'Byebye '}
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """

    def __init__(self, name=None):
        if name:
            self.__name = name
        self.__current_status = self.__states[0]
        self.__power = False
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    def boot(self):   
        self.__power = True
        self.__current_status = self.__states[1]
        print("%s, je suis %s j'ai %s%% de batterie"%(self.__speaches['boot'], self.__name, self.__battery_level))


    def shutdown(self):   
        self.__power = False
        self.__current_status = self.__states[0]
        self.__current_speed = 0
        print((self.__speaches['shutdown']))

    def charge(self):
        while self.__battery_level < 100:
            self.__battery_level += 10
            print("Je suis chargé à %s%%"%(self.__battery_level))
            time.sleep(1)
        if self.__battery_level > 0:
            self.__battery_level -= 5
            if self.__battery_level <= 0:
                self.battery_level = self.__power = False
                print("Je n'ai plus de batterie")

    def status(self):
        print("L'état de %s est : %s. Je possède %s%% de batterie"%(self.__name, self.__current_status, self.__battery_level))

    def stop(self):   
        self.__current_speed = 0
      
    def move(self, speed):
        if self.__current_status == 'running':
            self.__current_speed = speed
            if self.__battery_level > 0:
                self.__battery_level -= 5
                if self.__battery_level <= 0:
                    self.battery_level = self.__power = False
                    print("Je n'ai plus de batterie")


    def speed(self):
        print("J'ai une vitesse de : %s"%(self.__current_speed),"km/h") 

if __name__ == "__main__":
    robot = Robot(name = "MrRobot")
    robot.status()
    robot.boot()
    robot.status()
    robot.charge()
    robot.move(20)
    robot.status()
    robot.speed()
    robot.stop()
    robot.speed()
    robot.shutdown()



