"""
Q1.Write a function that takes the lengths of three sides : side1 , side2 and side3 of
the triangle as the input from the user using input function and return the area
and perimeter of the triangle as a tuple . Also , assert that sum of the length of any
two sides is greater than the third side .
"""


# function to calculate perimeter of the triangle

def perimeter(x1,x2,x3):
    p=x1+x2+x3
    print("Perimeter of Triangle : ",p)
    area(p,x1,x2,x3)



# function to calculate area of the triangle

def area(p,x1,x2,x3):
    p=p/2
    a=float((p*(p-x1)*(p-x2)*(p-x3))**0.5)
    print("Area of Triangle : ",a)
    return 



#Main function

def main():
    x1=int(input("Enter The Length Of Side 1 : "))
    x2=int(input("Enter The Length Of Side 2 : "))
    x3=int(input("Enter The Length Of Side 3 : "))

    if(x1+x2>x3 and x2+x3>x1 and x3+x1>x2):
       perimeter(x1,x2,x3)

    else:
        print("\nTriangle With Given Sides Is Not Possible")



if __name__=="__main__":
    main()
