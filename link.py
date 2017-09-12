#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import math, copy, random, logging
from common import *
from util import *
from agent import *

class Link(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.gama = 0.7
        self.alpha = 0.9
        self.env = None
        self.alpha_table = {}

    def update_utility(self, env):
        if self.prev_a == None:
            return

        value = 1

        if self.alpha_table.get((self.prev_s,self.prev_a)) is None:
            self.alpha_table[(self.prev_s,self.prev_a)] = value
        else:
            value = self.alpha_table.get((self.prev_s,self.prev_a)) + 1
            self.alpha_table[(self.prev_s,self.prev_a)] = value

        prev_u = self.utility_table.get((self.prev_s,self.prev_a))
        if prev_u == None:
            prev_u = 0

        future_u = self.utility_table.get((self.s,self.a))
        if future_u == None:
            future_u = 0

        self.utility_table[(self.prev_s,self.prev_a)] = prev_u + (self.alpha/value) * (self.r + self.gama * future_u - prev_u)

    #print 'prev_u: {} self.r: {} future_u: {} result: {} '.format(prev_u, self.r, future_u, prev_u + self.alpha * (self.r + self.gama * future_u - prev_u))

    def q_value(self, state, action):
        a = self.utility_table.get((state,action))
        if a == None:
            return 0
        return a


    def fn(self, action):
        return self.env.execute(action)



