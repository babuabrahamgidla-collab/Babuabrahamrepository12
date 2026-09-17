print("Hello World")
print("Hello OOPs World 1Sep")

class MyCar:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage =mileage
        
    def car_make_model_year(self):
        return f"{self.make}, {self.model}, {self.year}, the mileage is {self.mileage}"
    def car_start(self):
        print(f"The car has started")
    def car_running(self):
        print(f"The car is running")
    def car_stop(self):
        print(f"the car has stopped")

class MyHybridCar(MyCar):
    def __init__(self, make, model, year, mileage, batterycapacity, batteryhealth, enginemode):
        super().__init__(make, model, year, mileage)
        self.batterycapacity = batterycapacity
        self.enginemode = enginemode
        self.batteryhealth = batteryhealth
        self.batterytempindegC = 25
        
    def updateenginemode(self):
        if self.batterycapacity<20:
            self.enginemode = "Gas"
        elif self.batterycapacity<50:
            self.enginemode= "Hybrid"
        else:
            self.enginemode = "EV"                 

  
    def carstatus(self):
        return f"{self.car_make_model_year()}, battery charge is {self.batterycapacity:.1f}, battery health is {self.batteryhealth}, battery temperature, {self.batterytempindegC:.1f}, current operating mode is {self.enginemode}"

    def driving_charge(self, km):
        for i in range(km):
            if self.batterycapacity>0:
                drain = .5
                self.batterycapacity -= drain
                if self.batterycapacity<0:
                    self.batterycapacity = 0              
        heat_factor = (100- self.batteryhealth)/100
        self.batterytempindegC +=.1+ heat_factor*.05
        self.mileage += km
        self.batterydegradation()
        self.updateenginemode()
        
    def socket_charge(self, duration):
        for dur in range (duration):
            if self.batterycapacity <100:
                charge = 5*duration
                self.batterycapacity += charge
                if self.batterycapacity >100:
                   self.batterycapacity = 100    
        heat_factor = (100- self.batteryhealth)/100
        self.batterytempindegC +=1+ heat_factor*.2
        self.updateenginemode()
    def breaking_regen(self, km):
        regen = km*.3
        self.batterycapacity += regen
        heat_factor = (100- self.batteryhealth)/100
        self.batterytempindegC +=.05+heat_factor*.02
        self.updateenginemode()
        
    def maintenencecheck(self):
        if self.mileage<50000:
            print("no major repair required")
        elif self.mileage<100000:
            print("Basic service is required")
        elif self.mileage<150000:
                    print("Hybrid system service is required")
        elif self.mileage<200000:
                    print("Battery fan service is required")
        else:
             self.mileage>200000
             print("Hybrid battery service is required")
                    
    def batterydegradation(self):
        degradation = self.mileage //10000
        self.batteryhealth = max(100-degradation, 50)
        if self.batterycapacity > self.batteryhealth:
            self.batterycapacity = self.batteryhealth
            
    def checkoverheat(self):
         if self.batterytempindegC > 60:
             print("temperature is hgh so swithced to gas mode")
             self.batterycapacity -= 5
             if self.batterycapacity <0:
                 self.batterycapacity = 0
    def cool_battery(self):
        if self.batterytempindegC > 25:
            self.batterytempindegC -= .5
            if self.batterytempindegC <25:
               self.batterytempindegC = 25
 
               
mycarobj = MyHybridCar("Toyota","Camry", 2009, 0, 100, 100, "EV")
mycarobj.car_make_model_year()
mycarobj.car_running()
mycarobj.driving_charge(75)
carprenetstatus = mycarobj.carstatus()
print(carprenetstatus)
print("after charge of 2 hours")
mycarobj.socket_charge(2)
carprenetstatus = mycarobj.carstatus()
print(carprenetstatus)
mycarobj.breaking_regen(4)
carprenetstatus = mycarobj.carstatus()
print(carprenetstatus)
mycarobj.maintenencecheck()






  