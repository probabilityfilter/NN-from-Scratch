import numpy as np

def layer(wts, inpt, bias):
    if wts.shape[0] == bias.shape[0] and wts.shape[1] == inpt.shape[0]:
        otpt = wts.dot(inpt) + bias
        return(otpt)
    return("Dimension mismatch in arrays")

if __name__ == '__main__':
    img =  np.array([1,2,3,4])
    wt =  np.array([[1,2,3,4],[5,6,7,8]])
    b =  np.array([100,200])
    print(type(layer(wt,img,b)), layer(wt,img,b))