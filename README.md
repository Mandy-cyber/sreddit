# SREDDIT
> **A simple tool for scraping information from subreddits.**

<div id="skills-icons" align="left">
  <a target="_blank" href="#"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/></a>
  <a target="_blank" href="#"><img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/></a>
</div>



<br>

## **Installation**
To *install*, you can either [Download the Pypi Package](https://pypi.org/project/sreddit/#files) or,
```python
pip install sreddit
```

<br>

To *upgrade* to the latest version,
```python
pip install --upgrade sreddit
```

<br>


## **Usage**
### **srtitles**
Gets all unique titles from a subreddit.

```python
from sreddit import SubRedditTitles

scraper = SubRedditTitles(subreddit="subreddit_name")
scraper.run()
```


### **srbodies**
Gets all unique post bodies (i.e. descriptions) from a subreddit.

```python
from sreddit import SubRedditBodies

scraper = SubRedditBodies(subreddit="subreddit_name")
scraper.run()
```

<br>

### **Optional Arguments**

<br>

| **Argument**          | **What it Does**                                                                       |
|-----------------------|----------------------------------------------------------------------------------------|
| keywords              | Only includes content that has one or more of these keywords                           |
| show_progess          | Whether or not to show scraping progress (i.e. number of titles found) in the terminal |
| make_db               | If a database of the content found should be created after scraping                    |
| db_name               | The name of the database to be created--must end in .db                                |
| scroll_time           | Time to wait between scrolling down the page and finding elements.                     |


<br>

## **FAQs**



