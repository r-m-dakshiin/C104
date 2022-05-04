import csv
import statistics
import pandas as pd
with open('HeightWeight.csv') as f:

    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
for i in range(len(file_data)):
  n_num = file_data[i][2]
  new_data.append(float(n_num))
    
n = len(new_data)
total = 0

for x in new_data:
  total += x

mean = total/n

print("Mean / Average is: " + str(mean))



new_data.sort()
if n % 2 == 0:
    #getting the first number
	median1 = float(new_data[n//2])
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
    
    
else:
    median = float(new_data[n/2])

print("The Median is : "+str(median))
    