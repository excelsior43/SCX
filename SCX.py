class SequentialConsecutiveCrossover:
    """ Implementation of Sequential Constructive crossover (SCX) """
    def __init__(self, costMatrix, p1, p2):
        self.costMatrix=costMatrix
        self.parentChromosome1=p1
        self.parentChromosome2=p2
        self.siz=len(self.costMatrix)
    def createSCX(self):
        p=0   # initializing to 0 instead of 1 # STEP 1
        self.childChromosome=[self.parentChromosome1[0]]
        while True:
            (nodeAlfa,nodeBeta)= (self.getNextLegitimateNode(self.parentChromosome1,p) , self.getNextLegitimateNode(self.parentChromosome2,p)) # STEP 3
            print "Logger Inspecting Nodes : (%d, %d )" % (nodeAlfa+1,nodeBeta+1)
            p=( nodeBeta,nodeAlfa) [self.costMatrix[p][nodeAlfa]<self.costMatrix[p][nodeBeta]] 
            self.childChromosome.append(p)
            print [x+1 for x in self.childChromosome]       # I am starting the index from 0 and not 1. so to avoid confusion i am adding 1 finally.
            if len(self.childChromosome)==self.siz: # STEP 4
                self.result= [x+1 for x in self.childChromosome]   # same description as above
                break
    def getNextLegitimateNode(self,ar,p): # STEP 2
        try:
            return filter(lambda x: x not in self.childChromosome , self.cutNotApplicableSectionOfList(ar,p))[0]
        except IndexError:
            pass
        return filter(lambda x: x not in self.childChromosome , range ( 1, self.siz-1))[0] # same case here instead of {2,3,4...n},I am calling {1,2,...}
    def cutNotApplicableSectionOfList(self,ar,p) :
        ind=ar.index(p)
        return (list(ar)[ind+1:], [])[ind==self.siz]
    def getResult(self):
        return self.result
