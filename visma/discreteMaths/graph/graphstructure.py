class CreateAdjency:
    '''
    An optimized version of adjacency List and adjacency Matrix
    They are the most common structures for graph
    instead of making use of linked list we have combined dictionary with list
    As it works of values of all types
    '''
    def __init__(self,count,edge,map):
        self.adjList=[]
        self.adjencyMatrix=[]
        for i in count:
            self.adjList.append([])
        for i in count:
            self.adjencyMatrix.append([])
            for j in count:
                self.adjencyMatrix[i].append('inf')
        for i in edge:
            temp=self.adjencyMatrix[map[i[0]]]
            temp[map[i[1]]]=1
        for i in edge:
            self.adjList[map(i[0])].append(map[i[1]])
        return self
    def getValue(self):
        return self.adjencyMatrix,self.adjList
