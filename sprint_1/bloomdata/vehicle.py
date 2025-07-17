#Imagine I want to list these vehicles on craigslist
# The more specific class is called the "child" class
# Convertible inherits from Vehicle
class Convertible(Vehicle):

    def __init__ (self,make,model,color,year,mileage, top_down=True):
        super(). __init__(make, model, color, year, mileage)
        self.top_down = top_down
 
    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        else:
            self.top_down = True  
    
    def __repr__ (self):
        return f"A {self.color} {self.year} {self.make} {self.model} Convertible with {self.mileage} miles"
        

if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Avalon', 'Silver', '2007', 290000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())  
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)

    print(my_vehicle)

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status)
    print(my_vehicle.top_down)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))

x=1
print(x)

def bad():print("not good")




