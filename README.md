# SubRedditScraper
## *Python package for scraping user-inputted subreddits*

### **Installation**

[Download PyPi Package](https://pypi.org/project/srtitles/#files) , or
```pip install srtitles```
<br><br>

### **Modules**

MODULES | WHAT THEY DO
------------ | -------------
**srtitles** | <ul><li>Takes user input as a subreddit name Navigates to subreddit</li><li>Loads the entire page (since reddit uses infinte scrolling)</li><li>Scrapes titles of posts and returns them in a list</li><li>_Will eventually put list in a database you can then export._</li></ul>
**srcontent** | Coming soon

<br><br>

### **HOW TO USE:**
### _srtitles_

```python
from sreddit import srtitles
subRedditName = "name of a subreddit"
listOfTitles = srtitles.scrapeMe(subRedditName)
print(listOfTitles)
```
###### N.B <ul><li>chromdriver.exe is required to run modules</li><li>Some subreddits have a lot of pages and it takes time for each page to load for infinite scrolling... Get a cup of tea in the meanwhile <3</li></ul>




