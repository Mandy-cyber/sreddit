from setuptools import setup, find_packages

setup(
    name="sreddit",
    version='1.0.0',
    author="Mandy-cyber",
    author_email="",
    description='Web scraper for subreddits',
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