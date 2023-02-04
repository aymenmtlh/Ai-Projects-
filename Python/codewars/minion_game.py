## the minion game 


def minion_game () :


        word = input('enter a word in capital letters please')
        
        my_list = list(word)
        lis =[]

        constants =['B', 'C', 'D', 'F','G', 'J', 'K', 'L', 'M', 'N','P' , 'Q', 'S', 'T', 'V', 'X', 'Z' , 'H', 'R','W' , 'Y']

        ###### KEVIN TURN 
        print ('the word is :' , word)  
        input1 = input('enter your first word starts with constanst')
        input1_list= list(input1)
        for i  in input1_list :
           for j in my_list :
            if i == j :
                 lis.append(i)
                 print(lis)
          

                #repeat = my_list.count(input1_list) 
                #print(repeat)
                


        



minion_game()



        

       