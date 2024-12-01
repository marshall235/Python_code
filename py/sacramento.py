#!/usr/bin/python3
import pandas as pd
import statsmodels.api as sm
import sys

#Load the file from the command line
#file_name = sys.argv[1]
file_name = 'sacramento.csv'
data = pd.read_csv(file_name)

#Create the binary variable for bathrooms
data['bath_binary'] = data['baths'].apply(lambda x: 0 if x == 1 else 1)

#Prepare the data for regression 
x = data[['beds', 'sqft', 'price']]
x = sm.add_constant(x) #Add constant
y = data ['bath_binary']

#Run the logistic regression 
mod = sm.Logit(y, x).fit()

#Print the result parameters
print("Regression Parameters:")
print(mod.params.round(2))

print("\nP-values:")
print(mod.pvalues.round(2))

#Identify the smallets p-value
smallest_pvalue_var = mod.pvalues.idxmin()
print(f'\nThe smallest p-value is for {smallest_pvalue_var}')
