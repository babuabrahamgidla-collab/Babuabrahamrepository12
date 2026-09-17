print("Hello World 4 Sep. afternoon")

class MySmartHome():
    def __init__(self, devicename):
        self.devicename = devicename
        self.status = "On"        
        self.batteryliferemains = 100
        self.device_temperature = 25
        self.health = 100
        self.energy_used = 0
        self.ambient= 22
        self.temperature_state = "normal"
        self.health_state = "normal"
               
        
    def displaycurrentstatus(self):
        print(f"Device name {self.devicename} device status is {self.status} batterylife remains {self.batteryliferemains} device temperature is {self.device_temperature} device health {self.health} ")
            
    def device_energy_use(self, energyuse_value):
        self.energy_used +=energyuse_value             
        
    def device_operating_severity(self): # Child class to implement the method
        pass              
    
    def device_temp_change(self, usageadditive):
        self.device_temperature +=usageadditive
        if self.device_temperature >60:
            self.device_temperature = 60
        if self.device_temperature - self.ambient >2:
            self.temperature_state= "not normal"
        else:
            self.temperature_state= "normal" 
            
    def device_health_degrade(self, usageadditive):
        self.health -=usageadditive
        if self.health<=50:
            self.health_state = "not normal"            
        else:
            self.health_state = "normal"
        if self.health <50:
            self.health = 50
        else:
            self.health = self.health
            
    def device_alerts(self):
        devicealerts=[]
        if  self.batteryliferemains <15:
                devicealerts.append(f"Alert {self.devicename} remaining battery life is {self.batteryliferemains} and it is low")
        if  self.device_temperature == 60:
                devicealerts.append(f"Alert {self.devicename} temperature is {self.device_temperature} and it is high")
        if  self.health ==50:
                devicealerts.append(f"Alert {self.devicename} health is {self.health} and it is low")
        if  self.temperature_state != "normal":
            devicealerts.append(f"Alert {self.devicename} temperature state is {self.temperature_state} and it is not normal")
        if  self.health_state != "normal":
            devicealerts.append(f"Alert {self.devicename} health state is {self.health_state} and it is not normal") 
        return devicealerts 
    
    def update(self):
        self.device_operating_severity()
        self.device_temp_change(0)
        self.device_health_degrade(0)
        
    def turn_on(self):
        self.status = "On"
        
    def turn_off(self):
        self.status = "Off"
    
    def summary(self):
        return f"{self.devicename}: status={self.status}, temp={self.device_temperature}, health={self.health}"
    
class MySmartLight(MySmartHome):
    def __init__(self, devicename, brightness, color):
        super().__init__(devicename)       
        self.brightness = brightness
        self.color= color 
        self.lightingmode ="'"
        self.batteryliferemains   =25 
                       
    def device_operating_severity(self):
        if  self.brightness < 20:
            self.light_operating_severity = "Low"
        elif self.brightness <50:
            self.light_operating_severity = "Normal"
        else:
            self.light_operating_severity ="Extreme"
        print(f"The operating severity of the device is {self.light_operating_severity}")
                
    def set_brightness(self, brightnessvalue): 
        self.turn_on()
        self.device_energy_use(5)
        self.brightness = brightnessvalue        
        self.device_temp_change(3)
        self.device_health_degrade(4)
        
    def set_color(self, colorvalue):       
        self.turn_on()
        self.color = colorvalue
        self.device_temp_change(2)
        self.device_health_degrade(2) 
        self.device_energy_use(2)   
        
    def set_lightingmode(self, brightnessvalue, colorvalue):
        self.brightness = brightnessvalue
        self.color = colorvalue
        self.turn_on()
        if (self.brightness <=50 and self.color == "yellow"):
                self.lightingmode = "pleasent"
        elif self.brightness<=50 and self.color == "blue":
                 self.lightmode = "party"
        elif (self.brightness >50 or self.color =="red"):
            self.lightingmode = "not pleasent"
        
        print(f"the lighting mode is {self.lightingmode}")      
                        
    def check_smartligt_code(self):
        print("Smartlight part of the code is working")      
  
    
