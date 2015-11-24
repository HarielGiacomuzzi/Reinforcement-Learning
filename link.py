#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import math, copy, random, logging
from common import *
from util import *
from agent import *

class Link(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.gama = 0.5
        self.env = None

    def update_utility(self, env):
        # aqui eu calculo o valor de um estado
        if self.prev_a == None:
            return

        s = self.prev_s
        a = self.prev_a
        flag = False
        best_s = None
        stateReward = 0
        alpha = 1
        while True:
            best_r = -999999
            best_a = 0 
            
            if best_s != None:
                stateReward = env.state_reward(best_s)

            for i in range(0,3):
                #print env.compute_action_result(i,s)
                if env.execute(i)[1] > best_r:
                    best_r = env.execute(i)[1]
                    best_s = env.execute(i)[0]
                    best_a = i

            aux1 = self.utility_table.get((s,a))
            if aux1 == None:
                aux1 = 0
            aux2 = self.utility_table.get((best_s,best_a))
            if aux2 == None:
                aux2 = 0

            # self.utility_table[s,a] = self.utility_table.get(s,a) + alpha*( stateReward + self.gama * self.utility_table.get(best_s,best_a) - self.utility_table.get(s,a))
            self.utility_table[(s,a)] = aux1 + alpha*( stateReward + self.gama * aux2 - aux1)

            #self.utility_table[(s,a)] = 1

            print 'A: {} B: {} Result: {} Aux1: {} '.format(self.utility_table[s,a], self.utility_table.get((s,a)), (aux1 + alpha*( stateReward + self.gama * aux2 - aux1)), aux1)
            s = best_s
            a = best_a
            alpha -= 0.01
            if flag:
                break
            if env.terminal(s) or alpha <= 0:
                flag = True

        # estou armazenando tambem o alpha para usarmos nas proximas multiplicacoes do estado...
        #print self.utility_table.values()
        #self.utility_table[env.state,self.a] = ( stateReward + self.gama * argmax(env.available_actions(nextState), self.fn)[1][1] - self.utility_table.get(env.state, self.a))
        # a linha de cima e aquela formula loca do q learning la
        """
        Updates the learned utility values in the agent.

        Use self.utility_table to store values

        TODO implement your solution!

        """
        #raise NotImplementedError

    def q_value(self, state, action):
        # aqui eu retorno a politica para um estado 
        #return self.utility_table[state,action]
        a = self.utility_table.get((state,action))
        if a == None:
            return 0
        return a
        """
        Return the utility for an action and/or action.

        Use self.utility_table to retrieve values

        TODO implement your solution!

        """
        #raise NotImplementedError

    def fn(self, action):
        return self.env.execute(action)



