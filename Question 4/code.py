"""
Q4 .Write a function that takes a number (>=10) as an input and return the digits of
    the number as a set .
"""

def main():
     digits=set()        #Set To Print The Digits 
     temp=0              #Temp variable
     count=0             #Count variable
     digits_l=[]

     num=int(input("Enter The Number : "))
     temp=num
             
     #Storing the digits of num in list
     while(num):
          count+=1
          temp=int(num%10)
          num=int(num/10)
          digits.add(temp)
          digits_l.append(temp)

     for i in range(0,count//2,1):
          #reversing list
          digits_l[i],digits_l[count-i-1]=digits_l[count-i-1], digits_l[i]
     print("\nTotal Digits : ",count)
     print("All Digits : ",digits_l)        
     print("Distinct Digits : ",digits)

if __name__=="__main__":
     main()
         
