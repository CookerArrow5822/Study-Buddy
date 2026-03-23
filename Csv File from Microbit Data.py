#imports csv + serial plugin
import serial
import csv
#defines the variable score
score = 0
#creates ser as a serial object
ser = serial.Serial()
#sets serial baudrate to 115200
ser.baudrate = 115200
#identifies com9 is being used and locates it to collect data
ser.port = "COM9"
# opens the port to ready it to send/accept data
ser.open()

#this opens the premade csv file of StudyBuddy and renames it as file 
with open ("StudyBuddy.csv","a") as file:
    #iterates 20 times
    for i in range (20):
        #reads data and strips it of any excess information (Eoin Gallen)
        data = ser.readline().decode().strip()
        #defines variable intData to be the integer form of data as it is a string
        intData= int(data)
        #Validation
        #if the data is less than 0 or more than 255 it rejects that piece of data
        #and prints the message below
        if intData <0 or intData > 255:
            print("Data values have to be within 0 - 255")
        #if the data is not an integer it rejects the data and prints the message below   
        elif data.isdigit() == False:
            print("Value has to be an integer")
        #if there are no problems the data will write to the csv file
        else:
            #redefines intData to string so the write function can write it to the csv file
            file.write(str(intData) + "\n")
            #prints the data so you know it is functioning correctly and can see the values
            #that are being transefered to the csv file
            print(intData)
            print("")
 
    #asks the user to input an integer and rate 1-10 on the study session
    studySession = int(input("Rate the study session 1-10" ))
    #studySession validation, input has to between 0 and 10
    if studySession <1 or studySession >10:
        print("Input has to be between 1 and 10")
    else:
    #defines the variable score as score + studySession
        score = score + studySession
    #asks user for integer on the confidence they have for the next test
    confidence = int(input("On a scale of 1-10 how confident are you for the next test? "))
    if confidence <1 or confidence >10:
        print("Input has to be between 1 and 10")
    #redefines score variable to score + confidence
    score = score + confidence
    #asks the user for input on stress levels they are feeling at the moment
    stress = int(input("On a scale of 1-10 how stressed are you?" ))
    if stress <1 or stress >10:
        print("Input has to be between 1 and 10")
    #redefines score to score minus stress
    score = score - stress


    #if score is within 15 and 20 it will print the following text and set wellbeing to excellent
    if score >= 15 and score <=20:
        print("Wellbeing is excellent")
        wellbeing = "excellent"
    #if score is within 10 and 14 it will print the following text and set wellbeing to good
    elif score >= 10 and score <=14:
        print("Wellbeing is good")
        wellbeing = "good"
    #if score is within 5 and 9 it will print the following text and set wellbeing to bad    
    elif score >= 5 and score <=9:
        print("Wellbeing is bad")
        wellbeing = "bad"
    #every other value sets wellbeing to terrible
    else:
        print("Wellbeing is terrible")
        wellbeing = "terrible"
    #writes wellbeing results to csv file
    file.write(str(wellbeing))
    file.close()
    

