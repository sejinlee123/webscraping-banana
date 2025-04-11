"""
main.py
Sejin Lee
6/13/23
"""
import time
import search


def main():

    a_search = search.Search("https://en.wikipedia.org/wiki/Miniature_wargaming")
    a_search.generate_data_base(6)
    a_search.storage.compile()
    a_search.storage.save()
    quit()



    # user_input = input("Enter target URL LINK: ")
    a_search = search.Search("https://en.wikipedia.org/wiki/Tundra")
    a_search.storage.load()
    a_search.display()

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    res = et - st
    final_res = res / 60
    print('Execution time:', final_res, 'minutes')
