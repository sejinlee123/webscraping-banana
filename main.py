"""
main.py
Sejin Lee
6/13/23
"""
import nodes
import bs4
import requests


def generate_children(parent):
    res = requests.get(parent.url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    links = soup.find_all("a")
    f = open("raw_data.txt", "w+", encoding="utf-8")
    for link in links:
        url = link.get("href")
        if url is None:
            continue
        first_slice = url[0:3]
        second_slice = url[-1:-5:-1]
        first_filter = set(["#", "h", "//", "/w/"])
        second_filter = set([")", "gpj.", ".GPJ"])
        third_filter = set(["/wiki/Main_Page", "/wiki/Wikipedia", "/wiki/Portal", "/wiki/Special", "/wiki/Help",
                        "/wiki/Talk", "/wiki/Category", "/wiki/Template", "/wiki/File:", "/wiki/List"])
        if any(x in first_slice for x in first_filter):
            pass
        elif any(x in second_slice for x in second_filter):
            pass
        elif any(x in url for x in third_filter):
            pass
        else:
            if not parent.in_blacklist(url):
                parent.create_children(parent, url)
                f.write(str(url)+"\n")
    f.close()


def find_paths(user_input):
    index = 1
    found_generation = 9999
    while True:
        try:
            current_node = nodes.Node.queue[index]
        except:
            break

        print(f"Queue:{index} QueueLen:{len(nodes.Node.queue)} found:{found_generation} Gen:{current_node.generation} {current_node.url}")
        if found_generation < current_node.generation:
            break
        if user_input == current_node.url:
            found_generation = current_node.generation
            nodes.Node.found.append(current_node)
            # current_node.display_family_tree(user_input)
        if found_generation == current_node.generation:
            index += 1
            continue
        generate_children(current_node)
        index += 1


def main():
    aNode = nodes.Node(None, "https://en.wikipedia.org/wiki/Toy", 0)
    generate_children(aNode)
    user_input = input("Enter target URL LINK: ")
    find_paths(user_input)
    index = 0
    size = len(nodes.Node.found)
    while index < size:
        nodes.Node.found[index].display_family_tree()
        index += 1


if __name__ == "__main__":
    main()
