"""

Q10 .Write a function that takes a sentence as input from the user and calculates
     the frequency of each letter . Use a variable of dictionary type to maintain the
     count .

"""



#FUNCTION TO COUNT THE NUMBER OF TIMES EACH WORD OCCURS

def count_words(sentence):
    d=dict()
    string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"   #Saving all uppercase and lowercase alphabets in a string
    for i in string:
        d[i]=0
        
    for i in sentence:
        d[i]=d[i]+1
        
    for i in d:
        if(d[i]>0):
            print("'",i,"' OCCURS ",d[i]," TIMES")



#MAIN FUNCTION

def main():
    sentence=input("ENTER A SENTENCE WITHOUT NUMBERS : ")
    count_words(sentence)
    
    



#CALLNG MAIN FUNCTION
    
if __name__=="__main__":
    main()
