#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import math, copy, random, logging
from common import *
from util import *
from agent import *

class Link(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.aplpha = 1
        self.gama = 1

    def update_utility(self, env):
        # aqui eu calculo o valor de um estado
        self.aplpha = self.utility_table.get(env.state, self.a) -0.1
        nextState = env.execute(env.state)[0]
        stateReward = env.execute(env.state)[1]
        # estou armazenando tambem o alpha para usarmos nas proximas multiplicacoes do estado...
        self.utility_table[state,action] = (self.aplpha, stateReward + self.gama * argmax(nextState.available_actions(nextState.state), fn) - self.utility_table.get(env.state, self.a)[1])
        # a linha de cima é aquela formula loca do q learning la
        """
        Updates the learned utility values in the agent.

        Use self.utility_table to store values

        TODO implement your solution!

        """
        #raise NotImplementedError

    def q_value(self, state, action):
        # aqui eu retorno a politica para um estado 
        return self.utility_table.get(state,action)
        """
        Return the utility for an action and/or action.

        Use self.utility_table to retrieve values

        TODO implement your solution!

        """
        #raise NotImplementedError

    def fn(self, action):
        return self.execute(a)[1]