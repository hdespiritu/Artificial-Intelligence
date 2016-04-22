def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    
    """
    
    self.features = trainingData[0].keys() 
    
    for iteration in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      for i in range(len(trainingData)):
          score = util.Counter()
          correctLabel = trainingLabels[i]

          for label in self.legalLabels:
            score[label] = self.weights[label] * trainingData[i]

          labelGuess = score.argMax()

          if labelGuess is not correctLabel:
            self.weights[labelGuess] -= trainingData[i]
            self.weights[correctLabel] += trainingData[i]
    
def classify(self, data ):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label. 

    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
    return guesses