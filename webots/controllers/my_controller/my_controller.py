from controller import Robot, Motor, Camera, DistanceSensor, Keyboard

KEYBOARD_SAMPLING_PERIOD = 200
TIME_STEP = 64

CAMERA_SAMPLING_PERIOD = 50
CAMERA_RECOGNITION_SAMPLING_PERIOD = 100

class EpuckCamera(Camera):
    def __init__(self):
        super().__init__('camera')
        self.enable(CAMERA_SAMPLING_PERIOD)
        self.recognitionEnable(CAMERA_RECOGNITION_SAMPLING_PERIOD)
        self.__tracked_name = None

    def track_object(self, object_name):
        self.__tracked_name = object_name

    def is_tracked_object_present(self):
        objs = self.getRecognitionObjects()
        for obj in objs:
            print('I saw something !')
            print(obj)
            if self.__tracked_name == obj.get_model().decode("utf-8"):
                self.__recognized_object = obj
                return True
        return False


DISTANCE_SENSIOR_SAMPLING_PERIOD = 50

class EpuckDistanceSensor(DistanceSensor):
    def __init__(self, name):
        DistanceSensor.__init__(self, name)
        self.enable(DISTANCE_SENSIOR_SAMPLING_PERIOD)

class EpuckDistanceSensors():
    DISTANCE_THRESHOLD = 78

    def __init__(self):
        self.__front_left = EpuckDistanceSensor('ps7')
        self.__front_left2 = EpuckDistanceSensor('ps6')
        self.__front_right = EpuckDistanceSensor('ps0')
        self.__front_right2 = EpuckDistanceSensor('ps1')
    
    # Useful to debug Robot adventures
    def __str__(self):
        return "Left sensors: %s, %s\nRight sensors: %s, %s"%(
                self.__front_left.getValue(),
                self.__front_left2.getValue(),
                self.__front_right.getValue(),
                self.__front_right2.getValue()
        )

    def __repr__(self):
        return self.__str__()

    def front_left_collision_detected(self):
        return (self.__front_left.getValue() > self.DISTANCE_THRESHOLD or
                self.__front_left2.getValue() > self.DISTANCE_THRESHOLD)
    
    def front_right_collision_detected(self):
        return (self.__front_right.getValue() > self.DISTANCE_THRESHOLD or
                self.__front_right2.getValue() > self.DISTANCE_THRESHOLD)

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        self.max_speed = self.getMaxVelocity()

class SeatechRobot(Robot):
    max_speed = 60
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('front_left_wheel_joint')
        self.__leftMotor2 = RobotMotor('back_left_wheel_joint') 
        self.__rightMotor = RobotMotor('back_right_wheel_joint')
        self.__rightMotor2 = RobotMotor('front_right_wheel_joint')

    def run(self):
        self.__rightMotor2.setVelocity(15)
        self.__rightMotor.setVelocity(15)
        self.__leftMotor.setVelocity(1)
        self.__leftMotor2.setVelocity(1)

    # create the Robot instance.
robot = SeatechRobot()
while robot.step(TIME_STEP) != -1:
    robot.run()
    

