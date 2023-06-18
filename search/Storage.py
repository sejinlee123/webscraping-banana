"""
Storage.py
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
        self.index = 0
        self.df = pd.DataFrame()

    def compile(self):
        features = ["url", "parents", "generation"]
        values = [self.url, self.parent_index, self.generation]
        # updates the table
        pd.set_option('display.max_columns', 5)
        pd.set_option('display.max_rows', 100)
        self.df = pd.DataFrame(values, index=features).T
        # print(self.df)
        # saves the table

    def save(self):
        # self.df.set_index(["url"], inplace=True)
        # self.df = self.df.assign(url=self.df.index)
        table = pa.Table.from_pandas(self.df)

        pq.write_table(table, 'wiki_storage.parquet')

    def load(self):
        table = pq.read_table('wiki_storage.parquet')
        self.df = table.to_pandas()

    def add(self, url, parents, generation):
        if isinstance(url, str) and (isinstance(parents, set) or (parents is None)) \
                and isinstance(generation, int):
            self.url.append(url)
            self.parent_index.append(parents)
            self.generation.append(generation)
        else:
            print(f"ERROR: url: {url} parent_index: {parents} generation: {generation}")
            raise TypeError


if __name__ == "__main__":
    pass
