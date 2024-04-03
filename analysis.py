# Analysis of Iris flower dataset using Python

# Autor Yuliia Kharchenko 

import csv 
import pandas as pd 

filename="iris.csv"
file="summary.txt"


def readwithPands():
   data=pd.read_csv("iris.csv")
   summaryinfo= data.describe()
   return  summaryinfo
# print(readwithPands())


def readFile():
    with open(filename, "rt") as irisset:
       try:
          readfile=csv.reader(irisset,delimiter=",")
          firstline=True
          for line in readfile: 
            if firstline:
               firstline=False
               continue
           #  print(line)
       except FileNotFoundError: #the error type 
        print(filename, "does not exist!") # output the message when an error occurs

readFile()

def summaryInfo(): 
    results=readwithPands()
    with open (file, "wt") as f:
       print(results, file=f)

if __name__ == '__main__':
 
 summaryInfo()
 readwithPands()