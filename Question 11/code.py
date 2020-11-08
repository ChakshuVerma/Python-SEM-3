"""

Q11.Write a menu-driven program to accept a list of student names and perform
    the following :
    a.search an element using linear search / binary search .
    b.Sort the elements using bubble sort / insertion sort / selection sort .

"""



#Function To Perform Linear Search

def linear_search(names_list,x):
    for i in names_list:
        if i==x:
            print(x," FOUND")
            return
    print(x," NOT FOUND")
    return


#Function To Perform Binary Search

def binary_search(names_list,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if names_list[mid]==x:
            return mid
        elif names_list[mid] > x: 
            return binary_search(names_list, low, mid - 1, x) 
        else: 
            return binary_search(names_list, mid + 1, high, x) 
    else: 
        return -1
    
    
def insertion_sort(names_list,n):
    for i in range (1,n,1):
        j=i-1
        temp=names_list[i]
        while(j>=0 and names_list[j]>temp):
            names_list[j+1]=names_list[j]
            j-=1
        names_list[j+1]=temp
    print("\nTHE SORTED ARRAY IS : ",names_list)
    return


def selection_sort(names_list,n):
     for i in range(0,n,1): 
        min_idx = i 
        for j in range(i+1,n,1): 
            if (names_list[min_idx] > names_list[j]): 
                min_idx = j
        names_list[i], names_list[min_idx] = names_list[min_idx], names_list[i]
     print("\nTHE SORTED ARRAY IS : ",names_list)
     return



def bubble_sort(names_list,n):
    for i in range (1,n,1):
         j=i
         while(j>=0 and names_list[j]>names_list[j-1]):
             names_list[j],names_list[j-1]=names_list[j-1],names_list[j]
             j-=1
    print("\nTHE SORTED ARRAY IS : ",names_list)
    return
             


def main():
    names_list=[]
    n=int(input("ENTER TOTAL STUDENTS : "))
    for i in range (0,n,1):
        name=input("ENTER NAME OF STUDENT : ")
        names_list.append(name)
    choice='1'
    while(choice!=0):
        print("\n\t\t\tMENU ")
        print("(1)SEARCH AN ELEMENT")
        print("(2)SORT THE NAMES")
        print("(0)EXIT\n")
        choice=input("YOU SELECTED : ")
        assert choice=='1' or choice=='2' or choice =='0',"WRONG CHOICE !"

        if(choice=='0'):
            exit()
            
        elif(choice=='1'):
            print("\n1.LINEAR SEARCH")
            print("2.BINARY SEARCH")
            ch=input("YOU CHOSE : ")
            assert ch=='1' or ch=='2',"WRONG CHOICE !"
            if(ch=='1'):
                x=input("ENTER NAME TO BE SEARCHED : ")
                linear_search(names_list,x)
                
            else :
                x=input("ENTER NAME TO BE SEARCHED : ")
                res=binary_search(names_list,0,n-1,x)
                if res!=-1:
                    print(x," FOUND AT POSITION ",res+1)
                else:
                    print(x," NOT FOUND")
        
        else:
            print("\n1.SELECTION SORT")
            print("2.INSERTION SORT")
            print("3.BUBBLE SORT")
            ch=input("YOU CHOSE : ")
            assert ch=='1' or ch=='2' or ch=='3',"WRONG CHOICE !"

            if(ch==1):
                selection_sort(names_list,n)

            elif(ch==2):
                insertion_sort(names_list,n)

            else :
                bubble_sort(names_list,n)



if __name__=="__main__":
    main()
