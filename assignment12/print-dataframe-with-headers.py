#Task 5: Extending a Class

import pandas as pd

#Create a class called DFPlus
#Inherit from the Pandas DataFrame class
class DFPlus(pd.DataFrame):

    # This allows pandas to preserve the DFPlus type when performing operations
    @property
    def _constructor(self):
        return DFPlus

    # Class method to create a DFPlus object from a CSV file
    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    #Within the DFPlus class, declare a function called print_with_headers()
    #Only takes one argument, self
    def print_with_headers(self):
        #Know the length of the DataFrame
        total_rows = len(self)  

        #Provide a way to print the DataFrame giving column headers every 10 lines
        #The function will print the whole DataFrame in a loop, printing 10 rows at a time
        for start in range(0, total_rows, 10):
            end = start + 10
            #Specify the ten line slice you want
            chunk = super().iloc[start:end] 
            #Print what you get back, looping until you get to the bottom
            print(chunk.to_string(index=True))
            #Extra line for easier reading
            print()

if __name__ == "__main__":
    #Create a DFPlus instance by reading in ../csv/products.csv
    dfp = DFPlus.from_csv("../csv/products.csv")

    #Use the print_with_headers() method of your DFPlus instance to print the DataFrame
    dfp.print_with_headers()
