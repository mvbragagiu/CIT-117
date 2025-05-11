#Mihaela Bragagiu
#April 20 2025
#CIT-117-D01 - Python 2
#Numerology 
#This will use information prompted from the Use Numerology class to function

#################IMPORTS


import math
import time

class Numerology:

####################################
    def __init__(self, sName, sDOB):
        
        self.sName = sName
        self.sDOB = sDOB
        self.iPath = self.getLifePath()
        self.iBirthday = self.getBirthDay()
        self.iAttitude = self.getAttitude()
        self.iSoul = self.getSoul()
        self.iPersonality = self.getPersonality()
        self.iPower = self.getPowerName()

####################################

    def __str__(self):

        return f"Client Name: {self.sName}\nClient DOB: {self.sDOB}\nLife Path: {self.iPath}\nAttitude: {self.iAttitude}\nBirthday: {self.iBirthday}\nPersonality:{self.iPersonality}\nPower Name: {self.iPower}\nSoul: {self.iSoul}"
####################################
#####        FUNCTIONS         #####
####################################

    #returns the subjects name
    def getName(self): 

        return self.sName
    
    #returns the subjects Date of Birth
    def getBirthdate(self): 

         return self.sDOB
        
    #returns the computed attitude number
    def getAttitude(self): 
        temp = self.getBirthdate()
        iAttitude = int(temp[0])+int(temp[1])+int(temp[3])+int(temp[4])
        iAttitude = self._reduceToOne(iAttitude)
        return iAttitude

    #returns the computed birthday number
    def getBirthDay(self): 
        sTemp = self.getBirthdate()
        iBirthday = int(sTemp[3])+int(sTemp[4])#with the format we accepted, the day numbers should always be in these positions

        iBirthday = self._reduceToOne(iBirthday)
        
        return iBirthday

    #returns the computed life path number
    def getLifePath(self): 
        sTemp = self.getBirthdate()


        sTemp= sTemp.replace("-", "")
        sTemp= sTemp.replace("/", "")
        iPath = 0;
        for char in sTemp:
            iPath = iPath+ int(float(char))
            
        iPath = self._reduceToOne(iPath)
        
        return iPath

    #returns the computed personality number
    def getPersonality(self): 
        sTemp = self.getName()
        sTemp = sTemp.lower()
        iPersonality = 0
        for char in sTemp:
            if char not in ('a', 'e', 'i', 'o', 'u'):
                iTempNum = self._letterToNumberConverter(char)
                iPersonality = iPersonality + iTempNum
        iPersonality = self._reduceToOne(iPersonality)
        return iPersonality


    #returns the computed power name number
    def getPowerName (self): 
        iPower = self.iSoul+self.iPersonality
        iPower = self._reduceToOne(iPower)
        return iPower


    #returns the computed soul number
    def getSoul(self): 
        sTemp = self.getName()
        sTemp = sTemp.lower()
        iSoul = 0
        
        for char in sTemp:
            if char in ('a', 'e', 'i','o','u'):
                sTempNum = self._letterToNumberConverter(char)
                iSoul = iSoul + sTempNum
        iSoul = self._reduceToOne(iSoul)
        
        return iSoul


    
####################################
####     NO USING OUTSIDE      #####
#####         OF CLASS         #####
####################################
    #These methods have no use outside of this class

    #takes a number, and reduces it to a single digit
    def _reduceToOne(self, iInputtedNum):
        sTemp = str(iInputtedNum)
        iNumber = 0
        if (len(sTemp)>=2):
            while(int(sTemp)>9):
                iNumber=0
                for char in sTemp:
                    iNumber= iNumber+ int(char)
                sTemp = str(iNumber)
        else:
            iNumber = iInputtedNum
        
        return iNumber


    #Letters with the corresponding numbers to it.
    def _letterToNumberConverter(self,sTempChar):
        letterDict={}
        for key in ['a','j','s']:
            letterDict[key]=1
        for key in ['b','k','t']:
            letterDict[key]=2
        for key in ['c','l','u']:
            letterDict[key]=3
        for key in ['d','m','v']:
            letterDict[key]=4
        for key in ['e','n','w']:
            letterDict[key]=5
        for key in ['f','o','x']:
            letterDict[key]=6
        for key in ['g','p','y']:
            letterDict[key]=7
        for key in ['h','q','z']:
            letterDict[key]=8
        for key in ['i','r']:
            letterDict[key]=9

        #end of dictionary terms
        if sTempChar.lower() in letterDict:
            iNumber = letterDict[sTempChar.lower()]
        else:
            iNumber = 0##this is if the letter is not an alphabetical letter.

        return iNumber

        
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