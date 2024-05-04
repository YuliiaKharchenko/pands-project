
import csv 

# define the filename fof Iris dataset
filename="iris.csv"
# define the filenames for the output files
results_individual = "Individual_ratios.txt"
results_mean = "Mean_ratios.txt"

# function to read the CSV file (was created on purpose if the possibility will appear to use it)
def read_fileCSV():
    # open the CSV file
    with open(filename, "rt") as irisset:
       try:
          # read the file with csv.reader
          readfile=csv.reader(irisset,delimiter=",")
          firstline=True
          # skip the header(one way)
          for line in readfile: 
            if firstline:
               firstline=False
               continue
           #  print(line)  
       except FileNotFoundError: #the error type 
        print(filename, "does not exist!") # output the message when an error occurs

# function to calculate individual and mean ratios
def individual_and_mean_ratios():
    # create dictionary and list for storing data
    individual_ratios = []
    species_ratios = {}
    try:
        # open files (input and output)
        with open(filename, "rt") as irisset, open(results_individual, "w") as individual, open(results_mean, "w") as mean:
            # read with csv.reader
            readfile = csv.reader(irisset, delimiter=",")
            # skip the header 
            next(readfile)
            # create csv.writer object for individual ratios  
            writer_individual = csv.writer(individual, delimiter="\t")
            # write the header 
            writer_individual.writerow(["Species", " | ", "Petal Length to Width Ratio", " | ", "Sepal Length to Width Ratio", " | "])
            
            # iterate over each line
            for line in readfile:
                # extract data from the line 
                species = line[4]  
                sepal_length = float(line[0]) 
                sepal_width = float(line[1]) 
                petal_length = float(line[2])  
                petal_width = float(line[3])
                
                # calculate ratios 
                petal_ratio = petal_length / petal_width
                sepal_ratio = sepal_length / sepal_width
                # append individual ratios to the list
                individual_ratios.append((species, petal_ratio, sepal_ratio))
                
                # update species ratios dictionary
                if species not in species_ratios:
                    species_ratios[species] = {"petal_ratios": [], "sepal_ratios": []}
                species_ratios[species]["petal_ratios"].append(petal_ratio)
                species_ratios[species]["sepal_ratios"].append(sepal_ratio)
                
                # write to a file the result of individual ratios 
                writer_individual.writerow([species, " | ", "{:.2f}".format(petal_ratio), " | ", "{:.2f}".format(sepal_ratio), " | "])
        

        # calculate and write mean ratios to a file 
        with open(results_mean, "a") as mean:
            mean.write("\n\nMean Ratios:\n")
            for species, ratios in species_ratios.items():
                mean_petal_ratio = sum(ratios["petal_ratios"]) / len(ratios["petal_ratios"])
                mean_sepal_ratio = sum(ratios["sepal_ratios"]) / len(ratios["sepal_ratios"])
                mean.write(f"Species: {species}\n")
                mean.write(f"Mean Petal Length to Width Ratio: {mean_petal_ratio:.2f}\n")
                mean.write(f"Mean Sepal Length to Width Ratio: {mean_sepal_ratio:.2f}\n")
                mean.write("\n")
                
    # error handing for non-exsisting file     
    except FileNotFoundError: 
        print(f"File {filename} does not exist!")
