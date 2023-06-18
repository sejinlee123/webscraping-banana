"""
Node.py
Sejin Lee
6/13/23
"""


class Node:
    parent_blacklist = {}
    parent_blacklist_buffer = {}
    child_blacklist = {}
    queue = list()
    found = list()

    def __init__(self, url, parents, generation, index):
        self.url = url
        self.parents = parents
        self.generation = generation
        self.index = index

    def __str__(self):
        return self.url

    def in_parent_blacklist(self, url) -> bool:
        if url in self.parent_blacklist:
            return True
        else:
            self.parent_blacklist_buffer[url] = 0
            return False

    def in_child_blacklist(self, url, child_index) -> bool:
        if url in self.child_blacklist:
            return True
        else:
            self.child_blacklist[url] = child_index
            return False

    def update_parent_blacklist(self):
        self.parent_blacklist = self.parent_blacklist_buffer | self.parent_blacklist
        self.parent_blacklist_buffer = {}


if __name__ == "__main__":
    pass
