#BR3 
#imports these plugins
import statistics
import csv


#initialising variables
calledLightLevel = []
calledSoundLevel = []
calledWellBeing = []
location = 0
minLightLevel = 0
#opens CSV file to read and data is ready to be called from CSV file
#and also renames function to file
with open ("WellbeingData.csv","r+") as file:
    #defines a reader to read CSV file
    reader= csv.DictReader(file)
    #loops to call light level, sound level and wellbeing and adds it to a list
    for row in reader:
        calledLightLevel.append(int(row["Light Level"]))
        calledSoundLevel.append(int(row["Sound Level"]))
        calledWellBeing.append(str(row["Wellbeing"]))
    
    #the students wellbeing should be "Terrible" on the day of minimum light level
    #defines minLightLevel to the minimum value in the list calledLightLevel
        #analysis component being calculated
    minLightLevel = min(calledLightLevel)
    #finds the day that this occured in the list
    location = calledLightLevel.index(minLightLevel)
    #finds the wellbeing on that day
    wellbeing = calledWellBeing[location]
    print("The minimum light level recorded throughout the month was",minLightLevel,
          "Which happened on day", location,
          "and on this day the students wellbeing was", wellbeing, "\n")
    #prediction of what wellbeing may be
    # if minLightLevel is within these light level the prediction will = these values
    if minLightLevel <50 or minLightLevel >=200:
        prediction = "Terrible"
    elif minLightLevel >=50 and minLightLevel <=80:
        prediction = "Bad"
    elif minLightLevel >=81 and minLightLevel <=100:
        prediction = "Good"
    elif minLightLevel >=101 and minLightLevel <=150:
        prediction = "Excellent"
    elif minLightLevel >=151 and minLightLevel <=180:
        prediction = "Good"
    elif minLightLevel >=181 and minLightLevel <=200:
        prediction = "Bad"
    #validation in case data is wrong
    else:
        ("Invalid data")
    #informing future decisions
    if prediction == "Terrible":
        print("This student will most likely procrastinate due to bad light level")
    elif prediciton == "Bad":
        print("This student may procrastiante due to bad light level")
    elif prediciton == "Bad":
        print("This student most likely will not procrastinate due to light level")
    elif prediciton == "Bad":
        print("This student will not procrastinate due to light level")
    else:
        print("Invalid data")
    
    
    #tests if prediction was accurate
    #if the actual data point is equal to the prediction then prediction was accurate
    if wellbeing == prediction:
        print("Prediction is accurate")
    #if not hten the prediction was inaccurate
    else:
        print("Prediction is inaccurate")
        
    print("\n")
    
    
    
    
    
    #When sound level is maximum the students wellbeing should be "Terrible"
    #calculates max of sound
    maxSoundLevel = max(calledSoundLevel)
    location = calledSoundLevel.index(maxSoundLevel)
    #gets the wellbeing value from the day maxsoundlevel happened
    wellbeing = calledWellBeing[location]
    
    print("The minimum light level recorded throughout the month was",maxSoundLevel,
          "Which happened on day", location,
          "and on this day the students wellbeing was", wellbeing, "\n")
    #this is also a prediction
    #the higher the sound the worse the wellbeing
    if maxSoundLevel >=200:
        prediction = "Terrible"
    elif maxSoundLevel >=150 and maxSoundLevel <=200:
        prediction = "Bad"
    elif maxSoundLevel >=100 and maxSoundLevel <=150:
        prediction = "Good"
    elif maxSoundLevel <=100:
        prediction = "Excellent"
    #validation in case data is wrong
    else:
        print("Invalid data")
    if prediction == "Terrible":
        print("This student will most likely procrastinate due to bad sound level")
    elif prediciton == "Bad":
        print("This student may procrastiante due to bad sound level")
    elif prediciton == "Bad":
        print("This student most likely will not procrastinate due to sound level")
    elif prediciton == "Bad":
        print("This student will not procrastinate due to sound level")
    else:
        print("Invalid data")
        
    #says whether data is a ccurate or not
    if wellbeing == prediction:
        print("Prediction is accurate")
    else:
        print("Prediction is inaccurate")
    
    
    

    
    
    
    
    
    