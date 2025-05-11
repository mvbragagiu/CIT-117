#Mihaela Bragagiu
#April 27 2025
#CIT-117-D01 - Python 2
#Uuse Numerology
#This will prompt the user for the username and birthday that will be used in the Numerology class

#################IMPORTS

import NumerologyLifePathDetails

#################MAIN METHOD
def main():
    ##Get input
    sName = NumerologyLifePathDetails.setValidName()
    sDate = NumerologyLifePathDetails.setValidDate()

    ##Calculate all the numbers
    client = NumerologyLifePathDetails.LifePathDescription(sName,sDate)

    ##Output using the method
    print(client)
    print(client.getLifePathDescription)
    print("\n")##Gap between the two prints
    
    ##Output in format
    print(f"Client Name: {client.Name}")
    print(f"Client DOB: {client.Birthdate}")
    print(f"Life Path Number:    {client.LifePath}")
    print(f"Birth Day Number:    {client.BirthDay}")
    print(f"Attitude Day Number: {client.Attitude}")
    print(f"Soul Number:         {client.SoulNumber}")
    print(f"Personality Number:  {client.Personality}")
    print(f"Power Name Number:   {client.PowerName}")
    print(f"Power Name Number:   {client.getLifePathDescription}")
main()