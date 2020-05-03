import numpy as np
from timeit import default_timer as timer
import random

def neuron_loop(input,weight,bias):
    output = bias
    for x,y in zip(input,weight):
        output = output + x*y
    return(output)

def neuron_numpy(input,weight,bias):
    output = np.dot(weight,input) + bias
    return(output)

if __name__ == '__main__':
    weights = [random.randint(0,10) for i in range(500)]
    inputs = [random.randint(0,10) for i in range(500)]
    bias = random.randint(0,10)
    
    start = timer()
    neuron_loop(weights,inputs,bias)
    end = timer()
    print("loop ", end - start)

    start = timer()
    neuron_numpy(weights,inputs,bias)
    end = timer()
    print("numpy ", end - start)