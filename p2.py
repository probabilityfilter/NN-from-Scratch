def neuron(i,w,b):
    o = 0
    for x,y in zip(i,w):
        o = o + x*y
        print(o)
    o = o + b
    return(o)

if __name__ == '__main__':
    print(neuron([1,2],[3,4],5))