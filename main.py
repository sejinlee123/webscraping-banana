"""
main.py
Sejin Lee
6/13/23
"""
import time
import nodes
import bs4
import requests


def shitty_wifi(parent):
    try:
        result = requests.get(parent.url)
    except:
        time.sleep(30)
        result = shitty_wifi(parent)
    return result


def generate_children(parent, node_storage):

    res = shitty_wifi(parent)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    links = soup.find_all("a")
    children = list()
    for link in links:
        url = link.get("href")
        if url is None:
            continue
        # Filter
        first_slice = url[0:3]
        second_slice = url[-1:-5:-1]
        first_filter = {"#", "h", "//", "/w/"}
        second_filter = {")", "gpj.", "GPJ.", ".fdp", ".FDP"}
        third_filter = {"/wiki/Main_Page", "/wiki/Wikipedia", "/wiki/Portal", "/wiki/Special", "/wiki/Help",
                        "/wiki/Talk", "/wiki/Category", "/wiki/Template", "/wiki/File:", "/wiki/List"}
        if any(x in first_slice for x in first_filter):
            pass
        elif any(x in second_slice for x in second_filter):
            pass
        elif any(x in url for x in third_filter):
            pass
        else:
            if not parent.in_blacklist(url):
                fixed_url = "https://en.wikipedia.org" + url
                child = nodes.Node(parent, fixed_url, parent.generation+1, len(nodes.Node.queue))
                nodes.Node.queue.append(child)
                children.append(child.index)
    parent_parent = parent.parent
    parent_parent_index = 0
    if parent_parent is None:
        parent_parent_index = 0
    else:
        parent_parent_index = parent.parent.index
    node_storage.add(parent.url, parent_parent_index, parent.generation, children)


def find_paths_to_article(node_storage, target_url):
    index = 1
    found_generation = 99999
    while True:
        try:
            current_url = node_storage.df["url"].iloc[index]
            current_generation = node_storage.df["generation"].iloc[index]
        except IndexError:
            break
        # print(current_url)
        if found_generation < current_generation:
            break
        if current_url == target_url:
            found_generation = node_storage.df["generation"].iloc[index]
            nodes.Node.found.append(index)
        index += 1


def generate_graph(node_storage):
    index = 1
    max_generation = 11
    while True:
        try:
            current_node = nodes.Node.queue[index]
        except:
            break
        print(f"Queue:{index} QueueLen:{len(nodes.Node.queue)} Max_Gen:{max_generation} "
              f""f"Gen:{current_node.generation} {current_node.url}")
        if max_generation < current_node.generation:
            break
        generate_children(current_node, node_storage)
        index += 1


def main():
    root = nodes.Node(None, "https://en.wikipedia.org/wiki/Banana", 0, 0)
    node_storage = nodes.Storage()
    generate_children(root, node_storage)
    generate_graph(node_storage)
    node_storage.compile()
    node_storage.save()



    """


    node_storage.load()
    user_input = input("Enter target URL LINK: ")
    find_paths_to_article(node_storage, user_input)
    root.display_found(node_storage)
    print(nodes.Node.found)

    

    """

    """
    
    user_input = input("Enter target URL LINK: ")
    find_paths(user_input)
    index = 0
    size = len(nodes.Node.found)
    while index < size:
        nodes.Node.found[index].display_family_tree()
        index += 1
    """


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    res = et - st
    final_res = res / 60
    print('Execution time:', final_res, 'minutes')
