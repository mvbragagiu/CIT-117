# Mihaela Bragagiu
#Feburary 23
#CIT-117-D01 - Python 2
#Password Validator
#Validates a inputted password

#################IMPORTS

#NO IMPORTS AT THE MOMENT

#################FUNCTIONS


##########NAME RELATED FUNCTIONS###############
######Get name input and validate
def getNameInput(sText):
    while True:
        try:
            sName = input(sText)
            sSplitNames = sName.split()
            if len(sName)<3:
                raise ValueError
            if len(sSplitNames) <2:
                raise ValueError
            return sName
        except ValueError:
            print("Your name should be longer than 2 characters and have a first and last name.")
        else:
            break



######Get Initials
def getInitials(sName): 
    lNameSplit = sName.split()
    sInitials = lNameSplit[0][0] + lNameSplit[1][0]
    return sInitials


###########PASSWORD RELATED FUNCTIONS################
######Gets a password from input, makes sure it's valid
def getValidPassword(sText, sInitials):
    
    specialCharacters = "!@#$%^"
    while True:

        #######Error if password not 8-12 characters
        try:
            sPassword = input(sText)
            if len(sPassword) <8 or len(sPassword) > 12:
                raise ValueError
        #######Error if password contains pass
            try:
                if "pass" in sPassword.lower():
                    raise ValueError
        #######Error if password doesn't contain 1 uppercase
                try:
                    if sPassword.lower()==sPassword:
                        raise ValueError
        #######Error if password doesn't contain 1 lowercase
                    try:
                        if sPassword.upper()==sPassword:
                            raise ValueError
        #######Error if password doesn't contain a number
                        try:
                            iTempCounter=0
                            for char in sPassword:
                                if ('0' == char)or ('1' == char) or ('2' == char) or ('3' == char)or ('4' == char)or ('5' == char)or ('6' == char)or ('7' == char)or ('8' == char)or ('9' == char):
                                    iTempCounter = iTempCounter+1
                            if iTempCounter<1:
                                raise ValueError
        #######Error if password doesn't contain a special character
                            try:
                                iTempCounter=0
                                iTempCounter2=0
                                bSpecialCheck = False
                                for iTempCounter in range(len(sPassword)):
                                    for iTempCounter2 in range(len(specialCharacters)):
                                        if sPassword[iTempCounter]==specialCharacters[iTempCounter2]:
                                            bSpecialCheck = True
                                            break
                                        iTempCounter2= iTempCounter2+1
                                    iTempCounter= iTempCounter+1
                                    iTempCounter2= 0
                                if bSpecialCheck ==False:
                                    raise ValueError
        #######Error if password contains initials
                                try:
                                    if sInitials.lower() in sPassword.lower():
                                        raise ValueError
                                    break
                                except ValueError:
                                    print("Password must not contain user initials.")
                            except ValueError:
                                print("Password must have at least 1 special character.")
                        except ValueError:
                            print("Password must have at least 1 number.")
                    except ValueError:
                        print("Password must have at least 1 lowercase letter.")
                except ValueError:
                    print("Password must have at least 1 uppercase letter.")       
            except ValueError:
                print("Password can’t start with Pass")
        except ValueError:
            print("Password must be between 8 and 12 characters.")
        #except initialsError:
        #    print("")
        #except characterOccurenceError:
        #    print("These characters appear more than once:")
            ###need to create code that prints what the code kept track of here

    ###at this point all exceptions should've been gone through
    return sPassword



######Takes the password and counts all the times a character appears
def getCounter(sPassword):
    
    
    iTempCounter=0
    iCounterSwitch=False
    try:
        for iTempCounter in range((len(sPassword))):
            iTempCounter2 = sPassword.count(sPassword[iTempCounter])
            if iTempCounter2 >=2:
                iCounterSwitch=True
                print(str(sPassword[iTempCounter])+" appears "+str(iTempCounter2) + " times.")
            if iCounterSwitch==True:
                raise ValueError
    except ValueError:
        print("Password cannot have repeating characters.")
    if iCounterSwitch == True:
        return True
    else:
        return False
            



#################
#
#
#
#
#
#################MAIN CODE STARTS HERE

def main():
    sValidCounter=False
    
    ##Get all the inputs
    sName = getNameInput("Please enter your full name such as John Smith: ")
    sInitials = getInitials(sName)
    while True:
        sPassword = getValidPassword("Please input a new password: ",sInitials)
        sValidCounter = getCounter(sPassword)

        ##check if not repeats, then the password is valid
        if sValidCounter != True:
            print("Password is valid and OK to use")
            break
          
    return
############################

#call main code
main()