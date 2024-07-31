import numpy as np
import math


def npmap(fn,array : np.ndarray):
    res = np.ravel(array).tolist()
    for i in range(len(res)):
        res[i] = fn(res[i])
    res = np.array(res).reshape(array.shape)
    return res



class NeuralNetwork:
    def __init__(self,input_nodes,hidden_nodes,output_nodes):
        self.input_nodes = input_nodes 
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        
        a = -1
        b = 1
        
        self.weights_ih = np.random.uniform(a,b,(self.hidden_nodes,self.input_nodes)) 
        self.weights_ho = np.random.uniform(a,b,(self.hidden_nodes,self.output_nodes))  
        
        self.bias_h = np.random.uniform(a,b,(self.hidden_nodes))
        self.bias_o = np.random.uniform(a,b,(self.output_nodes))
        
    def sigmoid(self,x):
       return 1 / (1 + math.exp(-x))
   
   
    
    def train(inputs,answer):
        pass
    
    def feedforward(self,inp):
        inputs = np.matrix(inp)
        hidden = np.matmul(inputs,self.weights_ih)
        hidden += self.bias_h
        hidden = npmap(self.sigmoid,hidden)
   

       
        output = np.matmul(hidden,self.weights_ho)
        output += self.bias_o
        output = npmap(self.sigmoid,output)
       
        output = np.ravel(output)
        return output
      
    
nn = NeuralNetwork(2,2,1)
inp = [1,0]
output = nn.feedforward(inp)
print(output)
print(npmap(lambda x: x*2,np.array([[1],[2],[3],[4]])))



