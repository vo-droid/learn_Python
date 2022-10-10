


# class car():
#     def __init__(self, type):
#         self.type=type 
        
# class Petrolcar(car):
#     def __init__(self,type):
#         self.type=type

# car = Car("CUV")
# car.properties={"color","red","gear","auto","capacity":6}          # Liskov SP не рабочий вариант 

# petrol_car=petrolcar("sedan")
# petrol_car.properties=("blue","manual":4)

# cars=[car,petrol_car]

# def find_cars():
#     red_cars=0
#     for car in cars:
#         if car.properties['color']=="red":
#             red_cars += 1
#         print(f'number of red cars={red_cars}')

# find_cars(cars)




class Car():
  def __init__(self, type):
    self.type = type
    self.car_properties = {}
  
  def set_properties(self, color, gear, capacity):
    self.car_properties = {"Color": color, "Gear": gear, "Capacity": capacity}

  def get_properties(self):
    return self.car_properties

class PetrolCar(Car):
  def __init__(self, type):
    self.type = type
    self.car_properties = {}

car = Car("CUV")
car.set_properties("Red", "Auto", 6)

petrol_car = PetrolCar("Sedan")
petrol_car.set_properties("Blue", "Manual", 4)

cars = [car, petrol_car]

def find_red_cars(cars):
  red_cars = 0
  for car in cars:
    if car.get_properties()['Color'] == "Red":
      red_cars += 1
  print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)