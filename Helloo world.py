

import random
database ={}
    
def open():

    
    print('Welcome to Pelbank')



    haveAccount = int(input("1. Login  2. Register  \n"))


    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()
    else:
        print('You have selected an invalid option')
        open()


def login():

        print('*******LOGIN********')
        
        accountNo = int(input('What is your account number?  \n'))
        userPassword = input('Input password  \n')

    
        
        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNo):
                if(userDetails[3] == userPassword):
                    bankOperation(userDetails)

        
        print('Invalid account number or password')
        login()


def register():

        print('********Register********')

        firstName = input('Firstname  \n')
        lastName = input('Lastname   \n')
        dob = input('Date of Birth   \n')
        emailAddress = input('Email Address  \n')
        user_name = input('Create Username  \n')
        userPassword = input('Create Password  \n')



        
        accountNumber = generationAccountNumber()

        
        database[accountNumber] = [ firstName, lastName, emailAddress, userPassword]
        print('Your account has been created')
        print('Your account number is: %d' % accountNumber)
        

   

        login()


            
def bankOperation(user):
        from datetime import datetime

        
        now = datetime.now()
 
        print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)




				
        print("Welcome %s %s " % ( user[0], user[1] ) )
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Pay Bills')
        print('4. Complaint')



        selectedOption = int(input("Please select an option  \n"))
        currentBalance = 50000

        if(selectedOption == 1):
            print("You have selected %s " %selectedOption)
            withDraw = int(input('How much would you like to withdraw?'))
            print('Take your cash')
            amount = currentBalance - withDraw
            print("Current Balance: " + str(amount))
             
                   
        if(withDraw > 50000):
            print('Insufficient Funds')
             
        elif(selectedOption == 2):
            print("You have selected %s " %selectedOption)
            amt = float(input('How much would you like to deposit?'))
            balance = currentBalance + amt
            print('Deposit Successful')
            print("Current Balance: " + str(balance))

        elif(selectedOption == 3):
            print('You have selected %s ' %selectedOption)
            print('What would you like to pay for?')
            print('1. Recharge')
            print('2. Data Bundles')
            print('3. Power')
            



			 
        elif (selectedOption == 4):
            print("You have selected %s " %selectedOption)
            input('What issue would you like to report?')
            print('Thank you for contacting us')
 

        else:
            print('You have picked an invalid option')
        bankoperation(user)      

def generationAccountNumber():
        return random.randrange(0000000000,9999999999)

def logout():
    login()

open()
