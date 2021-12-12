

def computeAverage():
    print("************************************")
    print("ST2414 PSEC Practical 2 Submission 1")
    print("************************************")

    count = 0         # for counting user values
    saved = list()        # will save the user values inorder to compute the average
    
    while True:          # while user doesn't input the Q
        a=input("Pls enter a number or Q to stop: ")
        if a == 'Q': break

        if not a.isnumeric():          # if input is not numeric
            print('Invalid Input, Enter Valid Input')
            continue        # continue loop
        count += 1
        print('Current total of {} values is {}'.format(count, a))
        saved.append(int(a))            # saving user input to the list
    avg = sum(saved)/len(saved)             # computing average from the user inputs
    print('Average of {} numbers is {: .2f}'.format(count,avg) )           # {: .2f} means compute upto the 2 deciaml places
 
computeAverage()
