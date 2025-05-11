#Mihaela Bragagiu
#April 20 2025
#CIT-117-D01 - Python 2
#Uuse Numerology
#This will prompt the user for the username and birthday that will be used in the Numerology class

#################IMPORTS

import Numerology


#################MAIN METHOD
def main():
    ##Get input
    sName = Numerology.setValidName()
    sDate = Numerology.setValidDate()

    ##Calculate all the numbers
    client = Numerology.Numerology(sName,sDate)

    ##Output using the method
    print(client)
    print("\n")##Gap between the two prints
    
    ##Output in format
    print("Client Name:", client.sName)
    print("Client DOB: ", client.sDOB)
    print(f"Life Path Number:    {client.iPath}")
    print(f"Birth Day Number:    {client.iBirthday}")
    print(f"Attitude Day Number: {client.iAttitude}")
    print(f"Soul Number:         {client.iSoul}")
    print(f"Personality Number:  {client.iPersonality}")
    print(f"Power Name Number:   {client.iPower}")
main()