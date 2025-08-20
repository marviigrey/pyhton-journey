class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print('it moves along')
    
    def get_make_model(self):
      print(f"I am a {self.make} {self.model}")

my_car = Vehicle('tesla', 'model 3')
my_car.get_make_model()
  
print(my_car.make)
print(my_car.model)


class Food:
    def __init__(self, type, state):
        self.type = type
        self.state = state

    def restaurant(self):
        print('Chicken republic')
        
    
my_food = Food('rice', 'chicken')

print(my_food.type)
print(my_food.state)

my_food.restaurant()

your_car = Vehicle('rolls-royce', 'cullinan')

your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print('Flies along')

class Truck(Vehicle):
    def moves(self):
        print('rumbles along...')
class golfCart(Vehicle):
    pass

cessna = Airplane('Cessna', 'skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = golfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon): #polymorphism
    v.get_make_model()
    v.moves()


