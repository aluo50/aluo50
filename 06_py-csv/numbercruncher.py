import csv
import random

def readfile(file_name):
    
    occupations = []
    percentages = []
    
    with open(file_name, mode='r') as file:
        data = csv.reader(file)
      # we removed the first line of the csv  
        for row in data:
            
            occupation = row[0]
            percentage = float(row[1])/100
            occupations.append(occupation)
            percentages.append(percentage)
        
        
        occupations = occupations[0:-2]
        percentages = percentages[0:-2]
        
    return occupations, percentages

def chooseOccupation(occupations, percentages):
    rand = random.random()
    percentage = 0
    
    for i in range(len(occupations)):
        percentage += percentages[i]
        if (rand < percentage):
            return occupations[i], percentages[i]
            percentage = 0

occupations, percentages = readfile('occupations.csv')
print(chooseOccupation(occupations, percentages))


#print(readfile('occupations.csv'))
    
    