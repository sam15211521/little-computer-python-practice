# Define the DriveBot class here!

class DriveBot:
    
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    
    
    
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count +=1
        self.id =DriveBot.robot_count
        

    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction= new_direction
    
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
        
    def all_disabled(self):
        return False
   
        
        
###
DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

#here is robot 1
robot_1 =DriveBot(10, 180, 20)



#robot_1.motor_speed = 5
#robot_1.direction =90
#robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)
print(robot_1.latitude)
print(robot_1.longitude)
print(robot_1.robot_count)



print('''
###
''')
#Create robot_2 here!
robot_2 = DriveBot(35,75,25)



print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)
print(robot_2.latitude)
print(robot_2.longitude)

#robot 3
robot_3 = DriveBot(20, 60, 10)
print('''
###
''')
print(robot_3.motor_speed)
print(robot_3.direction)
print(robot_3.sensor_range)
print(robot_3.latitude)
print(robot_3.longitude)
print(robot_3.all_disabled)


print(robot_1.id)
print(robot_2.id)
print(robot_3.id)