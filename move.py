import random
import itertools
import pgzrun

WIDTH = 400
HEIGHT = 400

Block_Positions=[

    (50,50),
    (350,50),
    (350,350),
    (50,350)

]

block_positions = itertools.cycle(Block_Positions)

block = Actor("block",center=(50,50))
ship = Actor("ship2",center=(200,200))



def draw():
    screen.clear()
    ship.draw()
    block.draw()


pgzrun.go()
