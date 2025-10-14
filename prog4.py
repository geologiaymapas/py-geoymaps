"""
=========================
Carga de archivo CSV
=========================
"""
import csv
 
with open('data/example.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)