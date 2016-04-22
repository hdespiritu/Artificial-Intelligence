def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    """
    Trains a Naive Bayes classifier by collecting counts over the training data, and
    stores the Laplace smoothed estimates so that they can be used to classify.
    Evaluate each value of k in kgrid to choose the smoothing parameter 
    that gives the best accuracy on the held-out validationData.
    
    """

    self.prior = util.Counter()
    sampleSize = len(trainingData)
    maxCorrect = 0
    cptBestK = None


    for label in self.legalLabels:
        self.prior[label] += 1
    self.prior.normalize()

    featureCounts = util.Counter()
    for label in self.legalLabels:
        featureCounts[label] = util.Counter()

    for i in range(sampleSize):
        for feature in self.features:
            if trainingData[i][feature] is 1:
                featureCounts[trainingLabels[i]][feature] += 1

    for k in kgrid:
        cptKSmooth = []
        for label in self.legalLabels:
            cpt = util.Counter()
            for feature in self.features:
                cpt[feature] = (featureCounts[label][feature] + k) / float(k)
            cpt.normalize()
            cptKSmooth.append(cpt)
        
        self.cpt = cptKSmooth
        guesses = self.classify(validationData)
        correct = 0
        for i in range(len(guesses)):
            if guesses[i] is validationLabels[i]:
                correct += 1

        if correct > maxCorrect:
            maxCorrect = correct
            cptBestK = cptKSmooth

    self.cpt = cptBestK


        
def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    
    """
    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogJointProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
def calculateLogJointProbabilities(self, datum):
    """
    Returns the log-joint distribution over legal labels and the datum.
    Each log-probability should be stored in the log-joint counter, e.g.    
    logJoint[3] = <Estimate of log( P(Label = 3, datum) )>
    
    """
    logJoint = util.Counter()
    
    for label in self.legalLabels:
        sum = math.log(self.prior[label])
        for feature in self.features:
            if datum[feature] is not 0:
                sum = sum + math.log(self.cpt[label][feature])
        logJoint[label] = sum
    
    return logJoint