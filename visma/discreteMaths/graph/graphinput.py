# This class holds essential graph structures like adjency list representation
#represents directed and undirected graphs
# adjency matrix representation
# vretices list-(A list containing set vertices)
class dataParser:
#concerned with parsing the input data and organizing it.List of edges and mapping between the name of egges and a numerical value for effecient computation

    def __init__(self,names,graphName,graphType,args=0):
        if graphName not in names:
            self.graphName=graphName
            if args == 0:
                #operations from the CLI
                if graphType == 0:
                    self.graphType = "Directed"
                else:
                    self.graphType =" Un-Directed"
                self.map={}
                print("Enter the egdes seperated by ;")
                #Vertices are allocated in map
                inp=input()
                inp=inp.split(';')
                self.edges=[]
                self.conut=0
                for i in inp:
                    temp=i.split(',')
                    self.edges.append([temp[0],temp[1]])
                    if temp[0] not in self.map.keys():
                        self.map[temp[0]]=self.conut
                        self.count=self.conut+1
                    if temp[1] not in self.map.keys():
                        self.map[temp[1]]=self.count
                        self.count=self.count+1
                return None
        else:
            print("Graph already exists")
    def getData(self):
        return self.count,self.edges,self.map











