import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Grades.csv')

#571 rows
print(data)
#ensuring that CGPA column contains only numeric values
data['CGPA'] = pd.to_numeric(data['CGPA'], errors='coerce')
#removing rows that contain missing values
data.dropna(inplace=True)
#417 rows
print(data)


#the average value 
mean_cgpa = data['CGPA'].mean()
print(f'Mean grade: {mean_cgpa}')

#standard deviation
std_cgpa = data['CGPA'].std()
print(f'Standard deviation of grades: {std_cgpa}')

#histogram of cgpa scores
plt.hist(data['CGPA'], bins=10, color='green', alpha=0.5)
plt.title('Distribution of CGPA')
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.show()
