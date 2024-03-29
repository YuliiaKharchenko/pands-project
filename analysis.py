# Analysis of Iris flower dataset using Python

# Autor Yuliia Kharchenko 

import csv 
import pandas as pd 

filename="iris.csv"

def readFile():
 
 with open(filename, "rt") as irisset:
    try:
       readfile=csv.reader(irisset,delimiter=",")
       firstline=True
       for line in readfile: 
            if firstline:
               firstline=False
               continue
            # print(line)
    except FileNotFoundError: #the error type 
        print(filename, "does not exist!") # output the message when an error occurs

readFile()

def Summary(): 
    df=pd.read_csv("iris.csv")
    general=df.describe()
    print( general)

    if __name__ == '__main__':
     with open ("summary.txt", "wt") as f: 
         for f in general:
             print(f)
 
Summary()