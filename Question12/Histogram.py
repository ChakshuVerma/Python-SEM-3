"""

Q12.Write a program that makes use of a function to accept a list of 'n' integers
    and displays a histogram .

"""

import matplotlib.pyplot as plt

def histogram(x,n):
    plt.hist(x,bins="auto",ec='red')
    plt.xlabel("\nValue")
    plt.ylabel("\nFrequency")
    plt.title("Histogram")
    plt.xlim(min(x)-1,max(x)+1)
    plt.show()
    return



def main():
    l=[]
    n=int(input("Enter Number Of Data Values : "))
    print("\n")
    for i in range(0,n,1):
        element=int(input("Enter Element : "))
        l.append(element)
    histogram(l,n)


if __name__=="__main__":
    main()
