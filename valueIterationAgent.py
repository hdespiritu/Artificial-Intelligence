def computeQValueFromValues(self, state, action):
        """
          Computes the Q-value of a given action in a given state from the
          value function stored in self.values.
        """
        return sum([prob * (self.mdp.getReward(state, action, nextState) + 
          (self.discount * self.getValue(nextState))) for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action)])

def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          Note that if there are no legal actions, which is the case at the
          terminal state, it returns None.
        """
        if self.mdp.isTerminal(state):
            return None
        else:
            pi = list()
            all_actions = self.mdp.getPossibleActions(state)
            best_action = None
            maxqvalue = float("-inf")
            for action in all_actions:
                temp = self.getQValue(state, action)
                if temp > maxqvalue:
                    best_action = action
                    maxqvalue = temp
            return best_action