"""
storage.py
Sejin Lee
6/14/23
"""
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd


class Storage:

    def __init__(self):
        self.url = []
        self.parent_index = []
        self.generation = []
        self.children = []
        self.index = 0
        self.df = pd.DataFrame()

    def compile(self):
        features = ["url", "parent_index", "generation", "children"]
        values = [self.url, self.parent_index, self.generation, self.children]
        # updates the table
        self.df = pd.DataFrame(values, index=features).T
        # saves the table

    def save(self):
        table = pa.Table.from_pandas(self.df)
        pq.write_table(table, 'wiki_node_storage.parquet')

    def load(self):
        table = pq.read_table('wiki_node_storage.parquet')
        self.df = table.to_pandas()

    def add(self, url, parent_index, generation, children):
        if isinstance(url, str) and isinstance(parent_index, int) \
                and isinstance(generation, int) and isinstance(children, list):
            self.url.append(url)
            self.parent_index.append(parent_index)
            self.generation.append(generation)
            self.children.append(children)
        else:
            print(f"ERROR: url: {url} parent_index: {parent_index} generation: {generation}")
            print(f"children: {children}")
            raise TypeError

    def display(self):
        for i in range(100):
            url = self.df["url"].iloc[i]
            parent_index = self.df["parent_index"].iloc[i]
            generation = self.df["generation"].iloc[i]
            children = self.df["children"].iloc[i]
            print(f"Parent_Index: {parent_index} Gen: {generation}")

if __name__ == "__main__":
    pass
