# Analysis of Iris flower data set using Python

# Autor Yuliia Kharchenko 

import csv 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


filename="iris.csv"
file="Summary.txt"


def readwithPands():
   try:
      data=pd.read_csv(filename)
      return data 
   except FileNotFoundError:
      print(f"File{filename} is not found")
     
   
def summaryInfo():
   data= readwithPands()
   summaryinfo= data.describe()
   return  summaryinfo

def readFileCSV():
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


def summaryInfoResults(): 
    results=summaryInfo()
    with open (file, "wt") as f:
       print(results, file=f)

def separateSummaryInfo():
    data = readwithPands()
    # Obtain the names of all columns in the df data
    columns = data.columns
    # Iterate over each column
    for column in columns:
      separateSummary = data[column].describe()
      separateFiles = f"{column}(Summary).txt"
      with open(separateFiles, "wt") as f:
         print(separateSummary, file=f)

def safeHistogram():
    data = readwithPands()
    # Iterate over each column
    for column in data:
        # Create a histogram
        plt.figure(figsize=(8, 6))
        plt.hist(data[column], color="purple", edgecolor="black")
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.grid()
        plt.ylabel("Frequency")
        # Save the histogram as a PNG file
        plt.savefig(f"{column}_histogram.png")
        plt.close()  # Close the current figure to free up memory

def saveScatterPlot():
   data = readwithPands()
   sns.pairplot(data, hue="species of flowers", palette="Paired")
   plt.legend()
   # Save the scatter plot as a PNG file
   plt.savefig("scatter_plot.png")
   plt.close()


if __name__ == "__main__":
   summaryInfoResults()
   separateSummaryInfo()
   safeHistogram()
   saveScatterPlot()