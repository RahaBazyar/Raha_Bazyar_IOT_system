

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

a1 = Device(topic='home/parking/lamps/lamp9')  

print(f'Topic: {a1.topic}')  
print(f'Name: {a1.name}')  
print(f'Device Type: {a1.device_type}')  
print(f'Group: {a1.group}')  
print(f'Location: {a1.location}')

