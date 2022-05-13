import csv

def parse_data_from_file(filename):
    
    temperatures = []

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile, delimiter=",")
        
        # Skip the first line
        next(reader)
  
        # Append to lists
        for row in reader:
            temperatures.append(float(row[1]))
            
    return temperatures
