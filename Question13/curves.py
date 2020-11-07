"""

Q13.Write a program that makes use of a function to display sine , cosine ,
    polynomial and exponential curves .

"""


import matplotlib.pyplot as plt
import math


#Sine Function
def sineCurve():

    plt.subplot(2, 2, 1)
    degrees = range(0, 360 + 1)
    sinValues = [math.sin(math.radians(i)) for i in degrees]
    plt.plot(sinValues)
    plt.xlabel('Degrees')
    plt.ylabel('Sin Values')
    plt.title('Sine Curve')
    plt.grid()


#Cosine Curve
def cosineCurve():

    plt.subplot(2, 2, 3)
    degrees = range(0, 360 + 1)
    cosValues = [math.cos(math.radians(i)) for i in degrees]
    plt.plot(degrees, cosValues)
    plt.xlabel('Degrees')
    plt.ylabel('Cosine Values')
    plt.title('Cosine Curve')
    plt.grid()


#Polynomial Curve
def polynomialCurve():
    
    def polynomial(x):
        return (8*x*x)
    plt.subplot(2, 2, 2)
    x = range(-51, 50 + 2)
    y = [polynomial(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y = 8x^2')
    plt.title('Polynomial Curve')
    plt.grid()


#Exponential Curve
def expCurve():
    

    plt.subplot(2, 2, 4)
    x = []
    for i in range(0, 100*10):
        x.append((-5) + (0.01)*i)
    y = [math.exp(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y = e^x')
    plt.title('Exponetial Curve')
    plt.grid()


#Main Function
def main():
    plt.figure(figsize=(9, 5)) 
    sineCurve()
    cosineCurve()
    polynomialCurve()
    expCurve()
    plt.tight_layout()
    plt.savefig('plot.png', dpi=275, bbox_inches='tight') 
    plt.show()
    

if __name__ == "__main__":
    main()
