#AR2 + AR3
#imports matplotlib plugin
import matplotlib.pyplot as plt
#asks the user to input values to begin the validatio process
print("Enter following values to start validation")
light = float(input("Enter light level (0 - 255): "))
sound = float(input("Enter sound level 0 - 255) "))
time = int(input("Enter time studied as an integer in minutes: "))
#initialises wellbeing score as a float
wellbeing_score = float(0)

#defines light_validation to validate the variable light
def light_validation(light):
    #validates range of light (must be in the range of 0 - 255)
    if light < 0 or light > 255:
        print("Light have to be between 0-255")
        #returns boolean value of false
        return False
    #if there are no problems sends boolean value of True 
    return True
#defines sound_validation to validate the variable sound        
def sound_validation(sound):
    #validates range of sound (must be in the range of 0 - 255)
    if sound < 0 or sound > 255:
        print("Sound have to be between 0-255")
        return False
    return True
#defines time_validation to validate the variable time         
def time_validation(time):
    #time has to be a positive integer
    if time <= 0:
        print("Time has to be a positive integer")
        return False
    return True
        
#this calls all of the functions and if one value is flagged as wrong then prints
#invalid inputs
if not light_validation(light) and sound_validation(sound) and time_validation(time):
    print("Invalid Inputs")
    
#what if 1
#What would happen to a students wellbeing if they only studied for 10 minutes
#if there was no validation issues this code should run
else:
    #time hard coded to 10
    time = 10
    #validates the hardcoded value of time
    if not time_validation:
        print("Invalid Inputs")
    else:
    #add light and sound together    
        wellbeing_score = light + sound
    #then multuiply it by 10 to get a well being score
        wellbeing_score = wellbeing_score * time
    #if wellbeing score is in these ranges it defines wellbeing as one of 4 string values
    #"terrible" "bad" "good" "excellent"
        if wellbeing_score <= 1500 or wellbeing_score >= 3500:
            wellbeing = "Terrible"
            #prints the students wellbeing
            print("This students wellbeing is", wellbeing)
            #prints bar chart
            #defines lables
            lables = ["light", "sound", "time"]
            #data list takes the 
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 10 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()

            
        elif wellbeing_score >=1500 and wellbeing_score <=2000:
            wellbeing = "Bad"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 10 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            
            
        elif wellbeing_score >=3000 and wellbeing_score <=3500:
            wellbeing = "Bad"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 10 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            

        elif wellbeing_score >=2000 and wellbeing_score <=2300:
            wellbeing = "Good"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 10 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            
            
        elif wellbeing_score >= 2700 and wellbeing_score <= 3000:
            wellbeing = "Good"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 10 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            
            

        elif wellbeing_score >= 2300 and wellbeing_score <=2700:
            wellbeing = "Excellent"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 10 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
    
print("Enter new values for what- if question 2")  
light = float(input("Enter light level (0 - 255): "))
sound = float(input("Enter sound level 0 - 255) "))
time = int(input("Enter time studied as an integer in minutes: "))


if not light_validation(light) and sound_validation(sound) and time_validation(time):
    print("Invalid Inputs")
    
#what if question 2
#What would happen to a students wellbeing if they studied for 120 minutes
else:
    time = 120
    if not time_validation:
        print("Invalid Inputs")
    else:

        wellbeing_score = light + sound
        wellbeing_score = wellbeing_score * time

        if wellbeing_score <= 12000  or wellbeing_score >= 42000:
            wellbeing = "Terrible"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 120 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()

            
        elif wellbeing_score >=12000 and wellbeing_score <=18000:
            wellbeing = "Bad"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 120 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            
            
        elif wellbeing_score >=36000 and wellbeing_score <=42000:
            wellbeing = "Bad"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 120 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            

        elif wellbeing_score >=18000 and wellbeing_score <=24000:
            wellbeing = "Good"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 120 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            
            
        elif wellbeing_score >= 30000 and wellbeing_score <= 36000:
            wellbeing = "Good"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 120 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
            
            

        elif wellbeing_score >= 24000 and wellbeing_score <=30000:
            wellbeing = "Excellent"
            print("This students wellbeing is", wellbeing)
            
            lables = ["light", "sound", "time"]
            data = [light, sound, time]
            plt.figure(figsize=(5, 5))
            plt.bar(lables, data, color=["red","yellow","blue"])
            plt.title("What would happen to a students wellbeing if they only studied for 120 minutes")
            plt.xlabel("Factors")
            plt.ylabel("Data")
            plt.show()
    
    

        
    
    

     
    
        







