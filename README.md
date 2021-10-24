# SubRedditScraper
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Mandy-cyber/SubRedditScraper?color=%23ff5373&display_name=tag&style=flat-square)  ![GitHub](https://img.shields.io/github/license/Mandy-cyber/SubRedditScraper?color=%23bce1ff&style=flat-square)  ![GitHub repo size](https://img.shields.io/github/repo-size/Mandy-cyber/SubRedditScraper?color=%23ffcbc6&style=flat-square)
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

MODULES | WHAT THEY DO/PROCESS
------------ | -------------
**srtitles** | <ol><li>Navigates to given subreddit</li><li>Scrapes titles of posts</li><li>Scrolls down, and repeats until it reaches the end of the page</li><li>Returns list of all titles found</li><li>_Will eventually put list in a database you can then export._</li></ol>
**srcontent** | Coming soon

<br>

## **USAGE:**
### _srtitles_

```python
from sreddit import srtitles
subRedditName = "name of a subreddit"
showProgress = "Yes" #if you don't want to show progress then you can leave string blank
listOfTitles = srtitles.scrapeMe(subRedditName, showProgess)
print(listOfTitles)
```
<b>N.B -</b> Some subreddits have a lot of pages and it takes time for each page to load for infinite scrolling... Get a cup of tea in the meanwhile <3.




