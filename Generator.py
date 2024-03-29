#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from Random import Random
from CosmicRays import CosmicRays

#################################
# Decay Class
#################################

class Decay():
    #Initialize Class
    def __init__(self, seed = 5555, events = 1000, p = [0.5,0.5], time_neg = 2.0e-6, time_pos = 2.4e-6):
        self.p = p
        self.seed = seed
        self.rand = Random(self.seed)
        self.events = events
        self.muon_n =math.ceil(p[0]*self.events)
        self.muon_p =math.floor(p[1]*self.events)
        self.time_n = time_neg
        self.time_p = time_pos

    def Update_Distribution(self,PD):
        self.p = PD
        self.muon_n =math.ceil(PD[0]*self.events)
        self.muon_p =math.floor(PD[1]*self.events)
    
    #Categorical Probability to Simulate two different muons
    def Update_Probability(self):
        distribution = []
        #Sampling from a Cateogorical
        for i in range(self.events):
            x = self.rand.Categorical(self.p)
            distribution.append(x)

        num_negative = distribution.count(0)
        num_positive = distribution.count(1)
        m=[num_negative/self.events, num_positive/self.events]
        print(m)
        self.Update_Distribution(m)

    def Time(self):
        life_n = []
        life_p = []
        
        for i in range(self.muon_n):
            t1 = self.rand.Exponential(self.time_n)
            life_n.append(t1)

        for _ in range(self.muon_p):
            t2= self.rand.Exponential(self.time_p)
            life_p.append(t2)

        lifetimes = life_n + life_p

        return life_n, life_p, lifetimes

