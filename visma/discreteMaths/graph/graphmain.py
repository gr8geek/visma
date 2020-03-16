#from visma.discreteMaths.graphinput import dataParser
#from graphstructure import CreateAdjency
#from visma.discreteMaths.displaynetwork import displayNetworks
#from graphinput import dataParser
#from displaynetwork import displayNetworks

from visma.discreteMaths.graph.graphinput import *
from visma.discreteMaths.graph.displaynetwork import *
def acceptGraph(graph,name,graphType):
    container=[]
    g=dataParser(graph.keys(),name,graphType)
    container.append(g)
    #container.append(CreateAdjency(container[0].getData()))
    graph[name]=container

def displayGraph(graph,name):
    if name in graph.keys():
        print("Displaying ....")
        temp=graph[name]
        _,edges,_=temp[0].getData()
        displayNetworks(edges)



