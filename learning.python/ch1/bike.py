# let's define the class Bike
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print('braking!')

# let's we crate a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the Bike class.
print(red_bike.colour)  # print: Red
print(red_bike.frame_material)  # print: Carbon fiber
print(blue.colour)  # print: blue
print(blue.frame_material)  # print: Steel

# let's brake!
red_bike.brake()    # print: braking!
