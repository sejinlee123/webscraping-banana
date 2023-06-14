"""
Node.py
Sejin Lee
6/13/23
"""


class Node:
    blacklist = set()
    base_url = "https://en.wikipedia.org/wiki/Toy"
    queue = list()
    found = list()

    def __init__(self, parent, url, generation):
        self.url = url
        self.parent = parent
        self.generation = generation

    def __str__(self):
        return self.url

    def create_children(self, parent, url):
        link = "https://en.wikipedia.org" + url
        self.queue.append(Node(parent, link, self.generation+1))

    def in_blacklist(self, url) -> bool:
        if url in self.blacklist:
            return True
        else:
            self.blacklist.add(url)
            return False

    def display_family_tree_inner(self):
        print(self.url)
        if self.parent is not None:
            self.parent.display_family_tree_inner()

    def display_family_tree(self):
        print("Family Tree")
        if self.parent.url != self.base_url:
            print(self.url)
            self.parent.display_family_tree_inner()


if __name__ == "__main__":
    pass
