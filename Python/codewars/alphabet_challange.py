import string 

def alphabet_position(phrase) :

    my_list = list(phrase)  
    lower_alphabet_list  = list(string.ascii_lowercase)
    upper_alphabet_list  = list(string.ascii_uppercase)

    for x in my_list :
        for j in lower_alphabet_list :
            if x==j :
                yield lower_alphabet_list.index(x) 
        for k in upper_alphabet_list : 
            if x==k : 
                yield upper_alphabet_list.index(x)


for let in alphabet_position("The sunset sets at twelve o' clock.") :  
    print(let+1 , end=" ")  






 









