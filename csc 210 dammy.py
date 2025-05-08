# using homer's scheme we get

def horner(p,x):
    res = 0
    for coeff in p:
        res = res * x + coeff
    return res

p = [1,1,0,0,0,0,6,1] # coefficients of p(x)
x = 8
result = horner(p,x)
print("the result for the polynomial is ", result)
