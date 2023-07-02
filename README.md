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

MODULES | WHAT THEY DO
------------ | -------------
**srtitles** | Gets a list of all the unique titles in the subreddit.
**srcontent** | Coming soon

<br>

## **USAGE:**
### _srtitles_

```python
scraper = SubRedditScraper("beans")
scraper.find()
```
<b>N.B -</b> Some subreddits have a lot of pages and it takes time for each page to load for infinite scrolling... Get a cup of tea in the meanwhile <3.




