import numpy as np 
import scipy as sp
import scipy.special 
from matplotlib import pyplot as plt
import math

#psi takes in an nmax parameter and x parameter
#nmax is the number of hermite functions that you want to finish on
#x is an array of x values that you want to calculate the hermite functions for

x = [-2,-1,0,1,2]


#np.linspace(-2,2,51)
nmax = 7
m_max = 3
def f(x):
    return np.power(x,2)

def psi(nmax, x):
    func_array = []
    for i in range(0, nmax+1):
        polynomial = scipy.special.eval_hermite(i, x)
        function = (((2**i)*(math.factorial(i))*math.sqrt(math.pi))**(-1/2))*(math.exp((-i**2)/2))*polynomial
        func_array.append(function)
   # plt.plot(x, func_array[i])
    #plt.show()
    return func_array 

#psi(nmax,x)



def Hn(nmax, x):
    arr_of_arr = []
    for i in range(0, nmax+1):
        polynomial = scipy.special.eval_hermite(i, x)
        arr_of_arr.append(polynomial)
#    plt.plot(x, arr_of_arr[i])
#    plt.show()
    return arr_of_arr

#Hn(nmax,x)
        


def HT(x, f, m_max):
    dx = x[2] - x[1]
    fhn = np.zeros(m_max + 1)
    H = Hn(m_max,x)
    sum = 0
    for m in range(0, m_max+1):
        for n in range(0, len(H[m])):
            product = math.exp(-x[n]**2)*H[m][n]*f[n]*dx
            sum = sum + product
        fhn[m] = sum
    return fhn

#print(HT(x, f(x), m_max))



def iHt(x, fh, m_max):
    dx = x[2] - x[1]
    f = np.zeros(m_max+1)
    H = Hn(m_max,x)
    sum=np.zeros(len(H[1]))
    for m in range(0, m_max+1):
        product = (1/(((math.pi)**(.5))*(2**m)*math.factorial(m)))*fh[m]*H[m]
        sum = sum + product
    f = sum

    return f

#print(iHt(x, f(x), m_max))




#print(Hn(array, max))
#print(Hn(max,arr))   

#plt.figure()
#plt.plot(arr, Hn(max,arr))




#def HT(x, f, m_max, weight, normalisation)
#    dx = x[2] - x[1]
#    weightx = weight(x)
















    
    
    
