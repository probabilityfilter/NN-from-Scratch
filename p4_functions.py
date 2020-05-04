import numpy as np
np.random.seed(0)

def layer(wts, inpt, bias):
    if np.array(wts).shape[0] == np.array(bias).shape[0] and np.array(wts).shape[1] == np.array(inpt).shape[0]:
        otpt = np.dot(wts,inpt) + bias
        return(otpt)
    return("Dimension mismatch in arrays")

if __name__ == '__main__':
    img =  [1,2,3,4]
    wt =  [[1,2,3,4],[5,6,7,8]]
    b =  [100,200]
    print(type(layer(wt,img,b)), layer(wt,img,b))

    img2 =  [[1,2,3,4], [10,20,30,40]]
    wt2 =  [[1,2,3,4],[5,6,7,8]]
    b2 =  [100,200]
    print(type(layer(wt2,img2,b2)), layer(wt2,img2,b2))