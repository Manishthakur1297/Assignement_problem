import time
import random

#class Solution:
#    def __init__(self):
#        self.binary = self.BinaryTree()
#        self.data = self.
        
global nodeNum
global incInteger
global count

class BinaryTree:
    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.genisis = None


    def insert(self,c,newNode):
        if c%2==0:
            return self.insertLeft(self,newNode)
        else:
            return self.insertRight(self,newNode)
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        
            
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
                
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    
class Data:
    def __init__(self,data):
        arr = data.split(' ')
        self.id = arr[0]
        self.value = arr[1]
        self.name = arr[2]
            
    def getName(self):
        return self.name
        
    def getValue(self):
        return self.value
        
    def getId(self):
        return self.id
        
    def hashValue(self):
        return hash(tuple(self.id,self.value,self.name))
            
    
class Node:
    
        def __init__(self,data,referenceId,childId,genesisId):
            self.timestamp = time.time()
            self.data = Data(data)
            self.nodeNumber = self.IncInteger(incInteger)
            self.nodeId = self.generateId(nodeNum)
            self.referenceId = referenceId
            self.childId = childId
            self.genesisId = genesisId
            self.hashValue = hash((self.timestamp,self.data,self.nodeNumber,self.nodeId,self.referenceId,self.childId,self.genesisId))
            
        def IncInteger(self,incInteger):
                incInteger+=1
                return incInteger
            
        def generateId(self,nodeN):
                chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                while True:
                    value = "".join(random.choice(chars) for _ in range(32))
                    if value not in nodeN:
                        nodeN.add(value)
                        break

if __name__ == "__main__":
    nodeNum = set()
    incInteger = 0
    count = 0
    b = BinaryTree(100)
    while(count<10):
        count+=1
        name = input('Enter Name of Node : ')
        id = input('Enter Owner Id of Node : ')
        value = input('Enter Value of Node : ')
        data = str(name+' '+id+' '+value)
        referenceId = b.parent
        childreference = b.getLeftChild()
        genesis = b.genisis
        node = Node(data,referenceId,childreference,genesis)