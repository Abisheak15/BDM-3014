import pandas as pd

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

# Display basic information about the datasets
print("Test Dataset Information:")
print("Number of rows and columns:", df_test.shape)
print("\nColumns in the Test dataset:")
print(df_test.columns)
print("\nData types of columns:")
print(df_test.dtypes)
print("\nSummary statistics:")
print(df_test.describe())
print("\nPreview of the Test dataset:")
print(df_test.head())

print("Train Dataset Information:")
print("Number of rows and columns:", df_train.shape)
print("\nColumns in the Train dataset:")
print(df_train.columns)
print("\nData types of columns:")
print(df_train.dtypes)
print("\nSummary statistics:")
print(df_train.describe())
print("\nPreview of the Train dataset:")
print(df_train.head())

print("Validation Dataset Information:")
print("Number of rows and columns:", df_vali.shape)
print("\nColumns in the Validation dataset:")
print(df_vali.columns)
print("\nData types of columns:")
print(df_vali.dtypes)
print("\nSummary statistics:")
print(df_vali.describe())
print("\nPreview of the Validation dataset:")
print(df_vali.head())

print("Soil Dataset Information:")
print("Number of rows and columns:", df_soil.shape)
print("\nColumns in the Soil dataset:")
print(df_soil.columns)
print("\nData types of columns:")
print(df_soil.dtypes)
print("\nSummary statistics:")
print(df_soil.describe())
print("\nPreview of the Soil dataset:")
print(df_soil.head())

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

# Display basic information about the datasets After Data Handling
print("Test Dataset Information After Data Handling:")
print("Number of rows and columns:", df_test.shape)
print("\nColumns in the Test dataset:")
print(df_test.columns)
print("\nData types of columns:")
print(df_test.dtypes)
print("\nSummary statistics:")
print(df_test.describe())
print("\nPreview of the Test dataset:")
print(df_test.head())

print("Train Dataset Information After Data Handling:")
print("Number of rows and columns:", df_train.shape)
print("\nColumns in the Train dataset:")
print(df_train.columns)
print("\nData types of columns:")
print(df_train.dtypes)
print("\nSummary statistics:")
print(df_train.describe())
print("\nPreview of the Train dataset:")
print(df_train.head())

print("vali Dataset Information After Data Handling:")
print("Number of rows and columns:", df_vali.shape)
print("\nColumns in the vali dataset:")
print(df_vali.columns)
print("\nData types of columns:")
print(df_vali.dtypes)
print("\nSummary statistics:")
print(df_vali.describe())
print("\nPreview of the vali dataset:")
print(df_vali.head())

print("soil Dataset Information After Data Handling:")
print("Number of rows and columns:", df_soil.shape)
print("\nColumns in the soil dataset:")
print(df_soil.columns)
print("\nData types of columns:")
print(df_soil.dtypes)
print("\nSummary statistics:")
print(df_soil.describe())
print("\nPreview of the soil dataset:")
print(df_soil.head())

