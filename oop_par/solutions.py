# class Car:
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         self.total_car += 1
    
#     def get_brand(self):
#         return self.__brand

#     def fullname(self):
#         return f"{self.model} from {self.__brand}"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"

    


# class Electric_car(Car):
#     def __init__(self, __brand, model, battery_size):
#         self.battery_size = battery_size
#         super().__init__(__brand, model)

#     def fullinfo(self):
#         self.mybrand = super().get_brand()
#         return f"{self.model} from {self.mybrand} and Battery MAH is {self.battery_size}"
    
#     def fuel_type(self):
#         return "Electric Charge"


# my_electric_car = Electric_car("Toyota", "Corolla", "2000 MAH")
# my_car = Car("Toyota", "Corolla")

# print(my_car.fuel_type())
# print(my_electric_car.fuel_type())