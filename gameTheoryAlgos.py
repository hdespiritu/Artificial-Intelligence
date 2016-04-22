class MinimaxAgent(MultiAgentSearchAgent):
    """
      Minimax agent 
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
        """
       
	      currDepth = 0
        currIndex = self.index
        return self.value(gameState, currIndex, currDepth)[0]
        

    def value(self, gameState, currIndex, currDepth): 
        if currIndex >= gameState.getNumAgents():
            currIndex = self.index
            currDepth += 1

        if currDepth == self.depth:
            return self.evaluationFunction(gameState)

        if currIndex == self.index:
            return self.minMaxValue(gameState, currIndex, currDepth, False)
        else:
            return self.minMaxValue(gameState, currIndex, currDepth, True)
        
    def minMaxValue(self, gameState, currIndex, currDepth, minMax):

        
        if not gameState.getLegalActions(currIndex):
            return self.evaluationFunction(gameState)
	
      	if minMax != True:        
      	    v = ("unknown", -1E400)
      	else:
      	    v = ("unknown", 1E400)
              for action in gameState.getLegalActions(currIndex):
                  if action == "Stop":
                      continue
                  
                  cmpVal = self.value(gameState.generateSuccessor(currIndex, action), currIndex + 1, currDepth)
                  if type(cmpVal) is tuple:
                      cmpVal = cmpVal[1] 

  	    if minMax != False:
                  retV = min(v[1], cmpVal)
  	    else:
  	        retV = max(v[1], cmpVal)

              if retV is not v[1]:
                  v = (action, retV) 
        
        return v

    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Minimax agent with alpha-beta pruning 
    """

    def maxValue(self, gameState, depth, agentIndex, alpha, beta):
      if len(gameState.getLegalActions(0)) == 0:
        return self.evaluationFunction(gameState)
      maxVal= -1E400
      for action in gameState.getLegalActions(0):
      	s = gameState.generateSuccessor(0, action)
              temp = self.minVal(s, depth, 1, alpha, beta)
      	if temp > beta:
                return temp

        if temp > maxVal:
          maxVal = temp
          maxAction = action

        alpha = max(alpha, maxVal)

      if depth <= 1:
        return maxAction
      else:
        return maxVal

    def minVal(self, gameState, depth, agentIndex, alpha, beta):
      
      if len(gameState.getLegalActions(0)) == 0:
        return self.evaluationFunction(gameState)
      minValue= 1E400
      for action in gameState.getLegalActions(agentIndex):
        s = gameState.generateSuccessor(agentIndex, action)

        if agentIndex == gameState.getNumAgents() - 1:
          
          if depth == self.depth:
            temp = self.evaluationFunction(s)
          else:

            temp = self.maxValue(s, depth+1, 0, alpha, beta)

        else:
          temp = self.minVal(s, depth, agentIndex+1, alpha, beta)

        if temp < alpha:
          return temp
        if temp < minValue:
          minValue = temp

        beta = min(beta, minValue)
      return minValue

    def getAction(self, gameState):
      """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
  
      return(self.maxValue(gameState, 1, 0, -1E400, 1E400))
  

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Expectimax agent 
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

        """
        
        action, cost = self.getMaxActCost(gameState, self.depth)
        return action

    def getMaxActCost(self, gameState, depth):
        maxVal = -1E400
        maxAct = gameState.getLegalActions(0)[0]
        value = 0
        for action in gameState.getLegalActions(0):
            s = gameState.generateSuccessor(0, action)
            if s.isWin() or s.isLose():
                value = self.evaluationFunction(s)
            else:
                value = self.getAverageCost(s, depth, 1)
            if value > maxVal:
                maxVal = value
                maxAct = action

        return (maxAct, maxVal)

    def getAverageCost(self, gameState, depth, agentIndex):
        actions = gameState.getLegalActions(agentIndex)
        sum = 0
        value = 0
        for action in actions:
            s = gameState.generateSuccessor(agentIndex, action)
            if s.isLose() or s.isWin():
                value = self.evaluationFunction(s)
            elif (agentIndex + 1 == gameState.getNumAgents()):
                if depth == 1:
                    value = self.evaluationFunction(s)
                else:
                    value = self.getMaxActCost(s, depth - 1)[1]
            else:
                value = self.getAverageCost(s, depth, agentIndex + 1)
            sum += value

        return float(sum) / float(len(actions))

