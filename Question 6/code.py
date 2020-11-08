
"""
Q6.Consider a tuplet1 ={1,2,5,7,9,2,4,6,8,10}.
   Write a program to perform following operations :
a) Print another tuple whose values are even numbers in the given tuple .
b) Concatenate a tuplet2 = {11,13,15) with t1 .
c) Return maximum and minimum value from this tuple .
"""

ch=0
# Given
len=10
t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)



#Function to print a temp tuple with even values from t1

def even():
    temp=()
    print("Even Values : ")
    for i in range(0,len,1):
        if(t1[i]%2==0):
            temp=temp + (t1[i],)
    print(temp)
    return



#Function to print maximum and minimum values from t1

def max_min():
    Max=t1[0]
    Min=t1[0]
    for i in range (1,len,1):
        if(t1[i]>Max):
            Max=t1[i]   
    print("Max Element Is : ",Max)
    for i in range (1,len,1):
        if(t1[i]<Min):
            Min=t1[i]
    print("Min Element Is : ",Min)
    return



#Main function

def main():
    print("Press")
    print("1.Print A Tuple Having Even Values From ",t1)
    print("2.Concatenate ",t2," with ",t1)
    print("3.Print Maximum And Minimum Values From ",t1)
    ch=int(input())

    if(ch==1):
        even()  


    elif(ch==2):
        temp=t1+t2          #concatenating t1 and t2
        print(temp)

    elif(ch==3):
        max_min()


if __name__=="__main__":
    main()
