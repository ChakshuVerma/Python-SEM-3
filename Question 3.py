"""

Q3. Write a Python function to find the nth term of Fibonacci sequence and it's
    factorial . Return the result as a list .
    
"""

n=0         
x=0         #a temp variable
series=[]   #list to store fibonacci series


#function to find factorial of a number

def factorial(n):
    temp=n
    for i in range (n-1,1,-1):
        temp*=i
    return temp



#function to print the fibonacci series

def fibonacci(n):
    curr=1
    last=0
    x=curr
    series.append(0)
    series.append(1)
    for i in range (2,n,1):
        x=curr+last
        series.append(x)
        last=curr
        curr=x
    return series
    
    

#main function

def main():
    n=int(input("\nEnter The Number Of Terms Upto Which You Want To See The Fibonacci Series : "))    
    print("\nThe Fibonacci Series having Upto ",n," Terms Is : ",fibonacci(n))
    print("\nThe Factorial of ",n," is : ",factorial(n)," \n")   

if __name__ == "__main__":
    main()
