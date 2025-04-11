"""
Search.py
Sejin Lee
6-17-23
"""
from . import Storage
from . import Node
import bs4
import requests
import time

class Search:
    root_url = "https://en.wikipedia.org/wiki/Banana"
    filter_one = {"#", "h", "//", "/w/", ")", "gpj.", "GPJ.", ".fdp", ".FDP"}
    filter_two = {"/wiki/Main_Page", "/wiki/Wikipedia", "/wiki/Portal", "/wiki/Special", "/wiki/Help",
                  "/wiki/Talk", "/wiki/Category", "/wiki/Template", "/wiki/File:", "/wiki/List", "ftp:", "ftp."}

    def __init__(self, target_url):
        self.target_url = target_url
        self.storage = Storage()
        self.root = Node(self.root_url, None, 0, 0)

    def generate_data_base(self, max_gen=1):
        self.generate_children(self.root)
        index = 1
        current_gen = 0
        st = time.time()
        while True:
            try:
                current_node = Node.queue[index]
            except IndexError:
                break
            et = time.time()
            res = et - st
            final_res = res / 60
            print(f"Queue:{index} QueueLen:{len(Node.queue)} Max_Gen:{max_gen} Time:{final_res}"
                  f""f"Gen:{current_node.generation} {current_node.url}")
            if current_gen < current_node.generation:
                self.root.update_parent_blacklist()
            current_gen = current_node.generation
            if max_gen < current_gen:
                break
            self.generate_children(current_node, max_gen == current_node.generation)
            index += 1

    def buffer(self, link):
        try:
            result = requests.get(link)
            return result
        except:
            pass
        try:
            result = requests.get(link)
        except:
            user_input = input(f"Skip {link} (Y/N): ")
            if isinstance(user_input, str):
                if user_input == 'y' or user_input == 'Y':
                    return None
                elif user_input == 'n' or 'N':
                    return self.buffer(link)
            else:
                print("Incorrect Input")
                return self.buffer(link)
        return result

    def generate_children(self, parent, generation_flag=False):
        if generation_flag:
            self.storage.add(parent.url, parent.parents, parent.generation)
            return
        res = self.buffer(parent.url)
        if res is None:
            return
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        links = soup.find_all("a")
        if links is None:
            return
        for link in links:
            url = link.get("href")
            if url is None:
                continue

            url_slices = [url[0:1], url[0:2], url[0:3], url[-1], url[-1:-5:-1]]

            if any(x in self.filter_one for x in url_slices):
                pass
            elif any(x in url for x in self.filter_two):
                pass
            else:
                if self.root.in_parent_blacklist(url):
                    continue
                elif self.root.in_child_blacklist(url, len(Node.queue)):
                    index = self.root.child_blacklist[url]
                    child = Node.queue[index]
                    child.parents.add(parent.index)

                else:
                    fixed_url = "https://en.wikipedia.org" + url
                    child = Node(fixed_url, {parent.index}, parent.generation + 1, len(Node.queue))
                    Node.queue.append(child)
        self.storage.add(parent.url, parent.parents, parent.generation)

    def display(self):
        df = self.storage.df
        stack = list()
        starting_df = df.loc[df['url'] == self.target_url]  # Finds target URL series
        max_gen = df.iloc[starting_df.index[0]]["generation"]
        stack.append(starting_df.index[0])
        while len(stack) != 0:
            # Take off and proces top of stack
            current_index = stack.pop()
            url = df.iloc[current_index]["url"]
            gen_number = df.iloc[current_index]["generation"]
            print("\t"*(max_gen - gen_number), end="")
            print(f"Gen #{gen_number} URL: {url}")
            # Find neighbors
            temp_series = df.iloc[current_index]["parents"]
            # Add to stack
            if temp_series is None:
                continue
            else:
                for index in temp_series:
                    stack.append(index)


if __name__ == "__main__":
    pass

"""
  def generate_children(self, parent, generation_flag=False):
        if generation_flag:
            self.storage.add(parent.url, parent.parents, parent.generation)
            return
        res = self.buffer(parent.url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        links = soup.find_all("a")
        for link in links:
            url = link.get("href")
            if url is None:
                continue

            url_slices = [url[0:1], url[0:2], url[0:3], url[-1], url[-1:-5:-1]]
            filter_one = {"#", "h", "//", "/w/", ")", "gpj.", "GPJ.", ".fdp", ".FDP"}
            filter_two = {"/wiki/Main_Page", "/wiki/Wikipedia", "/wiki/Portal", "/wiki/Special", "/wiki/Help",
                          "/wiki/Talk", "/wiki/Category", "/wiki/Template", "/wiki/File:", "/wiki/List"}
            if any(x in filter_one for x in url_slices):
                pass
            elif any(x in url for x in filter_two):
                pass
            else:
                if self.root.in_parent_blacklist(url):
                    continue
                elif self.root.in_child_blacklist(url, len(Node.queue)):
                    index = self.root.child_blacklist[url]
                    child = Node.queue[index]
                    child.parents.add(parent.index)

                else:
                    fixed_url = "https://en.wikipedia.org" + url
                    child = Node(fixed_url, {parent.index}, parent.generation + 1, len(Node.queue))
                    Node.queue.append(child)
        self.storage.add(parent.url, parent.parents, parent.generation)
"""