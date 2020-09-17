# leaerning-beautifulsoup
Learning BeautifulSoup

Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/


### Setup

Setup the environment:

`python3 -m venv .venv`

OSX / Linux:
`source .venv/bin/activate`

Windows:

`\.venv\Scripts\activate.bat`

Install dependencies:

`pip install -r requirements.txt`

## test

`pytest`



- I need to have code that requests a page
- I will then pass the html to BeautifulSoup
- I will extract the page title from the HTML with BeautifulSoup
- I will build this as a small library/module


#### data flow


`Webpage > requests > HTML > BeautifulSoup > ???`


#### data structures


`Webpage as HTML string`

#### algorithms


1. Request the HTML data from the webpage


2. Take the HTML from the response and pass it to BeautifulSoup


#### actions that the object will be able to do


Return the value of the HTML page title.
Not the complete title tag. Just the value

