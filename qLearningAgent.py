def getQValue(self, state, action):
        """
          Returns Q(state,action)

        """
        return self.qvalues[(state, action)] 


def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, it returns a value of 0.0.
        """
        action_values = list()
        all_actions = self.getLegalActions(state)
        if all_actions:
          for action in all_actions:
            action_values.append(self.getQValue(state, action))
          return max(action_values)
        else:
          return 0.0


def computeActionFromQValues(self, state):
        """
          Computes the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          it returns None.
        """
        action_values = list()
        all_actions = self.getLegalActions(state)
        if all_actions:
          for action in all_actions:
            action_values.append(self.getQValue(state, action))
          max_index = action_values.index(max(action_values))
          return all_actions[max_index]
        else:
          return None

        

def getAction(self, state):
        """
          Computes the action to take in the current state.  With
          probability self.epsilon it takes a random action and
          takes the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, 
          None is chosen as the action.

        """
        # Picks Action
        legalActions = self.getLegalActions(state)
        action = None
        if legalActions:
            if util.flipCoin(self.epsilon):
                action = random.choice(legalActions)
            else:
                action = self.getPolicy(state)
        return action

        return action

def update(self, state, action, nextState, reward):
        """
          Updates Q-Value

        """

        previous = reward + self.discount * self.getValue(nextState)
        self.qvalues[(state, action)] = (1.0 - self.alpha) * self.qvalues[state, action] + self.alpha * previous
