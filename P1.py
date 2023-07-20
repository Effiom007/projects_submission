import pandas as pd 
from matplotlib import pyplot as plt 

# create dataframe 

df = pd.read_excel('Unemployment_Data.xlsx', sheet_name='2018-Q1')

# print(df)
# converting to csv 

# csv_data= df.to_csv('Uneployment_Data.csv', index=False) 

# print(csv_data)

# 3. Get the first 10 unemployment rates in Old Nigeria for the first 10 states

# change column name 
print(df.rename(columns = {"Unnamed: 1":"Labour","Unnamed: 2":"Total_Employed","Unnamed: 3":"Full_Time_Hrs","Unnamed: 4":
                           "Part_TimeHrs","Unnamed: 5":"Unemployed_Hrs","Unnamed: 6":"Unemployed_Hrs2","Unnamed: 7":"Total"
                           , "Unnamed: 8":"Part_time","Unnamed: 9":"Rates%","Unnamed: 10": "Rates","Unnamed: 11":"New Naija",
                           "Unnamed: 12":"Inter_national","Unnamed: 13":"Underemployment"}, inplace=True))
                          
# getting first unemployment rates in Old Nigeria

# Rates = df["Rates"].head(12)
# print(Rates)

#4.Get the first 10 underemployment rates for the first 10 states
# Rates = df["Underemployment"].head(12)
# print(Rates)

# 5.plot the unemployment rate against underemployment rate ( from 3 and 4)


Rates = df.loc[len(df)-39:39,['Rates']]
Underemployment = df.loc[len(df)-39:39,['Underemployment']]
print(Underemployment)

plt.plot(Rates,Underemployment, label= "Rates vs Underemployment", color="coral")
plt.title("Relationship between Unemployment Rates and Underemployment Rates")
plt.ylabel("Rates")
plt.xlabel("Underemployment")
plt.legend(["Rates vs Underemployment"])
graph = plt.show()
print(graph)


pdf = open('P1.pdf', 'w')
samp = open('p1.pdf', 'r')
samp.read(graph)
pdf.write(str(df))
pdf.write(str(plt))
pdf.write(str(graph))
pdf.close()






 

