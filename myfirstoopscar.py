print("Hellow World")
print("Hello OOPS World")

class Car:
        def __init__(self, make, model,year):
            self.make = make
            self.model = model
            self.year = year
            
        def  start(self):
            print(f"{self.make} {self.model} is starting")
        def get_info(self):
            return f"{self.year} {self.make} {self.model}"
        
my_car = Car("Toyota", "Camry", 2009)

class HybridCar(Car):
    def __init__(self, make, model, year,battery_capacity, enginemode):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.engine_mode = "EV" 
    
    def eco_mode(self):
        print("The eco mode is activated")
    def hybridcarinfo(self):
        return f"{self.make} {self.model} {self.year} battery capacity is {self.battery_capacity}%"
    def hybridcarage(self):
            return 2026-self.year
        

    def drive(self, km):
        "" "Driving drains battery depending on distance"""
        drain = km*.5
        self.battery_capacity -= drain
        
        if  self.battery_capacity < 20:
            self.engine_mode = "Gas"
        elif self.battery_capacity< 50:
             self.engine_mode = "Hybrid"
        else:
            self.engine_mode = "EV"
            
        print(f"Drove {km} km. Battery now at {self.battery_capacity:.1f}%, the mode is {self.engine_mode} ")        
            
    def charge(self, amount):
        self.battery_capacity += amount
        if self.battery_capacity>100:
            self.battery_capacity = 100
        print(f"charge battery, now the charge is {self.battery_capacity}%")
    def check_inverter_pump(self):
        if self.hybridcarage()>12:
            print("Warning inverter coolant pump may need inspection")
        else:
            print("Inverter pump is working normally")
            
    def breaking(self, km):
        regen = km*.3
        self.battery_capacity +=regen
        if self.battery_capacity>100:
            self.battery_capacity = 100
        print(f"Regenerated {regen:.1f} battery is {self.battery_capacity:.1f}%")
        
             
                
my_hybrid_car = HybridCar("Toyota", "Camry", 2009,50, "EV")
my_hybrid_car.drive(10)
my_hybrid_car.charge(20)
my_hybrid_car.check_inverter_pump()
my_hybrid_car.breaking(1)  

            