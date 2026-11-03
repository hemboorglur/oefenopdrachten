## NOAH ZEEMAN - 15494365
## NSP2 - ECPC - classes 'Een class maken'
## 3 Nov 26

quote_oog= "Yesterday is history, Tomorrow is a mystery, but Today is a gift. That is why it is called the present"
quote_opp= "Now I've becometh Death, destroyer of worlds"
quote_tob= "print('hello world')"

class Turtle:
    def __init__(self, shape):
        # print the shape of the turtle
        #print(shape)
        self.shape = shape
        #print(quote_tob) if self == 'toby'
        #print(quote_oog) if self == 'master_oogway'
        #print(quote_opp) if self == 'oppenheimer'


    def forward(self, distance):
        # print the distance that the turtle moves
        print(distance)

    def print_shape(self):
        print(self.shape)

    def is_my_name_toby(self):
        if self.shape == "toby":
            print("yes")
        else:
            print("no")

    def left(self, angle):
        # print the angle that the turtle turns counterclockwise
        print(angle)

    def do_kungfu_move(self):
        # do kungfu move
        self.forward(130)
        self.left(350)
        self.forward(60)

        print(f"{self=}")


toby = Turtle("toby")
toby.print_shape()
toby.is_my_name_toby()
master_oogway = Turtle("turtle")
print(f"{master_oogway=}")
#master_oogway.do_kungfu_move()
print(master_oogway.quote)

toby = Turtle("turtle")
print(f"{toby=}")
#toby.do_kungfu_move()
print(toby.quote)


