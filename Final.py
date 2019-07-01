import numpy as np

def razor(input_arg):
    def pow_vec(x,pow):
        ### pow_vec(x,pow) - creates an array of powers of x from x**0 to x**pow ###
        return np.array([x**n for n in range(0,pow+1)])

    def unitimes(va,vb,max_out):
        ### unitimes(va,vb,max_out) multiply the vectors va.reshape(1,-1) and vb.reshape(-1,1)
        #   and returns a vector of the unique indices that are lower than max_out
        ###
        retval = va.reshape(1,-1)*vb.reshape(-1,1)
        retval[retval>max_out] = 0
        retval= np.unique(retval)
        return retval

    vsize=1  # the size of power vector 

    out=np.array([1])
    # we'll try to find the n-th (max of "input_arg") indice. 
    # so we'll build the vector of "Razor numbers" 
    # untill its big enough to include this indice 

    while len(out) < max(input_arg):  
        vsize+=1
        # max_out is the largest number that we're sure we have all the razor numbers 
        # until that number it is the largest number that amalles number that can be achieved
        # from the power vector's multiplication, namely 2 ** (power vecto size)
        max_out = 2**vsize

        # initialize the power vectors
        v1= pow_vec(1,vsize)
        v2= pow_vec(2,vsize)
        v3= pow_vec(3,vsize)
        v5= pow_vec(5,vsize)
        v7= pow_vec(7,vsize)

        # delete all powers that are already larger than max_out
        for v in [v3,v5,v7]:
            v[v > max_out]=0
            
        out=v1

        for v in [v2,v3,v5,v7]:
            # use unitimes to get a vector of the unique numbers that are the product
            # of the two vectors and are smaller than max_out
            out = unitimes(out,v,max_out)
    # return the numbers correlating to the indices from input_arg        
    return(out.reshape(-1,1)[input_arg].tolist())
razor([1,2,3,4,11,12,13,21,22,23,100,1000,5842])
