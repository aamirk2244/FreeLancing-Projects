def Odd():
    print("************************************")
    print("ST2414 PSEC Practical 2 Submission 2")
    print("************************************")
    ist = input('Pls enter a starting number: ')
    last = input('Pls enter an ending number: ')
    if ist.isnumeric() and last.isnumeric():
        ist = int(ist)       # converting to integer
        last = int(last)      # 
        savedSequence = ''            # will save the sequence of output here 
            
        if ist < last :              # i.e ist = 22 ,and last = 33
            for val in range(ist,last):      # starting from ist upto last (excluding last)
                if val%2 != 0 : savedSequence = savedSequence + str(val) + '\t'       # val is integer therefore converting back to string in order to append to savedSequence
        if ist > last:            # it means we will print in reverse order i.e ist = 33 and last = 22
            for val in  reversed(range(last+1,ist+1)):      # this loop will traverse in opposite direction therfore I increment both the last and ist variable
                if val%2 != 0 : savedSequence = savedSequence + str(val) + '\t'        # val is 
        print(savedSequence)
    else : print('Invalid Input')
                
            
                
                
        
        
Odd()
        
    

   
