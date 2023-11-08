import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# file path
df_test = "C:\\Users\\beema\\OneDrive\\T2_BDM 3014 bg\\archive\\test_timeseries\\test_timeseries.csv"
df_train = "C:\\Users\\beema\\OneDrive\\T2_BDM 3014 bg\\archive\\train_timeseries\\train_timeseries.csv"
df_vali = "C:\\Users\\beema\\OneDrive\\T2_BDM 3014 bg\\archive\\validation_timeseries\\validation_timeseries.csv"
df_soil = "C:\\Users\\beema\\OneDrive\\T2_BDM 3014 bg\\archive\\soil_data.csv"

# Load the datasets into pandas DataFrames
df_test = pd.read_csv(df_test)
df_train = pd.read_csv(df_train)
df_vali = pd.read_csv(df_vali)
df_soil = pd.read_csv(df_soil)

# DATA HANDLING
#1 Check for missing values in the datasets
print("Missing values in the Test dataset:")
print(df_test.isnull().sum())

print("Missing values in the Train dataset:")
print(df_train.isnull().sum())

print("Missing values in the Validation dataset:")
print(df_vali.isnull().sum())

print("Missing values in the Soil dataset:")
print(df_soil.isnull().sum())

#2 Handling missing values:
# Drop rows with missing values in the datasets
df_test.dropna(inplace=True)
df_train.dropna(inplace=True)
df_vali.dropna(inplace=True)
df_soil.dropna(inplace=True)

#3. Remove duplicate rows in the datasets
df_test.drop_duplicates(inplace=True)
df_train.drop_duplicates(inplace=True)
df_vali.drop_duplicates(inplace=True)
df_soil.drop_duplicates(inplace=True)

#EDA
# Univariate Analysis
# Histogram of a variable
plt.figure(figsize=(8, 6))
plt.hist(df_train['T2M'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Temperature at 2 Meters')
plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
plt.show()

# Bivariate Analysis
# Scatter plot of two variables
plt.figure(figsize=(8, 6))
sns.scatterplot(x='T2M', y='PRECTOT', data=df_train, color='coral')
plt.title('Scatter Plot of Temperature vs. Precipitation')
plt.xlabel('Temperature (C)')
plt.ylabel('Precipitation (mm day-1)')
plt.show()

# Multivariate Analysis
# Pair plot of selected variables
sns.pairplot(df_train[['T2M', 'WS50M', 'PRECTOT', 'score']])
plt.show()

# Outlier Detection
# Box plot of a variable
plt.figure(figsize=(8, 6))
sns.boxplot(y='WS50M', data=df_train, color='lightgreen')
plt.title('Box Plot of Wind Speed at 50 Meters')
plt.ylabel('Wind Speed (m/s)')
plt.show()

# Feature Engineering
# Creating new features
df_train['T2M_DIFF'] = df_train['T2M_MAX'] - df_train['T2M_MIN']

# Statistical Testing
# Exclude non-numeric columns
numeric_columns = df_train.select_dtypes(include=['float64', 'int64'])

# Correlation matrix
corr_matrix = numeric_columns.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Set the value of rcParams for Agg
mpl.rcParams['agg.path.chunksize'] = 1000
mpl.rcParams['path.simplify_threshold'] = 0.1

# Visualization
# Line plot of a variable over time
df_train['date'] = pd.to_datetime(df_train['date'])
df = df_train.set_index('date')
plt.figure(figsize=(10, 6))
plt.plot(df['T2M'], marker='o', linestyle='-')
plt.title('Temperature at 2 Meters Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.show()
