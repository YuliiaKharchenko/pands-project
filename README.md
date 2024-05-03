# The Project on the module "Programming and scripting" 

#### **Analysis of the Iris flower dataset using Python**



This repository contains an analysis of the Iris flower dataset used by the famous British statistician and biologist [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) to demonstrate the method of linear discriminant analysis in 1936. The data set was collected by botanist [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson). 

#### **Key Objectives**:

1. **Data Summary**: The program outputs a comprehensive summary of each variable in the dataset to a single text file. This summary includes general characteristics of variables, checking for missing values, and counting the number of flowers of each species.
2. **Histogram Generation**: Histograms of each variable are saved as PNG files. Histograms provide insights into the distribution of values for each feature and help identify patterns and outliers.
3. **Scatter Plot Creation**: The program generates scatter plots of each pair of variables. Scatter plots visualize the relationship between two variables and can reveal correlations or patterns in the data.
4. **Additional Analysis**: The program conducts any other pertinent analysis necessary for gaining deeper insights into the dataset. This includes calculating individual and mean ratios of length-to-width variables, generating a correlation matrix, and saving it to a separate file.


[WikipediA's](https://en.wikipedia.org/wiki/Iris_flower_data_set) description of the dataset.


Downloaded from this resource-[Fisher's Iris data](https://archive.ics.uci.edu/dataset/53/iris).


#### Components of the dataset:

- sepal length in cm
- sepal width in cm
- petal length in cm
- petal width in cm
- species of Flowers(setosa,versicolor, virginica)

#### Overview of the Iris dataset: 

1. There are 150 rows.
3. Each row has a row index with values ranging from 0 to 149.
4. The table has 5 columns. all the columns have a value for each of the rows (all 150 values are non-null). 
5. The columns sepal length in cm, sepal width in cm,  petal length in cm, petal width in cm contain float type data (float64). The column species of flowers contains string type data (object).


#### Data analysis Python libraries required: 

 - Pandas - to read, manipulate, calculate data, review data types 
 - Numpy - to calculate data
 - Matplotlib.pyplot - to create plots 
 - Seaborn - to visualise rezults of analysis 
 - CSV - to read, write, and process data from CSV files


#### Get started

1. Clone the repository to your local machine:

'''git clone <repository_url>'''

2. Navigate to the project directory:

'''cd <project_directory>'''

3. Install the required dependencies. You can install them using pip:

'''pip install pandas numpy matplotlib seaborn'''

4. Once the dependencies are installed, you can run the program by executing the analysis.py script:

'''python analysis.py'''

The program will generate summary information about the dataset, histograms for each variable, scatter plots for pairs of variables, and additional analysis such as individual and mean ratios, and a correlation matrix.
Explore the generated files and outputs to gain insights into the dataset. You can further customize the analysis according to your requirements by modifying the analysis.py script.

#### Author

This project was created by **Yuliia Kharchenko**. 


*** 

#### References: 
* [Pandas. User guide.](https://pandas.pydata.org/docs/user_guide/index.html)
* [NumPy fundamentals](https://numpy.org/doc/stable/user/basics.html)
* [Matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
* [Seaborn: statistical data visualization](https://seaborn.pydata.org/#seaborn-statistical-data-visualization)
* [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
* [Reading and Writing CSV Files in Python_Real_Python](https://realpython.com/python-csv/)
* [Exploratory Data Analysis on Iris Dataset on www.geeksforgeeks.org](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)
* [Exploratory Data Analysis on Iris Dataset](https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset)
* [Iris Flower Data Set on www.devx.com](https://www.devx.com/terms/iris-flower-data-set/)