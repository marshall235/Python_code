#!/usr/bin/python3
import sys
import pandas as pd
import statsmodels.api as sm

#Load the csv file i
#filename = sys.argv[1]
file_name = 'german_credit_data.csv'
data = pd.read_csv(filename)

#Rename the 'Credit amount' to 'credit_amount'
data = data.rename(columns={'Credit amount': 'Credit_amount'})

#Prepare the data for regression 
x = data[['Age', 'Duration']]
x = sm.add_constant(x) # Add a constant
y = data['Credit_amount']

#Run the regression 
model = sm.OLS(y,x).fit()

#Print the parameters and R-Squared
print("Model Parameters:")
print(model.params.round(2))
print("\nRsquared Value:")
print(model.rsquared.round(2))
