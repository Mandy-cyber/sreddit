# SubRedditScraper
![GitHub](https://img.shields.io/github/license/Mandy-cyber/SubRedditScraper?color=%23bce1ff&style=flat-square)  ![GitHub repo size](https://img.shields.io/github/repo-size/Mandy-cyber/SubRedditScraper?color=%23ffcbc6&style=flat-square)
#### *Python package for scraping user-inputted subreddits*
---
## **INSTALLATION**
To install:
[Download PyPi Package](https://pypi.org/project/sreddit/#files) , or <br>
```$
$ pip install sreddit
```
To upgrade:
```$
$ pip install sreddit --upgrade
```
<br>

## **MODULES**

MODULES | WHAT THEY DO
------------ | -------------
**srtitles** | <ul><li>Takes user input as a subreddit name Navigates to subreddit</li><li>Loads the entire page (since reddit uses infinte scrolling)</li><li>Scrapes titles of posts and returns them in a list</li><li>_Will eventually add option to put list in a database you can then export._</li></ul>
**srcontent** | Coming soon

<br>

## **USAGE:**
### _srtitles_

```python
from sreddit import srtitles
subRedditName = "name of a subreddit"
listOfTitles = srtitles.scrapeMe(subRedditName)
print(listOfTitles)
```
<b>N.B -</b> Some subreddits have a lot of pages and it takes time for each page to load for infinite scrolling... Get a cup of tea in the meanwhile <3.




