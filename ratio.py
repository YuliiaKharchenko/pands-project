
import csv 

filename="iris.csv"
results_individual = "Individual_ratios.txt"
results_mean = "Mean_ratios.txt"

def read_fileCSV():
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


def individual_and_mean_ratios():
    individual_ratios = []
    species_ratios = {}
    try:
        with open(filename, "rt") as irisset, open(results_individual, "w") as individual, open(results_mean, "w") as mean:
            readfile = csv.reader(irisset, delimiter=",")
            next(readfile)
            writer_individual = csv.writer(individual, delimiter="\t")
            writer_individual.writerow(["Species", " | ", "Petal Length to Width Ratio", " | ", "Sepal Length to Width Ratio", " | "])
            
            for line in readfile:
                species = line[4]  
                sepal_length = float(line[0]) 
                sepal_width = float(line[1]) 
                petal_length = float(line[2])  
                petal_width = float(line[3])
                
                petal_ratio = petal_length / petal_width
                sepal_ratio = sepal_length / sepal_width
                
                individual_ratios.append((species, petal_ratio, sepal_ratio))
                
                if species not in species_ratios:
                    species_ratios[species] = {"petal_ratios": [], "sepal_ratios": []}
                species_ratios[species]["petal_ratios"].append(petal_ratio)
                species_ratios[species]["sepal_ratios"].append(sepal_ratio)
                
                writer_individual.writerow([species, " | ", "{:.2f}".format(petal_ratio), " | ", "{:.2f}".format(sepal_ratio), " | "])
        
        with open(results_mean, "a") as mean:
            mean.write("\n\nMean Ratios:\n")
            for species, ratios in species_ratios.items():
                mean_petal_ratio = sum(ratios["petal_ratios"]) / len(ratios["petal_ratios"])
                mean_sepal_ratio = sum(ratios["sepal_ratios"]) / len(ratios["sepal_ratios"])
                mean.write(f"Species: {species}\n")
                mean.write(f"Mean Petal Length to Width Ratio: {mean_petal_ratio:.2f}\n")
                mean.write(f"Mean Sepal Length to Width Ratio: {mean_sepal_ratio:.2f}\n")
                mean.write("\n")
        
    except FileNotFoundError: 
        print(f"File {filename} does not exist!")
