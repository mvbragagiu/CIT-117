#Mihaela Bragagiu
#April 27 2025
#CIT-117-D01 - 
#Numerology 
#This will use information prompted from the Use Numerology class to function

#################IMPORTS


import math

class NumerologyLifePathDetails:
    sName =""
    sDob = ""
    __iPersonalityNumber =0
    __iSoulNumber =0
    __iLifePathNumber =0
    __iAttitudeNumber =0
    __iBirthdayNumber =0
    __iPowerName =0
    

####################################
    def __init__(self, Name, DOB):
        self.sName = Name
        self.sDob = DOB
        ##compute personality
        iTemp=0
        for char in self.sName:
            if char not in ('a', 'e', 'i', 'o', 'u'):
                iTempNum = self.convertCharToInteger(char)
                iTemp = iTemp + iTempNum
        self.__iPersonalityNumber = self.__reduceNumber(iTemp)

        ##compute soul number
        sTemp = self.sName
        sTemp = sTemp.lower()
        iTemp =0
        for char in sTemp:
            if char in ('a', 'e', 'i','o','u'):
                sTempNum = self.convertCharToInteger(char)
                iTemp = iTemp + sTempNum
        self.__iSoulNumber = self.__reduceNumber(iTemp)

        ##compute life path
        sTemp = self.sDob
        sTemp= sTemp.replace("-", "")
        sTemp= sTemp.replace("/", "")
        iTemp = 0;
        for char in sTemp:
            iTemp = iTemp+ int(float(char))
        self.__iLifePathNumber = self.__reduceNumber(iTemp)

        ##compute attitude
        iTemp = self.sDob
        self.__iAttitudeNumber = self.__reduceNumber((int(iTemp[0])+int(iTemp[1])+int(iTemp[3])+int(iTemp[4])))

        ##compute birthday number
        sTemp = self.sDob
             #with the format we accepted, the day numbers should always be in these positions below
        self.__iBirthdayNumber = self.__reduceNumber((int(sTemp[3])+int(sTemp[4])))

        ##compute powername
        iTemp = self.__iSoulNumber+self.__iPersonalityNumber
        self.__iPowerName = self.__reduceNumber(iTemp)
        

####################################

    def __str__(self):
        return f"Client Name: {self.sName}\nClient DOB: {self.sDob}\nLife Path: {self.__iLifePathNumber}\nAttitude: {self.__iAttitudeNumber}\nBirthday: {self.__iBirthdayNumber}\nPersonality:{self.__iPersonalityNumber}\nPower Name: {self.__iPowerName}\nSoul: {self.__iSoulNumber}"

##print function optional (ignore this please)
#def prinout(self):
#        def wrapper():
#            print(f"Client Name: {self.sName}")
#            print(f"Client DOB: {self.sDOB}")
#            print(f"Life Path: {self.iPath}")
#            print(f"Attitude: {self.iAttitude}")
#            print(f"Birthday: {self.iBirthday}")
#            print(f"Personality:{self.iPersonality}")
#            print(f"Power Name: {self.iPower}")
#            print(f"Soul: {self.iSoul}")
#        return wrapper


####################################
#####      GET FUNCTIONS       #####
####################################

    #returns the subjects name
    @property
    def Name(self): 
        return self.sName
    
    #returns the subjects Date of Birth
    @property
    def Birthdate(self):
        return self.sDob

    #returns the computed personality number
    @property
    def Personality(self):      
        return self.__iPersonalityNumber
    
    #returns the computed soul number
    @property
    def SoulNumber(self):       
        return self.__iSoulNumber
    
    #returns the computed life path number
    @property
    def LifePath(self):
        return self.__iLifePathNumber
    
    #returns the computed attitude number
    @property
    def Attitude(self):
        return self.__iAttitudeNumber
    
    #returns the computed birthday number
    @property
    def BirthDay(self):
        return self.__iBirthdayNumber

    #returns the computed power name number
    @property
    def PowerName(self):
        return self.__iPowerName


    
####################################
####     NO USING OUTSIDE      #####
#####         OF CLASS         #####
####################################
    #These methods have no use outside of this class

    #takes a number, and reduces it to a single digit (taken from Mr. Candido's corrections)
    def __reduceNumber(self, iNumber):
        while (len(str(iNumber)) > 1):
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber


    #Letters with the corresponding numbers to it. (taken from Mr. Candido's corrections)
    def convertCharToInteger(self, sCharacter):

        #initialize to 0 incase a Non A-Z is passed in:
        iCharacterToNumberValue = 0
       
        #Check for A-Z
        if sCharacter.isalpha() :
            # Get the ASCII equivalent for upper A-Z and subtract how
            # many charcters after from captial A and then do math
            # get the numerology equivalent from 1 - 9:
            iCharacterToNumberValue = (( ord(sCharacter.upper() )  - 65) % 9 + 1)
            #print(sCharacter,ord(sCharacter), iCharacterToNumberValue)
 
        return iCharacterToNumberValue
        
####################################
#####       MISC CLASSES       #####
####################################


##Get a name with atleast one letter so the program works
def setValidName():
    prompt = ("Please enter a valid name at least one letter: ")
    sName = input(prompt)

    while True:
        try:
            if (len(sName)<1):
                raise ValueError
            elif(sName==""):##blank name
                raiseValueError
            elif(sName==" "):##blank name
                raiseValueError
        except ValueError:
            sName = input(prompt)
        else:
            break

    return sName



##Get a date with the date in the wanted format.
def setValidDate():
    prompt = ("Please enter your birthday in the MM/DD/YYYY or MM-DD-YYYY format: ")
    sDOB = input(prompt)

    while True:
        try:
            if (len(sDOB)!=10):#Including symbols, the date should be 10 characters
                raise ValueError
            elif((sDOB[2]!='/')and (sDOB[2]!='-')):##doesnt have correct dividers
                raiseValueError
            elif((sDOB[5]!='/')and (sDOB[5]!='-')):##doesnt have correct dividers
                raiseValueError
                
            elif not((sDOB[0].isdigit)and(sDOB[1].isdigit)and (sDOB[3].isdigit) and (sDOB[4].isdigit) and (sDOB[6].isdigit) and (sDOB[7].isdigit) and (sDOB[8].isdigit) and (sDOB[9].isdigit)):##checks if stripped string is only numbers
                raiseValueError
        except ValueError:
            sDOB = input(prompt)
        else:
            break

    return str(sDOB)





###LifePathDescription
class LifePathDescription(NumerologyLifePathDetails):
    __sPathDescription=""

    def __init__(self, sName, sDob):
        NumerologyLifePathDetails.__init__(self, sName, sDob)
        self.__sPathDescription = self.getLifePathDescription
        

    #get string for path based on dictionary
    @property
    def getLifePathDescription(self):
        path_dict ={
            1: "The Independent:\n                     Wants to work/think for themselves",
            2: "The Mediator:\n                     Avoids conflict and wants love and harmony",
            3: "The Performer:\n                     Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker:\n                     Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer:\n                     Likes to travel and meet others, often a extrovert",
            6: "The Inner Child:\n                     Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist:\n                     Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive:\n                     Gravitates to money and power",
            9: "The Humanitarian:\n                     Helps others and/or experiences pain and learns the hard way",
            }
        sPathDescription = path_dict.get(self.LifePath)
        
        return sPathDescription