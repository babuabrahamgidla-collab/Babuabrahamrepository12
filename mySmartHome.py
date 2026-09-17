print("Hello World")
print("Hello OOPs World of Smart Home System")

class SmartDevice:
    def __init__(self, devicename):
        self.devicename = devicename
        self.devicestatus = "on"
        self.batterylevel = 100 
        self.devicehealth = 100
        self.temperature = 25
        self.energy_used = 0       
       
    def turn_on(self):
        self.devicestatus = "on"
    
    def turn_off(self):
            self.devicestatus = "off"    
    
    def showattributes(self):
        return f"Device is {self.devicename}, its status {self.devicestatus}, battery level {self.batterylevel}, its health {self.devicehealth}, device is now at {self.temperature} Deg C., energy usage is {self.energy_used} units" 
    
    def drain_battery(self, drainamount):
        self.batterylevel -= drainamount
        if self.batterylevel<0:
            self.batterylevel =0
            
    def degrade_health(self, degradeamount):
        self.devicehealth -=degradeamount
        if self.devicehealth<50:
            self.devicehealth=50
    
    def increase_temperature(self, amount_heating):
        self.temperature += amount_heating
        if self.temperature < 20:
            self.temperature = 20
        if self.temperature>60:
            print(f"WARNING: {self.devicename} is overheating!")
            self.devicestatus = "off"
            self.drain_battery(5)
            self.degrade_health(2)
    def cooling(self):
        if self.temperature>25:
            self.temperature -= 1
        if self.temperature<25:
            self.temperature = 25
    
    def add_energy_used(self,energyuseamount):
        self.energy_used +=energyuseamount
        
    def check_alerts(self):
        alerts=[]
        if  self.batterylevel<15:
                alerts.append(f"Alert: {self.devicename} battery level is low {self.batterylevel} ") 
        
        if  self.temperature>55:
            alerts.append(f"Alert: {self.devicename} temperature is high {self.temperature}")
            
        if self.energy_used > 10:
            alerts.append(f"Alert: {self.devicename} energy usage is high {self.energy_used}")
        
        if self.devicehealth < 60:       
            alerts.append(f"ALERT: {self.devicename} health is degrading ({self.devicehealth}%).")
        return alerts
            
    def perform_maintenance(self):
        # Improve health slightly
        if self.devicehealth<90:
            self.devicehealth +=2
        # Cool device faster during maintenance
        if self.temperature>30:
            self.temperature -=1
        # recharge battery slightly
        if self.batterylevel<50:
            self.batterylevel += 1                

         
class SmartLight(SmartDevice):
    def __init__(self, devicename, brightness=50, color="White"):
        super().__init__(devicename) 
        self.brightness = brightness
        self.color = color    
         
    def set_brightness(self, brightnessvalue):
        self.brightness = brightnessvalue
        self.drain_battery(1)
        self.degrade_health(.2)
        self.increase_temperature(.5)
        self.add_energy_used(.8)
        
    def set_color(self, colorvalue):
        self.color = colorvalue
        self.drain_battery(.5)
        self.degrade_health(.1) 
        self.increase_temperature(.2)
        self.add_energy_used(.4)
        
           
               
class SmartThermostat(SmartDevice):
    def __init__(self, devicename, temperature= 22, mode="auto"):
        super().__init__(devicename)
        self.temperature = temperature
        self.mode = mode
        
    def set_temp(self, tempvalue):
            self.temperature = tempvalue
            self.drain_battery(2)
            self.degrade_health(.3)
            self.increase_temperature(1)
            self.add_energy_used(1.5)
    
    def set_mode(self, modevalue):
            self.mode = modevalue
            self.drain_battery(1)
            self.degrade_health(.2)
            self.increase_temperature(.5)
            self.add_energy_used(.7)
            
        
        
class SmartDoorLock(SmartDevice):       
    def __init__(self, devicename):
        super().__init__(devicename)
        self.locked = True
        self.pin = []
        
       
    def lock(self):
           self.locked = True
           self.drain_battery(.5)
           self.degrade_health(1)
           self.increase_temperature(.3)
           self.add_energy_used(.3)
            
    def unlock(self):
            self.locked = False
            self.drain_battery(.5)
            self.degrade_health(1)
            self.increase_temperature(.3)
            self.add_energy_used(.3)
             
    def add_pins(self, pin):
            self.pin.append(pin)  
            self.drain_battery(.2)
            self.degrade_health(.1)
            self.increase_temperature(.1)
            self.add_energy_used(.1)           
            
class SmartHub():
    def __init__(self):
        self.devices = []
    
    def add_device(self, device):
            self.devices.append(device)
    
    def remove_device(self, device):
             self.devices.remove(device)
    
    def show_status_alldevices(self):
            for dev in self.devices:
                dev.cooling()
                print(dev.showattributes())
    def show_totalenergy_usage(self):
        total = 0
        for dev in self.devices:
            total +=dev.energy_used
        print(f"Total energy used by all devices: {total} units")
            
           
    def run_automation_rules(self):
        for dev in self.devices:
            if dev.batterylevel <10:
               dev.turn_off()
               print(f"Automation: {dev.devicename}, is turned off due to low battery") 
            if dev.temperature>50:
                dev.cooling()
                print(f"Automation: Cooling applied to {dev.devicename}.")          
            if isinstance(dev,SmartLight) and dev.energy_used>5:
                dev.set_brightness(30)
                print(f"Automation: {dev.devicename} brightness reduced due to high energy consumption.")
            if isinstance(dev, SmartDoorLock) and dev.batterylevel<20:
                dev.lock()
                print(f"Automation: {dev.devicename}, is locked as the battery level is low ")
    
    def full_system_check(self):
        print("Running automation rules")
        self.run_automation_rules()
        print("After running Automation rules the device status is as below")
        self.run_alerts_and_maintenance()
        self.show_status_alldevices()
        
    def run_alerts_and_maintenance(self):
        print("\nRunning Alerts & Maintenance...")
        for dev in self.devices:
        # Show alerts
            alerts = dev.check_alerts()
            for alert in alerts:
                print(alert)
            # Perform maintenance
            dev.perform_maintenance()
        
         
      
            
#Test           
light1 = SmartLight("Livingroom light", 70, "Warm White")
thermostat1= SmartThermostat("Frontroom thermostat", 21, "cool")
door1=SmartDoorLock("Frontroom lock")

light1.set_brightness(90)
thermostat1.set_temp(25)
door1.unlock()

hub= SmartHub()
hub.add_device(light1)
hub.add_device(thermostat1)
hub.add_device(door1)

#hub.show_status_alldevices()
hub.show_totalenergy_usage()
hub.full_system_check()

            
            