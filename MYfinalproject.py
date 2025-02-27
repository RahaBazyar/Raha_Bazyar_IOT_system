'''

APM:
Agar soali dashtid inja benevisid:

salam vaght bekheir. man hameye tabe haro kamel neveshtam, lotfan molaheze befarmaid ke agar moshkeli vojood nadasht, link ro toy telegram khedmateton ersal konam


   APM:
salam ye checke mojadad farmaeed
shoma alan dota class Device neveshtid, dota class Sensor neveshtid hamchenin class sensor niaz b tabe haye volume up va down nadare
hamchnin yeki az tabe haye admin panel dakhele class Device neveshtid



check shdo besiar awli fght task3 ( yani dot atabeye ezafi ro anujam  nadade boodid)

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
#####33-----------------------------------------------
class admin_panel():  
    def __init__(self):  
        self.groups={}  
        self.all_devices = []   
    def create_group(self,group_name):  
        if group_name not in self.groups:  
            self.groups[group_name]=[]  
            print(f'group {group_name} is created')  
        else:  
            print('your name is dublicated')  
    def add_device_to_group(self,group_name,device):  
        if group_name in self.groups:  
            self.groups[group_name].append(device)  
            self.all_devices.append(device) 
        else:  
            print('your group is not created')  
    def create_device(self,group_name,device_type,name):  
        if group_name in self.groups:  
            topic=f'loction/{group_name}/{device_type}/{name}'  
            new_device=Device(topic)  
            self.add_device_to_group(group_name, new_device)  
        else:  
            print('your group is not created')    
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):  
        if group_name in self.groups:  
            for i in range(1,number_of_devcies+1):  
                device_name=f'{device_type}{i}'  
                topic=f'location/{group_name}/{device_type}/{device_name}'  
                new_device=Device(topic)  
                self.add_device_to_group(group_name, new_device)  
        else:  
            print('your group is not created')   
    def get_devices_in_groups(self,group_name):  
        if group_name in self.groups:  
            return self.groups[group_name]  
        else:  
            print('Group not found') 
            return None  
    def turn_on_all_in_groups(self,group_name):  
        devices=self.get_devices_in_groups(group_name)  
        if devices:  
            for device in devices:  
                device.turn_on()
                print(f'{device.name} turned on in all groups')
    def turn_off_all_in_groups(self,group_name):  
        devices = self.get_devices_in_groups(group_name)  
        if devices:  
            for device in devices:  
                device.turn_off() 
                print(f'{device.name} turned off in all groups')
    def turn_on_all_devices(self):  
        for device in self.all_devices:  
            device.turn_on() 
            print(f'{device.name} turned on all devices')
    def turn_off_all_devices(self):  
        for device in self.all_devices:  
            device.turn_off()  
            print(f'{device.name} turned off all devices')
    def get_status_in_group(self, group_name):  
        devices = self.get_devices_in_groups(group_name)  
        if devices:  
            for device in devices:  
                print(f'{device.name} is {device.status}')
        else:  
            print("No devices found in this group.")  
    def create_sensor(self, sensor_type, sensor_name):  
        topic = f'location/sensors/{sensor_type}/{sensor_name}'   
        return 'new_esensor'  
    def add_sensor_in_group(self, group_name, sensor):  
        if group_name in self.groups:  
            self.groups[group_name].append(sensor)  
        else:  
            print('your group is not created')  
class Device:
    def __init__(self, topic):  
        self.topic = topic  
        self.status = "off"  
    def turn_on(self):  
        self.status = "on"  
        print(f'{self.topic} turned on')  
    def turn_off(self):  
        self.status = "off"  
        print(f'{self.topic} turned off')  
    def get_data_from_sensor_in_group(self, group_name):  
           devices = self.get_devices_in_groups(group_name) 
           for device in devices: 
               if devices:
                   print(f'Data from {device.topic}: {device.read_data()}')
               else:
                   print("No devices found in this group of yours")


##task 3 -- volume up va volume down
class Sensor:  
    def __init__(self, topic):  
        self.topic = topic  
    def read_data(self):  
        return "Sensor data here"  
    def volume_up(self):
        print(f'{self.topic} volume is up')
    def volume_down(self):
        print(f'{self.topic} volume is down')
    def timer(self):
        print(f'{self.topic} timer is running')

