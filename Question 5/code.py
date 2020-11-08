"""
Q5 .Write a function that finds the sum of the n terms of the following series .
    Import the factorial function created in question 4 .
    1 – x2/2! + x4/4! – x6/6! + ... xn/n!
"""

#importing factorial from another file
from factorial import factorial





#Function to find sum of series

def sumofseries(n,x):
    sum=1        
    for i in range(1,n,1):
        if(i%2!=0):
            sum-=float(pow(x,2*i)/factorial(2*i))
        else :
            sum+=float(pow(x,2*i)/factorial(2*i))
    return sum
            



#Main function    

def main() :
    n=int(input("Enter The Number Of Terms : "))
    if(n<=0):
        print("Invalid Input\nExiting Program...")
        exit()
    x=int(input("\nEnter Value of x : "))   
    print("\nSum Of Series Upto ",n," Terms = ",sumofseries(n,x))
    

if __name__=="__main__":
    main()
