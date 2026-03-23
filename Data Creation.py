#importing these plugins
import random
import statistics
import csv




#initialising variables (lists)
lightLevel  = []
soundLevel = []
time = []
wellbeing = []
data = []

#Makes a new csv file to thats able to have data written to it
with open("WellbeingData.csv","w",newline = '') as file:
    #loops 30 times assuming light + sound are their mean values for that day
    # and the student only has one study session
    for i in range (30):
        #setting random numbers for each of these within their respective ranges
        ranwellbeing = random.randint(1,4)
        rantime = random.randint(1,4)
        
        light = random.randint(0,255)
        sound = random.randint(0,255)
        #appends light and sound to lightLevel and soundLevel list
        lightLevel.append(light)
        soundLevel.append(sound)
        
        #if statements to change the time cycling values to actual minutes    
        if rantime == 1:
            timeScore = 15
        elif rantime == 2:
            timeScore = 30
        elif rantime == 3:
            timeScore = 60
        elif rantime == 4:
            timeScore = 120
            #Range validation has to be between 1-4
        else:
            print("Value has to be between 1 - 4")
        #appends the time in minutes to this list   
        time.append(timeScore)
        #if statements to change the random number from 1-4 into different wellbeing strings
        #to be transfered into the CSV file
        if ranwellbeing == 1:
            strranwellbeing = "Terrible"
            #appends ranwellbeing to the wellbeing list
            wellbeing.append(ranwellbeing)
    
        elif ranwellbeing == 2:
            strranwellbeing = "Bad"
            wellbeing.append(ranwellbeing)
        
        elif ranwellbeing == 3:
            strranwellbeing = "Good"
            wellbeing.append(ranwellbeing)
        
        elif ranwellbeing == 4:
            strranwellbeing = "Excellent"
            wellbeing.append(ranwellbeing)
        #validation if outside range
        
        else:
            print("incorrect data entered")
        # this appends all of these values to the list data to be written to CSV file   
        data.append([i, light, sound, timeScore, strranwellbeing])
    #creates a writer to write our code into the csv file
    write = csv.writer(file)
    #writes a premade title row 
    write.writerow(["Day","Light Level","Sound Level", "Time (mins)", "Wellbeing"])
    # for how many rows are in data is how many rows will be written in this case 30
    for row in data:
        write.writerow(row)
        
        
        
        

    
    
    
    
    
    
    
    
    
    
    






        
        
    


    
    

    
