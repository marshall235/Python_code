#!/usr/bin/python3
import statsmodels.api as sm
import sys
import pandas as pd

def main():
    #Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python fastfood.py <path_to_csv>")
        sys.exit(1)

    #Get the path from the command line argument
    #file_path = sys.argv[1]
    file_path = 'fastfood.csv'

    #Load the csv file 
    df = pd.read_csv(file_path)
    
    #Define the independent variables and add a constant
    x = df[['total_fat', 'sat_fat', 'cholesterol', 'sodium']]
    x = sm.add_constant(x)

    #Define the dependent variable
    y = df['calories']

    #Perform the regression
    model = sm.OLS(y, x).fit()

    #Print the results to two deciml places
    print("MSE:")
    print(model.mse_total.round(2))
    print("\nRsquared Value:")
    print(model.rsquared.round(2))
    print("\nParameters:")
    print(model.params.round(2))
    print("\nPvalues:")
    print(model.pvalues.round(2))

if __name__ == "__main__":
    main()
