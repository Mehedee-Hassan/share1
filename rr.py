import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample DataFrames
data1 = {
    'id': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'value': [10, 20, 15, 10, 30, 25, 10, 20]
}

data2 = {
    'id': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'value': [12, 22, 10, 15, 25, 30, 5, 18]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Calculate the differences
df_merged = df1.merge(df2, on='id', suffixes=('_set1', '_set2'))
df_merged['difference'] = df_merged['value_set1'] - df_merged['value_set2']

# Define bins programmatically based on data range
min_diff = df_merged['difference'].min()
max_diff = df_merged['difference'].max()
num_bins = 7  # Number of bins you want
bins = np.linspace(min_diff, max_diff, num_bins + 1)

# Bucket the differences
df_merged['bucket'] = pd.cut(df_merged['difference'], bins=bins, right=False)

# Count the number of IDs in each bucket
bucket_counts = df_merged['bucket'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(bucket_counts.index.astype(str), bucket_counts.values, color='skyblue')
plt.xlabel('Difference Buckets')
plt.ylabel('Count of IDs')
plt.title('Count of IDs per Difference Bucket')
plt.xticks(rotation=45)
plt.show()
