''' Insert heading comments here.'''
" PROJECT 03"

import string

alpha = string.ascii_lowercase

letter="abcdefghijklmnopqrstuvwxyz"           #build an alphabet

answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
while answer.upper() != 'Q':
    if answer.upper()=='E':       #if the input is encrypt, do encrypt process
        a=5
        b=8
        key_empt = ''
        key_word = input("Please enter a keyword: ")      # input your keyword
        while not key_word.isalpha() :                # Check the keyword is alpha or not. if not print invalid string
            print("There is an error in the keyword. It must be all letters and a maximum length of 26") 
            key_word = input("Please enter a keyword: ")
            break
        while key_word.isalpha() and len(key_word) >26:  ##check the keyboard is aplha but the length of it is bigger than 26
            print("There is an error in the keyword. It must be all letters and a maximum length of 26") 
            key_word = input("Please enter a keyword: ")
            break
        key_word=key_word.lower()       # change the keyword's string into lowercase
        affine_num=''                                      # build a new empty string, use for the new alphabt
        num=''
    
        for ch in key_word:
        
            if ch not in key_empt:     #check the repeat letters
                key_empt += ch              
        
        for ch in letter:
            if ch not in key_empt:     #check the repeat letters
                key_empt += ch  
        
        for i in range(26 ):
            affine_num += key_empt[(a*i+b)%26] 
        message=input("Enter your message: ")
        message=message.lower()
        for i in message:                #input message, and encrypt it 
           if i.isalpha():                
               if i in letter:
                   v = letter.find(i)         #find the input string's position in letter
                   num_encrypt=key_empt[(a*v+b)%26]    #transfer it into key_empt
                   num+=num_encrypt          # add the new encrypt into the empty string
           else:
               num += i
        print("your encoded message: ",num)
                  
    elif answer.upper()=='D':                  # if the player want to decrypt the code
        a=5
        b=8
        key_empt = ''
        key_word = input("Please enter a keyword: ")       # input the keyword
        while not key_word.isalpha():              # Check the keyword is alpha or not. if not print invalid string
            print("There is an error in the keyword. It must be all letters and a maximum length of 26") 
            key_word = input("Please enter a keyword: ")
            break
        while key_word.isalpha() and len(key_word) >26:      #check the keyboard is aplha but the length of it is bigger than 26
            print("There is an error in the keyword. It must be all letters and a maximum length of 26") 
            key_word = input("Please enter a keyword: ")
            break
        key_word=key_word.lower()      ## change the keyword's string into lowercase
        affine_num=''
        num_2=''
        if key_word.isalpha():
            for ch in key_word:
                
                if ch not in key_empt:     #check the repeat letters
                    key_empt += ch
    
            for ch in letter:
                if ch not in key_empt:     #check the repeat letters
                    key_empt += ch  
            
            for i in range(26 ):
                affine_num += key_empt[(a*i+b)%26]    
            message=input("Enter your message: ")
            message=message.lower()
            for i in message:                        #input message, and decrypt it 
                if i.isalpha(): 
                    x = affine_num.index(i)          #use the formualr in the verse way to find the position of the letter
                    num_2 += alpha[x]
                else:
                    num_2 += i
                
                   
                       
            print("your decoded message: ",num_2)        
            
    else:                                 # check the input keword is not michigan, print invaild string
        print("There is an error in the keyword. It must be all letters and a maximum length of 26")
    answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
print("See you again soon!")
