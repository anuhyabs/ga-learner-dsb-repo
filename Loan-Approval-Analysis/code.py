# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
df = pd.DataFrame(bank)
categorical_var = df.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = df.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here
banks = bank
banks.drop(['Loan_ID'],inplace = True,axis=1)
print(banks.info())
print(banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)
banks['Gender'] = banks['Gender'].fillna(banks['Gender'].mode()[0])
banks['Married'] = banks['Married'].fillna(banks['Married'].mode()[0])
banks['Dependents'] = banks['Dependents'].fillna(banks['Dependents'].mode()[0])
banks['Self_Employed'] = banks['Self_Employed'].fillna(banks['Self_Employed'].mode()[0])
banks['LoanAmount'] = banks['LoanAmount'].fillna(banks['LoanAmount'].mode()[0])
banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].fillna(banks['Loan_Amount_Term'].mode()[0])
banks['Credit_History'] = banks['Credit_History'].fillna(banks['Credit_History'].mode()[0])
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'], values='LoanAmount', aggfunc = 'mean')

print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status' ]=='Y')]
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status' ]=='Y')]
percentage_se = (loan_approved_se['Loan_Status'].count()/banks['Loan_Status'].count())*100
percentage_nse = (loan_approved_nse['Loan_Status'].count()/banks['Loan_Status'].count())*100
print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here

#print(banks['Loan_Amount_Term'])

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
print(loan_term.count())
big_loan_term = loan_term[loan_term>=25].size
print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
print(loan_groupby)
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


