import pandas as pd


df = pd.read_parquet('wiki_storage.parquet', engine='pyarrow')  # Or engine='fastparquet'
df['parents'] = df['parents'].apply(lambda x: "{" + ",".join(map(str, x)) + "}" if x is not None else "{}")
#print(df.loc[500])
# Convert to CSV
df.to_csv('3_Deg_of_Bana.csv')  # Set index=False to exclude row numbers