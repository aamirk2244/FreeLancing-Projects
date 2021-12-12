
def presentServices(): 
    # returning services in the from of dict
    return {'Firewall Service': 1.2, 
                'Security Ops Centre': 4.2,
                'Hot Site': 8.5,
                'Data Protection': 10.0
               }
def addServices(service = None):
    if service is None:     
        service = presentServices()

    serviceName = list(service)               # this will contain all service names 
    added = []
    getInput = '-1'          # initializing with some dummy value
    service_length = len(service)
    while  getInput != '0':
        getInput = input('Enter the service 1-{} that you would like to add, or 0 to stop:'.format(service_length))

        if getInput == '0':continue         # stopping th loop

        if int(getInput) < 1 or int(getInput) > service_length:
            print('Invalid Value: Enter valid Input')
            input('Enter to continue ..')
            continue
        added.append(serviceName[int(getInput)-1])          # adding the user selected service to the added list
        print(getInput + ' added')
    
    
    return added
        

def getAddedServices(services = None):
    return addServices(services)                 # ist calling to addServices function and directly returning services which the user added in that function

def displayServices(services): 
    serviceIndex = 1           # for service number
    
    
    
    for values in services:
        serviceName = values             # getting key and value from the dictionary , services
        amount = services[values]
#         1. Firewall Service	:	 $1.2k/year   # printing in this formatt 
        if serviceName == "Hot Site" : serviceName += '\t'   # adding tab to service name HOt service because it is affecting our padding
        
        print("{}. {}\t\t:\t ${}k/year".format(serviceIndex,serviceName,amount) ) # {} is the placeholder for the variables to print in required manner , .format funcion takes the variables to insert into the placeholder
        serviceIndex += 1
        
def payment(serviceAdded):
    defaultServices = presentServices()
    print('Please check your services added:\n\n')
    to_dict = {}
    for val in serviceAdded:
        to_dict[val] = defaultServices[val]                # converting the added services list to dictionary to show the equivalent amount
   
    displayServices(to_dict)        # displaying this added services 

    totalSum = sum(list(map(lambda service : defaultServices[service], serviceAdded  )))  # adding total of  all added services     
    if totalSum == 0:
        print('No Services added yet')
        return
    print('Your subscription will be a total of : ${}k/year.'.format(totalSum))
    print('Thank you for using ESP.')
    input('Press enter to continue')

def Search(services):
    serviceNames = services.keys()

    userSearch = input('please enter service to search: ')
    userSearch = userSearch.lower()
    foundServices = {}
    tempName = ''
    for names in serviceNames:
        tempName = names.lower()          # for working with both upper and lower case search
        if userSearch in tempName:
            foundServices[names] = services[names]        # key will be the service name and the value will be the amount of that service
    
    if len(foundServices) == 0 : 
        print('No services found ')
        input('press Enter to continue ..')
    else:
        displayServices(foundServices)
        return foundServices
        


def showHome():

    print('========================================================')
    print('Welcome to Electronic Services & Protection:')
    print('========================================================\n\n\n')
    print('\t 1. Display Our List of Services')
    print('\t 2. Search for Services')
    print('\t 3. Display added services')
    print('\t 4. Payment')
    print('\t 5. Exit ESP\n\n')
    
    
            
            



def startMain(): # setting main home page
    added_service = None
    services = presentServices()

    while True:
        showHome()
        getInput = input('\t Please input your choice of action (ENTER to exit):') # taking input from user
    

        if getInput == '1':
            print('Yes, we have the following service(s):')
            displayServices(services)
            added_service =  getAddedServices()
            
            if added_service == '0':          # i.e if the user wants to stop 
                clearConsole()            # clearing the whole console
        
        elif getInput == '2':    # searching 
            foundS = Search(services)
            if foundS is not None:
                print('Yes, we have the following service(s):')

                added_service =  getAddedServices(foundS)
           
        elif getInput == '3':
            if added_service is not None: 
                print('Services you have today : ', added_service)
                input('Press enter to continue ..')
            else : print('No Services added yet')
        
        elif getInput == '4':
            if added_service is not None: payment(added_service)
            else : print('No Services added yet')
        
        elif getInput == '5':
            input('Good Bye!!')
            return  

        elif getInput == '': 
            return
        else : print('Invalid Input..')      


        
   
    
startMain()
