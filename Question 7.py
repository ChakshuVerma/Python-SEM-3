"""
Q7.Write a menu driven program to perform the following on strings :
a) Find the length of string .
b) Return maximum of three strings .
c )Accept a string and replace all vowels with “#” .
d) Find number of words in the given string .
e) Check whether the string is a palindrome or not .
"""


#function to return maximum of 3 strings

def maxstring():
    s1=input("\nEnter String 1 : ")
    s2=input("Enter String 2 : ")
    s3=input("Enter String 3 : ")
    if(s1>=s2 and s1>=s3):
        s1=s1
    elif(s2>=s1 and s2>=s3):
        s1=s2
    else:
        s1=s3
    return s1



#Function to modify string

def modstring():
    s=input("\nEnter The String : ")
    s1=""
    Length=len(s)
    for i in range(0,Length,1):
        if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
            s1+=('#')
        else:
            s1+=s[i]
    print("Modified String Is : ",s1)
    return        



#Function to count number of words in a string

def countwords():
    s=input("\nEnter The String : ")
    length=len(s)
    count=1
    for i in range(0,length-1,1) :
        if(s[i]==' ' and s[i+1]!=' '):
            count+=1;
    print("No. Of Words In ",s," is : ",count)
    return




#Function to check whethera string is palindrome or not

def palindrome():
    i=0
    s1=""           #Temporary string to store reverse of original string
    s=input("Enter The String : ")
    length=len(s)
    for i in range (length-1,-1,-1):
        s1+=s[i]
    if(s==s1):
        print("The String {",s,"} Is A Palindrome")
    else:
        print("The String {",s,"} Is Not A Palindrome")
    return




    
#Main function

def main():
    ch='y'          #Variale for taking choice to continue or not
    while ch=='y' or ch=='Y' :
        print("\n\nPRESS")
        print("1.LENGTH OF STRING")
        print("2.RETURN MAXIMUM OF 3 STRINGS")
        print("3.REPLACE VOWELS BY '#'")
        print("4.PRINT NUMBER OF WORDS IN STRING")
        print("5.CHECK FOR PALINDROME")
        print("0.EXIT THE PROGRAM")
        opt=int(input("\nYOUR CHOICE : "))

        if(opt==0):
            print("\n============================EXITING THE PROGRAM================================")
            exit()
            
        elif(opt==1):
            s=input("\nEnter The String : ")
            length=len(s)
            print("The Length Of String ",s," is : ",length)

        elif(opt==2):
            print("\nMaximum String Among These 3 Is : ",maxstring())
            
        elif(opt==3):
            modstring()
            
        elif(opt==4):
            countwords()
            
        elif(opt==5):
            palindrome()
            
        else:
             print("\nInvalid Option Selected!!")
             
        ch=input("\nDo You Want To Do Any Operation ? ( y=yes ) : ")


if __name__=="__main__":
    main()
