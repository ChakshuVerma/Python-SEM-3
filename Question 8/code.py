"""
Q8 .Write a Python program to perform the following using list :
a)  Check if all elements in list are numbers or not .
b)  If it is a numeric list ,then count number of odd values in it .
c)  If list contains all Strings , then display largest String in the list .
d)  Display list in reverse form .
e)  Find a specified element in list .
f)  Remove the specified element from the list .
g)  Sort the list in descending order .
h)  accept 2 lists and find the common members in them .
"""



#Function to check whether the list contains all numbers

def checknum(l,r):
    flag=-1
    for i in l:
        if(not(i.isnumeric())):
            flag=0
            break

    if(flag==-1):
         temp=[]
         print("\nALL ELEMENTS ARE NUMBERS")
         print("ODD VALUES : ")
         count=0
         for i in l:
             num=int(i)
             if(num%2!=0):
                 count=count+1
                 print(i,",")
         print("TOTAL ODD VALUES : ",count)        
    else:
         print("\nELEMENTS HAVE OTHER CHARACTERS TOO")
    return




#Function to check whether the list contains all strings

def checkstring(l,r):
    flag=-1
    for i in l:
        if(i.isnumeric()):
            flag=0
            break

    if(flag==-1):
        print("\nALL ELEMENTS ARE STRINGS ")
        print("LARGEST STRING IS: ",max(l))
    else:
        print("\nALL ELEMENTS ARE NOT STRINGS")
    return




#Function to display reverse of a list

def reverselist(l,r):
    temp=[]
    for i in range(r-1,-1,-1):
        temp.append(l[i])
    print("\nLIST IN REVERSED ORDER IS : ",temp)    
    return          




#Function to search an element in a list

def searchele(l,r):
    flag=0
    ele=input("\nENTER ELEMENT TO BE SEARCHED ")
    for i in range(0,r,1):
        if(l[i]==ele):
            print("ELEMENT ",ele," FOUND AT POSITION ",i+1)
            flag=-1
            break
    if(flag==0):
        print("\nELEMENT ",ele," WAS NOT FOUND ")
    return    




#Function to remove an element from a list

def removeele(l,r):
    flag=0
    ele=input("\nENTER ELEMENT TO BE REMOVED : ")
    for i in range(0,r,1):
        if(l[i]==ele):
            flag=-1
            r-=1
            print("MODIFIED RANGE : ",r)
            for j in range (i,r,1):
                l[j]=l[j+1]
            l=l[:-1]    
            break    
    if(flag==-1):
        print("ELEMENT REMOVED")
        print("NOW THE LIST IS : ",l)
    else :    
        print("ELEMENT ",ele," WAS NOT FOUND ")
    return




#Function to sort a list in descendind order

def sortlist(l,r):
    for i in range (0,r,1):
        for j in range(0,r-i-1,1):
            if(l[j]<l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
        
    print("\nSORTED LIST : ",l)
    return
    

#Function to print the common elements in 2 lists.

def commonele():
    a=[]
    b=[]
    r1=int(input("\nENTER NUMBER OF ELEMENTS IN LIST 1: "))
    print("")
    for i in range(0,r1,1):
        ele=input("ENTER THE ELEMENT : ")
        a.append(ele)
    r2=int(input("\nENTER NUMBER OF ELEMENTS IN LIST 2: "))
    for i in range(0,r2,1):
        ele=input("ENTER THE ELEMENT : ")
        b.append(ele)
    temp=[]
    for i in range (0,r1,1):
        for j in range (0,r2,1):
            if(a[i]==b[j]):
                temp.append(a[i])
    print("\nCOMMON ELEMENTS : ",temp)            
    return        


#Main Function

def main():
    ch='y'
    r=0
    l=[]
    print("\t\t\t-----------MENU DRIVEN PROGRAM--------------")
    r=int(input("ENTER NUMBER OF ELEMENTS IN LIST : "))
    print("\n")
    for i in range(0,r,1):
        ele=input("ENTER THE ELEMENT : ")
        l.append(ele)    
    while ch=='y' or ch=='Y':
        print("\n\t\t\tMENU")
        print("\n1. CHECK IF ALL ELEMENTS IN LIST ARE NUMBERS AND COUNT ODD VALUES ")
        print("2. CHECK IF ALL ELEMENTS IN LIST ARE STRINGS AND DISPLAY LARGEST STRING")
        print("3. DISPLAY A LIST IN REVERSE FORM ")
        print("4. FIND SPECIFIC ELEMENT IN A LIST ")
        print("5. REMOVE SPECIFIC ELEMENT FROM A LIST ")
        print("6. SORT A LIST IN DESCENDING ORDER ")
        print("7. FIND COMMON MEMBERS IN 2 LISTS ")
        print("0. EXIT THE PROGRAM ")
        opt=int(input("\nSELECT AN OPTION : "))
        if (opt==1):
            checknum(l,r)
            
        elif (opt==2):
            checkstring(l,r)
            
        elif (opt==3):
            reverselist(l,r)
            
        elif (opt==4):
            searchele(l,r)
            
        elif (opt==5):
            removeele(l,r)
            l=l[:-1]
            print("Range : ",r)
            
        elif (opt==6):
            sortlist(l,r)
            
        elif(opt==7):
            commonele()
                
        elif (opt==0) :
            print("=============EXITING THE PROGRAM====================")
            exit()
            
        else:
            print("\nINVALID OPTION SELECTED!!!")

        ch=input("\nCONTINUE?(y=yes) : ")
    
        
if __name__=="__main__":
    main()
    
