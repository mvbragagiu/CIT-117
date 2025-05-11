# Mihaela Bragagiu
#March 9
#CIT-117-D01 - Python 2
#Inter Plantary Weights
#Calculate person's weight on different planets in solar system using dictionaries and pickling

#################IMPORTS

import pickle

#################FUNCTIONS


#check for valid pickle
def checkPickle(dictPlanetHistory):
    eof = False
    try:
        input_file = open('mbPlanetaryWeights.db', 'rb')

        ##read and load pickle pile
        while not eof:
            try:
                dictPlanetHistory = pickle.load(input_file)
            except EOFError:
                eof=True
        input_file.close()
    except FileNotFoundError:
        pass
    return dictPlanetHistory

    


##show history if user wants to see
    while True:
        try:
            print("Would you like to see the history?: ")
            sYesNo = input()
            if ((sYesNo=='Y')or(sYesNo=='y')):
                print(dictPlanetHistory)
            elif((sYesNo != 'N')or(sYesNo!='n')):
                raise ValueError
            return sName
        except ValueError:
            print("Please write Y for yes or N for no.")
        else:
            break

    return dictPlanetHistory

###Get unique name
def getName(dictPlanetHistory, prompt):

    sName = input(prompt)

    while True:
        try:
            if ((sName in dictPlanetHistory)or(sName.upper() in dictPlanetHistory)or(sName.lower() in dictPlanetHistory)) :
                raise ValueError
            elif(sName==""):##blank name
                break
        except ValueError:
            print("The name must be unique.")
            sName = input(prompt)
        else:
            break

    return sName

###get a valid weight
def getEarthWeight(prompt):

    while True:

        try:
            fEarthWeight = float(input(prompt))
            if ((fEarthWeight<=10) or (fEarthWeight>=1400)) :
                raise ValueError
        except ValueError:
            print("Not Valid input.")
        else:
            break
    return fEarthWeight


###print out your weight on all the plants
def weightOnPlanets(sName,dictPlanetsData,fEarthWeight,dictPersonWeights):
    listPlanetNames = list(dictPlanetsData.keys())

    fMultiplyTemp =0.0
    fTemp =0
    print(sName,f", here are your weights on our Solar System's planets.")
    
    while(fTemp<(len(dictPlanetsData))):
        fMultiplyTemp = round((fEarthWeight * dictPlanetsData[listPlanetNames[fTemp]]),2)
        print(f"Weight on {(listPlanetNames[fTemp]+':'):10} {fMultiplyTemp:>10}")

        
        dictPersonWeights[listPlanetNames[fTemp]]=fMultiplyTemp##add to dictionary
        fTemp=fTemp+1
        

    return dictPersonWeights



#################
#
#
#
#
#
#################  MAIN CODE STARTS HERE   ##################

def main():

    ##planet dictionary with weights
    dictPlanetsData = {"Mercury":0.38,"Venus":0.91,"Moon":0.165,"Mars":0.38,"Jupiter":2.34,"Saturn":0.93,"Uranus":0.92,"Neptune":1.12,"Pluto":0.066}
    dictPlanetHistory={}

    #input file and get dictPlanetHistory
    dictPlanetHistory = checkPickle(dictPlanetHistory)

    #get valid name and weight inputs
    sName = getName(dictPlanetHistory,"Please enter your name: ")
    fEarthWeight = getEarthWeight("Please enter a your weight on earth: ")

    #calculate weight on planets
    dictPersonWeights ={}
    dictPersonWeights = weightOnPlanets(sName,dictPlanetsData,fEarthWeight,dictPersonWeights)

    #get dictionary of person name with all their weights
    dictPlanetHistory[sName] = dictPersonWeights


    #output file
    output_file=open('mbPlanetaryWeights.db', 'wb')
    pickle.dump(dictPlanetHistory,output_file)
    output_file.close()

    #print in terminal just in case

    for key, value in dictPlanetHistory.items():
        print (key,value)
    
    
          
    return
##################################################################

#call main code
main()