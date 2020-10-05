"""
Q2. Consider a showroom of electronic products,where there are various
    salesmen . Each salesman is given a commission of 5% , depending on the sales
    made per month . In case the sale done is less than 50000 , then the salesman is
    not give nany commission . Write a function to calculate total sales of a salesman
    in a month , commission and remarks for the salesman . Sales done by each
    salesman per week is to be provided as input . Use tuples / list to store data of
    salesmen .

    Assign remarks according to the following criteria :
    Excellent : Sales >= 80000
    Good : Sales >= 60000 and < 80000
    Average : Sales >= 40000 and < 60000
    Work Hard : Sales < 40000
"""






#function to print monthy sales of each salesman

def monthlysales(s,i):
    print("\nSales Done In One Month By Salesman ",i+1," are : ",s*4)
    commission(s,i)




#function to print commission of each salesman
    
def commission(s,i):
    if(s>=50000):
        print("Commission of Salesman ",i+1," is : " ,s*0.05)
    else :
        print("Commission of Salesman ",i+1," is : 0")
    remarks(s,i)




#function to print remarks of each salesman
    
def remarks(s,i):
    if(s>=80000):
        print("Remark Of Salesman ",i+1," is -- Excellent")
    elif(s>=60000):
        print("Remark Of Salesman ",i+1," is -- Good Sales")
    elif(s>=40000):
        print("Remark Of Salesman ",i+1," is -- Average")
    else:
        print("Remark Of Salesman ",i+1," is -- Work Hard")
    return




#Main function

def main():
    Sales=[]    #list to store weekly sales of salesmen
    n=int(input("Enter The Number Of Salesmen : "))
     
    for i in range(0,n,1):
        s=0
        print("\nEnter The Sales For Salesman ",i+1," for four weeks")
        for j in range (1,5,1):
             ele=int(input("Enter The Sales : "))        #Assuming the sales per week are constant for all weeks
             s=s+ele 
        Sales.append(s)
        monthlysales(s,i)        
            
            
if __name__=="__main__":
    main()
