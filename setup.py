from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = 'Web scraper for subreddits'

# Setting up
setup(
    name="sreddit",
    version=VERSION,
    author="Mandy-cyber",
    author_email="",
    description=DESCRIPTION,
    packages=find_packages(),
    url="https://github.com/Mandy-cyber/sreddit",
    install_requires=['selenium', 'get_chrome_driver', 'pysqlite3'],
    keywords=['python', 'selenium', 'reddit', 'subreddit'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)