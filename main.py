"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    z = _quadratic_multiply(x,y)
    return z.decimal_val

def _quadratic_multiply(x, y):
    ### TODO
    x = x.binary_vec
    y = y.binary_vec
    s = pad(x, y)
    x = s[0]
    y = s[1]
    if ((binary2int(x).decimal_val <= 1) and (binary2int(y).decimal_val <= 1)):
        return BinaryNumber(binary2int(x).decimal_val * binary2int(y).decimal_val)
    else:
        xsplit = split_number(x)
        ysplit = split_number(y)
        xleft = xsplit[0]
        xright = xsplit[1]
        yleft = ysplit[0]
        yright = ysplit[1]
        val1 = bit_shift((_quadratic_multiply(xleft,yleft)), (len(x)))
        val2 = bit_shift(_quadratic_multiply(xleft, yright), len(x) // 2)
        val3 = bit_shift(_quadratic_multiply(xright, yleft), len(x) // 2)
        val4 = bit_shift(_quadratic_multiply(xright, yright),0)

        return BinaryNumber(val1.decimal_val + val2.decimal_val + val3.decimal_val + val4.decimal_val)
    ###


     
    
def test_quadratic_multiply():
    start = time.time()

    _quadratic_multiply(BinaryNumber(2), BinaryNumber(2))
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