class MySmartairconditioner(MySmartHome):
    def __init__(self, devicename, device_temperature, ambient):
        super().__init__(devicename)        
        self.device_temperature = device_temperature        
        self.ambient = ambient
        self.controlledeqpmode =""
        self.temperaturesetpoint= 0
       
    def airconditioner_operating_cycle(self, setpointvalue):
        self.temperaturesetpoint=setpointvalue
        if self.ambient-self.temperaturesetpoint>=2:
            self.turn_on()
            self.controlledeqpmode = "Cooling"            
        elif self.ambient-self.temperaturesetpoint<2:
             self.turn_on()
             self.controlledeqpmode = "Heating"
        elif abs(self.temperaturesetpoint- self.ambient) <2:
            self.controlledeqpmode = "Standing by"
            self.turn_off()
        print(f"the controlled equipment is presently {self.controlledeqpmode}")        
            
    def device_operating_severity(self):
        if self.device_temperature - self.ambient <3:
           self.airconditioner_operating_severity = "mild"
           self.device_energy_use(5)                                
        else:
            self.airconditioner_operating_severity = "agressive"
            self.device_energy_use(10)
        print(f"The air conditoner is operating {self.airconditioner_operating_severity}")
    def check_smartairconditioner_code(self):
        print("Smartairconditioner part of code is OK")
        
class MySmartventilator(MySmartHome):
    def __init__(self, devicename):
        super().__init__(devicename)
        self.humidity = 80        
        self.humiditysetpoint = 60
        
    def show_ventilatot_status(self):
        print(f"the device name is {self.devicename}, humidity is {self.humidity} the desired humidity is {self.humiditysetpoint}")
       
    def show_ventilator_operating_mode(self, humidity, humiditysetpoint):
        self.humidity = humidity
        self.humiditysetpoint = humiditysetpoint
        if self.humidity-self.humiditysetpoint>2:
            self.venti_operatingmode = "Isothermal"
            self.turn_on()            
        else:
            self.venti_operatingmode = "Adiabatic"
            self.status = "Off" 
        print(f"the ventilator oprating mode is {self.venti_operatingmode}")
        
    def device_operating_severity(self):                                   
            if self.humidity - self.humiditysetpoint<10:
                self.vent_operating_severity = "mild"           
            else:
                self.vent_operating_severity = "agressive" 
            print(f"The ventilator operating severity is {self.vent_operating_severity}")
            
                
    def check_smartventilator_code(self):
            print("Smartventilator part of code is OK")             
        
        
class MyDeviceHub():
    
    def __init__(self):
        self.mydevices=[]
        
    def add_a_device(self, device):
        self.mydevices.append(device)
        
    def list_my_devices(self):
        for dev in self.mydevices:
            print(f"{dev.devicename}")
            dev.displaycurrentstatus()
    
    def runautomationrules(self):
        for dev in self.mydevices:
            if  dev.device_temperature>50:
                print (f"{dev.devicename} is at high temp")

    def runalerts(self):
            for dev in self.mydevices:                
                alerts = dev.device_alerts()
                for alert in alerts:
                    print(alert)
                    
    def run_device_summary(self):
        for dev in self.mydevices:
            print(dev.summary())
    
    def rundeviceseverity(self):
        for dev in self.mydevices:
            dev.device_operating_severity()
    
    def runupdates(self):
        for dev in self.mydevices:
            dev.update()
    
    def dashboard(self):
        for dev in self.mydevices:
            dev.update()
        print("\n--- Smart Home Dashboard ---")
        for dev in self.mydevices:
            print(dev.summary())
        print("----------------------------\n")       
        
 
light1 =   MySmartLight("Hall light", 30, "yellow")
light1.check_smartligt_code()
light1.set_brightness(60)
light1.set_color("yellow")
light1.set_lightingmode(60, "blue")
aircooler1 = MySmartairconditioner("Hall AC" , 30, 36)
aircooler1.airconditioner_operating_cycle(20)
aircooler1.check_smartairconditioner_code() 
aircooler1.device_operating_severity()
venti1 = MySmartventilator("No sweat Magic")
venti1.show_ventilatot_status()
venti1.show_ventilator_operating_mode(90, 60)
venti1.device_operating_severity()

hub1 = MyDeviceHub()
hub1.add_a_device(light1)
hub1.add_a_device(aircooler1)
hub1.add_a_device(venti1)
hub1.list_my_devices()
hub1.runautomationrules()
hub1.runalerts()
hub1.runupdates()
hub1.rundeviceseverity()
hub1.dashboard()

print("did we survive")
        
                
        
        
        
        
                
        
            
        
        
        
       
