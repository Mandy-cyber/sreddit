from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sqlite3

class SubRedditScraper():
    """
    A tool for scraping content from a subreddit
    """

    def __init__(self, subreddit: str, keywords: list = None, 
                 show_progress: bool = True, make_db: bool = True, 
                 db_name: str = "subreddit_info.db", scroll_time: int = 1) -> None:
        """
        Initializes a SubRedditScraper.

        Args:
            subreddit: the name of the subreddit to be scraped
            keywords: list of words to look out for in the subreddit
            show_progress: if the progress should be shown in the terminal
            make_db: if a database of the information found should be created
            scroll_time: time to wait between each scroll so page can load
        """
        # general
        self.subreddit = subreddit
        self.show_progress = show_progress
        if keywords == None:
            keywords = []
        self.keywords = keywords

        # database
        self.make_db = make_db
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.setup_database()

        # browser
        self.browser = None
        self.setup_browser()
        self.scroll_time = scroll_time
        self.scroll_height = self.browser.execute_script("return document.body.scrollHeight")

        # misc
        self.titles = set()

    def setup_browser(self) -> None:
        """
        Downloads and configures the browser (webdriver) with default settings
        """
        get_driver = GetChromeDriver() 
        get_driver.install()

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--log-level=3")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.browser = webdriver.Chrome(options=chrome_options)
           
    
    def setup_database(self) -> None:
        """
        Creates a new .db file, if one doesn't already exist, to hold the information 
        found in the subreddit.
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        createTable = """CREATE TABLE IF NOT EXISTS
        srinfo(id INTEGER PRIMARY KEY autoincrement, title TEXT)"""
        self.cursor.execute(createTable)


    def navigate_to_subreddit(self) -> None:
        """
        Navigates to the subreddit if it exists.

        Raises:
            Exception: if the subreddit cannot be found
        """
        assert len(self.subreddit) > 0, "Subreddit name cannot be empty"

        try:
            self.browser.get(f"https://www.reddit.com/r/{self.subreddit}")
        except:
            raise Exception("Subreddit could not be found")


    def scroll_page(self) -> bool:
        """
        Scrolls down the page dynamically after waiting for the page to load

        Returns:
            False: if the end of the subreddit page has been reached
        """
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.scroll_time)

        new_height = self.browser.execute_script("return document.body.scrollHeight")
        old_height = self.scroll_height
        self.scroll_height = new_height
        return new_height == old_height
    

    def find_titles(self):
        """
        Gathers a list of titles of each post on the subreddit.
        """
        self.navigate_to_subreddit()
        use_keywords = len(self.keywords) != 0

        while True:
            raw_titles = self.browser.find_elements(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
            self.titles.update(self.clean_titles(raw_titles, use_keywords))
            end_reached = self.scroll_page()
            if (end_reached):
                break
            else:
                continue
                

    def clean_titles(self, raw_titles: list, use_keywords: bool) -> set():
        """
        Converts each title in the set into their text format, and adds them to the
        clean set if they include keywords (if necessary).

        Args:
            raw_titles: the titles in raw, web-element, format
            use_keywords: whether, or not, keywords are necessary in the titles
        
        Returns:
            cleaned_titles: the text titles with keywords (if necessary)
        """
        cleaned_titles = set()
        title_count = 0

        for raw_title in raw_titles:
            text_title = raw_title.text
            # validate title
            if (len(text_title) > 0 
                and ((use_keywords and any(word in text_title for word in self.keywords))
                    or not use_keywords)):
                cleaned_titles.add(text_title)
                # update progress
                if self.show_progress:
                    title_count +=1 
                    
            # display progress
            print(f"Valid titles Found: {title_count}", end="\r")
        return cleaned_titles


    def add_titles_to_db(self) -> None:
        """
        Adds the given set of titles to the database
        """
        for title in self.titles:
            self.cursor.execute("INSERT INTO {table_name} (title) VALUES(?)"
                                .format(table_name='srinfo'),(title,))
        self.conn.commit()

    
    def find(self) -> None:
        """
        Runs the subreddit scraper to find all the titles on the page. Will later
        change to find other things as well <3
        """
        self.find_titles()
        if self.make_db:
            self.add_titles_to_db()
            print(f"Titles added to {self.db_name}")
        else:
            for title in self.titles:
                print(title + "\n")
        