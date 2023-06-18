import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000000)
table2= pq.read_table('wiki_storage.parquet')
table2 = table2.to_pandas()


df = table2

print(df.head(1000))




"""
df = pd.DataFrame(
  {
    'url' : ['org1', 'org2', 'org3'],
    'parent_index' : [2, 3, 4],
    'generation' : [1, 2, 3],
    'children' : [[13, 12], [15, 68], [90, 101]]
  }
)
"""
"""
table = pa.Table.from_pandas(df)

pq.write_table(table, 'example.parquet')

# Load the table from the Parquet file
table2= pq.read_table('example.parquet')
table2 = table2.to_pandas()

print(df)

# grabs a row
row_iloc = df.iloc[1]
print(row_iloc)

# grabs a cell: [row, colum] starting from index zero
row_iloc = df.iloc[1,0]
print(row_iloc)

# Goes to column url, row 0
print(df["url"].iloc[0])

# nested list
print(df["children"].iloc[0][0])

"""

# adding an element
"""

url = ['org1', 'org2', 'org3']
parent_index = [2, 3, 4]
generation = [1, 2, 3]
children = [[13, 12], [15, 68], [90, 101]]

features = ["url", "parent_index", "generation", "children"]
values = [url, parent_index, generation, children]
df = pd.DataFrame(values, index=features).T

print(df)
print(df.iloc[0][3])
"""


