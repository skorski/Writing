# Scrapy Introduction

1) Install scrapy
- conda install scrapy

2) Make the scrapy directory
This is where the spider and the data handlers will be created.  This project cannot be run within iPython notebook because the spiders essentially run on the command line.


# Creating the basic scraper

## The following is required:
1) A website to scrape

## Scraping the first page

Have scrapy setup the files
'scrapy startproject jobs'

At this point a new directory will be created that will have all of the scrapy files within it.  Scrapy will name your directory whatever you stipulate in the last word.  In this tutorial, we created a folder named jobs.

The directory structure is as follows:

    ├── scrapy.cfg
    └── jobs
        ├── __init__.py
        ├── items.py
        ├── pipelines.py
        ├── settings.py
        └── spiders
            └── __init__.py

We need two things to scrape a page, a crawling spider and a item definition.  First we will start with the spider.

### Creating a spider

First we need to create a new spider file.  We'll name ours 'job_spider.py'.  This will be within the spider directory.

Within that file we need to put in the following code:

    from scrapy import Spider

    class jobSpider(Spider):
        name = "jobs"
        allowed_domains = ["http://www.indeed.com/"]
        start_urls = [
            "http://www.indeed.com/jobs?q=operations+research&l=seattle%2C+WA",
        ]

#### Advanced
We'll come back here and show how to add parameters to the spider that can be called from the command line.

We also need to tell the program how to parse the page:
   
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)


We can run the spider at this point to see that it is actually working.  This is an important step becuase it will ensure the spider is hitting the appropriate web pages.  We can work to parse the pages once we know we are actually getting there.

To run the scraper, go to the root of the scraper directory.  In this case it was ./jobs and run the following command:
    
    scrapy crawl jobs

If all goes well, the command line should show that it crawled a single page.

## Scraping an item

In this example, it is likely that we are going to want to get a listing of all of the jobs that are in the search results.  Perhaps the first two items of interest would be the name of the job and the company that is doing the hiring.

Scrapy will let you grab these items by specififying what is called the xpath.  This sounds complicated but is actually very easy to find using chrome.  
Start up the development tools when you navigate to the page and use the page inspector.  

Go to the position that you are interested in and select id

![Animated](http://i.gyazo.com/91f8ca59cc12dbb085e81ccbe43c4e34.gif)

When I selected the xpath of the first title here is what it shows

    //*[@id="sja1"]

At first glance we could use this as our xPath selector but it is worth digging in a bit at this point.  If we take a minute to look at some of the other ids on the page we'll notice that one is a bit of an anomoly.

| *item name*                          | *ID*                |
|--------------------------------------|---------------------|
| Research Scientist, Personalization  | sja1                |
| Business Analyst                     | sja2                |
| Data Analyst, Operations             | jl_5c15181492f341c5 |

We can quickly see that all of these id's are different so selecting all id's with sja1 is likely to only give us the first sponsored result.  It may be useful to capture the ID name  so we can track these sponsored results but for now we are only trying to see what jobs titles are available given this search.

When we look a bit closer at the html we notice that each of of the titles has an h2 element and a class of jobtitle.  This is something that we can work with.

Let's grab all of the h2 elements that have a class of jobtitle using the following xPath selector
    
    //h2[@class="jobtitle"]

The line above basically asking the parser to give us all h2 elements (regardless of their location) who have a class of jobtitle.

We could modify it to only show the h2 elements that are within the actual results column by chaning the commands
    
    //td[@id="resultscol"]/h2[@class=jobtitle]

Notice there is only a single slash in this example.  This now will not select all of the items on the page, only 

A detailed explination of xpath selectors can be found [here](http://www.w3schools.com/xpath/xpath_syntax.asp) or [here](http://www.w3schools.com/XPath/default.asp)

Now let's modify our spider so we can export that information.  

        for url in response.xpath('//a/@href').extract():
                yield scrapy.Request(url, callback=self.parse)


