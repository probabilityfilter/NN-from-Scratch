def neuron(input,weight,bias):
    output = bias
    for x,y in zip(input,weight):
        output = output + x*y
    return(output)

if __name__ == '__main__':
    print(neuron([10,2,1],[3,40,1],100))