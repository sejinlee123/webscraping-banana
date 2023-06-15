"""
node.py
Sejin Lee
6/13/23
"""


class Node:
    blacklist = set()
    base_url = "https://en.wikipedia.org/wiki/Toy"
    queue = list()
    found = list()

    def __init__(self, parent, url, generation, index):
        self.url = url
        self.parent = parent
        self.generation = generation
        self.index = index

    def __str__(self):
        return self.url

    def in_blacklist(self, url) -> bool:
        if url in self.blacklist:
            return True
        else:
            self.blacklist.add(url)
            return False

    def display_found(self, node_storage):

        for index in self.found:
            # print(f"Current_Index: {current_index} Parent_Index: {parent_index}")
            print("Path: ")
            current_index = index
            while current_index != 0:
                url = node_storage.df["url"].iloc[current_index]
                print(url)
                current_index = node_storage.df["parent_index"].iloc[current_index]
            root_url = node_storage.df["url"].iloc[0]
            print(root_url)



if __name__ == "__main__":
    pass
