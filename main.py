from __future__ import print_function

import random

foodRatio = 0.1
passRatio = 0.01
alpha = 1 # mutation ratio

def mutation_fusion(x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    return random.randint(max(0,x1-alpha), x2+alpha)

def randomCell():
    p = random.random()
    food = p < foodRatio
    p = random.random()
    passing = p > passRatio  
    return case(passing, food)  

class case:
    def __init__(self, passing, food):
        self.passing = passing
        
        if not self.passing and food:
            print("Error, no food on no passing")
            self.food = False
        else: 
            self.food = food

    def __str__(self):
        if self.passing:
            if self.food:
                return "F"
            else:
                return " "
        else:
            return "X"
                

class World:
    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        self.terrain = [ [randomCell() for i in range(x)] for j in range(y)] #store food and obstacles
        self.populace = [ [False for i in range(x)] for j in range(y)] #store population
        
    def __str__(self):
        s = ' '+'_'*self.y + '\n'
        for x in range(self.x):
            s += '|'
            for y in range(self.y):
                if self.populace[x][y]:
                    s += 'O'
                else:
                    s += str(self.terrain[x][y])
            s += "|\n"
        s += '|'+'-'*self.y + '|\n'
        return s
        
    def populate(self):
        x = random.randrange(0, self.x)
        y = random.randrange(0, self.y)
        while not self.terrain[x][y].passing or self.populace[x][y]:
            x = random.randrange(0, self.x)
            y = random.randrange(0, self.y)
        self.populace[x][y] = True


class Sens:
    def __init__(self, values=[1]*8):
        self.v = values
    def guess(self, terrain):
        self.v * terrain

class creature:
    def __init__(self, energy=10, speed=(1,1), sens=(Sens(),Sens())):
        self.energy = energy
        self.speed = mutation_fusion(speed[0], speed[1])
        
    def _fusion_sens(s1, s2):
        v = [0] * 8
        for i in range(8):
            v[i] = mutation_fusion(s1[i], s2[i])
        return v
        
    def step(self, terrain):
        self.energy -= self.speed*slef.speed
        
        
if __name__ == "__main__":
    w = World(10,10)
    print(w)
    for i in range(10):
        w.populate()
    print(w)
    
    
