import csv
import random

def readfile(file_name):
    
    occupations = []
    percentages = []
    
    with open(file_name, mode='r') as file:
        data = csv.reader(file)
        next(data)
      # skips first line
        for row in data:
            
            occupation = row[0]
            percentage = float(row[1])/100
            occupations.append(occupation)
            percentages.append(percentage)
        
        
        occupations = occupations[0:-1]
        percentages = percentages[0:-1]
        
    return occupations, percentages

def chooseOccupation(occupations, percentages):
    rand = random.random()
    percentage = 0
    
    for i in range(len(occupations)):
        percentage += percentages[i]
        if (rand < percentage):
            return occupations[i], percentages[i] * 100
            

occupations, percentages = readfile('occupations.csv')
print(chooseOccupation(occupations, percentages))


#print(readfile('occupations.csv'))
    
    