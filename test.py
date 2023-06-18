

import bs4
import requests
import search

def algo1():
    url = "https://en.wikipedia.org/wiki/Poppy_seed_defence"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    links = soup.find_all("a")
    my_file = open("fixed_data.txt", "w+")
    for link in links:
        url = link.get("href")
        first_slice = url[0:3]
        second_slice = url [-1:-5:-1]
        first_filter = ["#", "h", "//", "/w/"]
        second_filter = [")", "gpj."]
        third_filter = ["/wiki/Main_Page", "/wiki/Wikipedia", "/wiki/Portal", "/wiki/Special"
                        , "/wiki/Help", "/wiki/Talk", "/wiki/Category"]
        if any(x in first_slice for x in first_filter):
            pass
        elif any(x in second_slice for x in second_filter):
            pass
        elif any(x in url for x in third_filter):
            pass
        else:
            print(url)
            # my_file.write(link.get("href") + "\n")

    my_file.close()


def algo2():
    if "https://en.wikipedia.org/wiki/United_States_Department_of_Health_and_Human_Services" \
            == "https://en.wikipedia.org/wiki/United_States_Department_of_Health_and_Human_Services":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    a_search = search.Search("https://en.wikipedia.org/wiki/Miniature_wargaming")

