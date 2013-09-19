class SCX:
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
                return [x+1 for x in self.childChromosome]   # same description as above
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
#END OF CLASS. test data is below 

costMatrix = [
    [999,75, 99, 9, 35, 63, 8],
    [51, 999, 86, 46, 88, 29, 20],
    [100, 5, 999, 16, 28, 35, 28],
    [20, 45, 11, 999, 59, 53, 49],
    [86, 63, 33, 65, 999, 76, 72],
    [36, 53, 89, 31, 21, 999, 52],
    [58, 31, 43, 67, 52, 60, 999]
]
P1=(0, 4, 6, 2, 5, 3, 1)
P2=(0, 5, 1, 3, 2, 4, 6)
a = SCX(costMatrix, P1,P2)
print a.createSCX()  
