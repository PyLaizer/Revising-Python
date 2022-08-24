#Exercise 9.9
# The final version of electric_car.py in the PDF

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 85

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")      
        
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"\nThis car has a gas tank of {self.gas_tank}")    

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"\nThis car has a {self.battery_size}-Kwh battery.")  

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"The car can go about {range} miles on a full charge.")  

    def upgrade_battery(self):
        if self.battery_size:
            self.battery_size = 100                        

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) 
        self.battery = Battery() 

    def fill_gas_tank(self):
        print("\nThis car doesn't need a gas tank")

my_tesla = ElectricCar("tesla","model s","2020")
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

mytoyota = ElectricCar("toyota","highlander",2018)
mytoyota.battery.get_range()
mytoyota.battery.upgrade_battery()
mytoyota.battery.get_range()
# mycar = Car("Toyota","Higlander","2018")
# mycar.fill_gas_tank()

