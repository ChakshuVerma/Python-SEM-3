"""

Q9 .Use dictionary to store marks of the students in 4 subjects . Write a function to
    find the name of the student securing highest percentage . ( Hint : Names of
    students are unique ) .
    
"""



#Function To Find The Maximum Percentage

def maximum_percentage(data,Max):
    print("")
    for i in data:
        print(i," : ",data[i]*100)
        if(data[i]>data[Max]):
            Max=i
    return Max



#Main Function Definition

def main():
    data=dict()
    students=int(input("ENTER THE NUMBER OF STUDENTS : "))
    for i in range (0,students,1):
            print("\n\t\tSTUDENT ",i+1)
            name=input("ENTER NAME : ")
            m1=int(input("ENTER THE MARKS IN SUBJECT 1 (OUT OF 100) : "))
            assert m1>=0 and m1<=100 , "INVALID MARKS"
            m2=int(input("ENTER THE MARKS IN SUBJECT 2 : "))
            assert m2>=0 and m2<=100 , "INVALID MARKS"
            m3=int(input("ENTER THE MARKS IN SUBJECT 3 : "))
            assert m3>=0 and m3<=100 , "INVALID MARKS"
            m4=int(input("ENTER THE MARKS IN SUBJECT 4 : "))
            assert m4>=0 and m4<=100 , "INVALID MARKS"
            percentage=(m1+m2+m3+m4)/400
            data[name]=percentage
    Max=name                                                #Saving The Index Of Last Element For A Initial Value
    y=maximum_percentage(data,Max)                          #Calling maximum_percentage Function
    print("\n",y," HAS MAXIMUM PERCENTAGE : ",data[y]*100,"%")



#Calling Main Function
if __name__=="__main__":
    main()
