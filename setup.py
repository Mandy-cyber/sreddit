from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Web scraper for subreddits'
LONG_DESCRIPTION = 'A simple way to scrape titles, body text, and more from posts on subreddits'

# Setting up
setup(
    name="sreddit",
    version=VERSION,
    author="Mandy-cyber",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium', 'get_chrome_driver', 'pysqlite3'],
    keywords=['python', 'selenium', 'reddit', 'subreddit'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)