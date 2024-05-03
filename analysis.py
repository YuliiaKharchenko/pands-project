# Analysis of Iris flower dataset using Python

# Autor Yuliia Kharchenko 


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import ratio
from pandas_profiling import ProfileReport

filename="iris.csv"
file="Summary.txt"


def read_with_pandas():
   try:
      data=pd.read_csv(filename)
      return data 
   except FileNotFoundError:
      print(f"File{filename} is not found")
     
   
def summary_info():
   data= read_with_pandas()
   summaryinfo= [
      "Summary information of Iris dataset (description of the data in the DataFrame)",
      "--------" * 10, 
      "General characteristics of variables",
      "--------" * 10, 
      data.describe(),
      "--------" * 10,
      "Checking of missing values",
      "--------" * 10, 
      data.isnull().sum(),
      "--------" * 10, 
      "Count the number of flowers of each species",
      "--------" * 10,
      data["species of flowers"].value_counts(),
      "--------" * 10,
      "Setosa species description",
      "--------" * 10,
      data.loc[data["species of flowers"]=="Iris-setosa"].describe(),
       "--------" * 10,
      "Versicolor species description",
      "--------" * 10,
      data.loc[data["species of flowers"]=="Iris-versicolor"].describe(),
       "--------" * 10,
      "Virginica species description",
      "--------" * 10,
      data.loc[data["species of flowers"]=="Iris-virginica"].describe(),
      "--------" * 10
   ]
   return  summaryinfo


def summary_info_results(): 
   results=summary_info()
   with open(file, "wt", encoding="utf-8") as f:
        for result in results:
            print(result, file=f)


def separate_summary_info():
    data = read_with_pandas()
    # Obtain the names of all columns in the df data
    columns = data.columns
    # Iterate over each column
    for column in columns:
      separateSummary = data[column].describe()
      separateFiles = f"{column}(Summary).txt"
      with open(separateFiles, "wt") as f:
         print(separateSummary, file=f)


def safe_histogram():
    data = read_with_pandas()
    # Iterate over each column
    for column in data:
        # Create a histogram
        plt.figure(figsize=(10, 8))
        plt.hist(data[column], color="purple", edgecolor="black")
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.grid()
        plt.ylabel("Frequency")
        # Save the histogram as a PNG file
        plt.savefig(f"{column}_histogram.png")
        plt.close()  # Close the current figure to free up memory


def save_scatter_plot():
   data = read_with_pandas()
   sns.pairplot(data, hue="species of flowers", palette="Paired")
   plt.legend()
   # Save the scatter plot as a PNG file
   plt.savefig("scatter_plot.png")
   plt.close()


def correlation_matrix():
   data= read_with_pandas()
   columns = data.drop(columns=["species of flowers"])
   corr_mat = columns.corr()
   plt.figure(figsize=(10, 8))
   sns.heatmap(corr_mat, annot=True, cmap="BuPu", fmt=".2f")
   plt.title("Iris dataset correlation matrix")
   plt.savefig("Correlation_matrix.png")
   plt.close()


def main():
   summary_info_results()
   separate_summary_info()
   safe_histogram()
   save_scatter_plot()
   ratio.individual_and_mean_ratios()
   correlation_matrix() 
   print("The project is completed")



if __name__ == "__main__":
    main()

  