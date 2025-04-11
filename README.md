# webscraping-banana

This project uses the **C++ Requests** library to perform web scraping.

## Structure

- `main.py`: Entry point that accesses the classes inside the `search/` folder.

### `search/` Folder:

- **Class `Storage`**  
  Acts as the "black box" between `main.py` and the web scraper along with the storage solution pyarrow.

- **Class `Search`**  
  Responsible for scraping, filtering inputs, and storing results.

- **Class `Node`**  
  Handles the structure of the resulting data and manages blacklists to avoid duplicates.
#Note that the main bottleneck is the rate limiting of Wikipedia which is around a second on average.
