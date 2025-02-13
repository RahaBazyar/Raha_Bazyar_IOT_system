'''
TASK 1

TASK2

TASK 3

'''
import numpy as np

class Device:  
   
    def __init__(self, topic):  
        self.topic = topic  
        self.topic_list = topic.split('/')      
        self.location = self.topic_list[0] 
        self.group = self.topic_list[1]     
        self.device_type = self.topic_list[2]   
        self.name = self.topic_list[3]     
        print(f'Device {self.name} initialized with topic {self.topic}')
        
    def turn_on(self):
        self.status = 'on'
        print(f'Device {self.name} turned ON')  

    def turn_off(self):  
        self.status = 'off'  
        print(f'Device {self.name} turned OFF')  
                
    def get_status(self): 
        print(f'{Device.name} status is {Device.get_status()}')
        return self.status  

a1 = Device(topic='home/parking/lamps/lamp9')  
print(f'Topic: {a1.topic}')  
print(f'Name: {a1.name}')  
print(f'Device Type: {a1.device_type}')  
print(f'Group: {a1.group}')  
print(f'Location: {a1.location}')
    
class Sensor:  
    def __init__(self, name, group, unit, pin):  
        self.name = name  
        self.group = group  
        self.unit = unit  
        self.pin = pin  
        self.current_value = None
        
    def read_sensor(self):
        return np.random.uniform(20,25)

