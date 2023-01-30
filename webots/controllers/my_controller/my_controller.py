
from controller import Robot, Motor, DistanceSensor, GPS
import random

class SmashBotMotor(Motor):

    def __init__(self, name=None):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        

class SmashBotMotors():
    def __init__(self, speed=None):
        self.__front_right_wheel_m = SmashBotMotor("front_right_wheel_joint")
        self.__front_left_wheel_m = SmashBotMotor("front_left_wheel_joint")
        self.__rear_right_wheel_m = SmashBotMotor("back_right_wheel_joint")
        self.__rear_left_wheel_m = SmashBotMotor("back_left_wheel_joint")
    
    def go_forward(self, speed=5):
        self.__front_right_wheel_m.setVelocity(speed)
        self.__front_left_wheel_m.setVelocity(speed)
        self.__rear_left_wheel_m.setVelocity(speed)
        self.__rear_right_wheel_m.setVelocity(speed)

    def go_backwards(self, speed=5):

        self.__front_right_wheel_m.setVelocity(-1*speed)
        self.__front_left_wheel_m.setVelocity(-1*speed)
        self.__rear_left_wheel_m.setVelocity(-1*speed)
        self.__rear_right_wheel_m.setVelocity(-1*speed)
        print("Go Back method")

    def go_left(self, speed=20):
        self.__front_right_wheel_m.setVelocity(3*speed)
        self.__front_left_wheel_m.setVelocity(-speed)
        self.__rear_left_wheel_m.setVelocity(-speed)
        self.__rear_right_wheel_m.setVelocity(3*speed)
        print("Go Left method")

    def go_right(self, speed=20):
            self.__front_right_wheel_m.setVelocity(-speed)
            self.__front_left_wheel_m.setVelocity(3*speed)
            self.__rear_left_wheel_m.setVelocity(3*speed)
            self.__rear_right_wheel_m.setVelocity(-speed)

class SmashBot(Robot):

    def __init__(self, speed=None):
        super().__init__()
        self.__motors = SmashBotMotors()
        self.__sensors = SmashBotSensors()
        self.gps = SmashBotGPS()

    def run(self, dir='forward', speed=20):
        if dir=='forward':
            self.__motors.go_forward()
        elif dir=='backwards':
            self.__motors.go_backwards()
        elif dir=='left':
            self.__motors.go_left()
        elif dir=='right':
            self.__motors.go_right()

        self.__sensors.get_sensor()
        self.__sensors.print_sensor_value()
                


class SmashBotSensor(DistanceSensor):
    def __init__(self):
        super().__init__()
        self.enable()
        #self.getValue()

class SmashBotSensors(SmashBotSensor):
    
    def __init__(self):
        self.__front_right_sensor = DistanceSensor("front right distance sensor")
        self.__front_left_sensor = DistanceSensor("front left distance sensor")
        self.__rear_right_sensor = DistanceSensor("rear right distance sensor")
        self.__rear_left_sensor = DistanceSensor("rear left distance sensor")

    def get_sensor(self):
        return [self.__front_right_sensor.getValue(),
        self.__front_left_sensor.getValue(),
        self.__rear_right_sensor.getValue(),
        self.__rear_left_sensor.getValue()]

    def print_sensor_value(self):
        print("sensor value :")
        print(self.__front_left_sensor.getValue())
    
class SmashBotGPS(GPS):
    def __init__(self):
        super().__init__('gps')


    def getGPS(self):
        return self.getValues()

    def checkGPS(self):
        borders={
            "right":2.5,
            "left":-2.5,
            "front":2.5,
            "back":-2.5
        }

        limit=0.3

        coord=self.getValues()
        long=[]

        for key,value in borders.items():
            long.append(abs(coord[0]-borders[key]))
            long.append(abs(coord[1]-borders[key]))

        long = min(long)

        if(long<limit):
            print(True)
            return True
        else:
            print(False)
            return False


robot = SmashBot()


timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    gpsVal = robot.gps.getGPS()


    robot.run("forwward")

    if(robot.gps.checkGPS()==True):
        if(turn==1):
            robot.run("right")
        else:
            robot.run("left")
    else:
        robot.run("forward")
        if(random.randint(0,1)==1):
            turn=1
        else:
            turn=0

