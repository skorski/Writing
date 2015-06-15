[TOC]

# Scrapy Introduction

1. Install scrapy
- conda install scrapy

2. Make the scrapy directory
This is where the spider and the data handlers will be created.  This project cannot be run within iPython notebook because the spiders essentially run on the command line.


# Creating the basic scraper

## The following is required:
1. A website to scrape

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

```python
from scrapy import Spider

class jobSpider(Spider):
    name = "jobs"
    allowed_domains = ["http://www.indeed.com/"]
    start_urls = [
        "http://www.indeed.com/jobs?q=operations+research&l=seattle%2C+WA",
    ]
```

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

Also notice that there is a file that has been created that contains all of the html for that page.  This should be under the jobs jobs/jobs folder.

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

## Testing Selectors

I have found the best way to test these selectors is to start the scrapy shell.  Open up the command line and point scrapy to the root web address.  In this example it is the following:

    scrapy shell "http://www.indeed.com/jobs?q=operations+research&l=seattle%2C+WA"

*note: you must do this in the top level directory of the project*

Once you run the command you should get a listing of output and available objects.

    2015-06-02 08:30:35-0700 [default] DEBUG: Crawled (200) <GET http://www.indeed.com/q-operations-research-l-seattle,-WA-jobs.html> (referer: None)
    [s] Available Scrapy objects:
    [s]   crawler    <scrapy.crawler.Crawler object at 0x104aff490>
    [s]   item       {}
    [s]   request    <GET http://www.indeed.com/jobs?q=operations+research&l=seattle%2C+WA>
    [s]   response   <200 http://www.indeed.com/q-operations-research-l-seattle,-WA-jobs.html>
    [s]   settings   <scrapy.settings.Settings object at 0x104547590>
    [s]   spider     <Spider 'default' at 0x107266450>
    [s] Useful shortcuts:
    [s]   shelp()           Shell help (print this help)
    [s]   fetch(req_or_url) Fetch request (or URL) and update local objects
    [s]   view(response)    View response in a browser 

Our goal here is to query the response with our selector to make sure we will get the correct items when we run the spider.

    response.xpath('//h2[@class=jobtitle]')

When you run this you will notice 10 items were returned.  At first glance this seems right but if we look at the output we notice something is missing.

    In [3]: response.xpath('//h2[@class="jobtitle"]')
    Out[3]: 
    [<Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_14f5c9bc2bc3b340" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_5c15181492f341c5" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_70eed8b81ce334ec" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_f40e7b3c76dd994f" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_ced5550548e5d0f6" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_2b6b7a9261a8a48f" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_30ef81aabd259b43" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_0dec09b1c39c41cf" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_3c8b1bcd141af224" class="jobt'>,
     <Selector xpath='//h2[@class="jobtitle"]' data=u'<h2 id="jl_bdb6c60fcdbb7604" class="jobt'>]

The ID's we referenced at the beginning are not showing up in the selector list.  If you look closer at the page, you'll notice it is the set of sponsored job listings that are missing.  I personally think these are important for our search so I'd like to make sure they get included.

When we go back to the page to look at the source, an interesting difference can be found.

#### Sponsored format
```html
    <div class="row sjlast result" data-jk="a4bafb8b1d8872e6">
    <a target="_blank" id="sja3" class="jobtitle" href="/pagead/clk?mo=r&amp;ad={...}" title="Quality Engineer - Bothell, Washington - 148650" rel="nofollow" onmousedown="sjomd('sja3'); clk('sja3');" onclick="sjoc('sja3',0); convCtr('SJ', pingUrlsForGA)">Quality Engineer - Bothell, Washington - 148650</a>
    ...
    </div>
```

#### Nonsponsored format
```html
    <h2 id="jl_14f5c9bc2bc3b340" class="jobtitle">
    <a rel="nofollow" href="/rc/clk?jk=14f5c9bc2bc3b340" target="_blank" onmousedown="return rclk(this,jobmap[0],0);" onclick="return rclk(this,jobmap[0],true,0);" itemprop="title" title="Logistics Data Scientist, Logistics Strategy - Framingham, MA">Logistics Data Scientist, Logistics Strategy - Framingham, M...</a>
    </h2>
```

Notice how there is a bunch of add information tucked within the sponsored location and the structure is different.  In the non-sponsored area, the structure of `h2[@class=jobtitle]` can be found.  The sponsored link would have to have a selector of `a[@class=jobtitle]`.

We will deal with the sponsored selections later because these might be repeated at the top of many pages and thus throw off our results.

### Extracting the right data

At this point we have a list of selectors from scrapy.  We need to get the actual text within the tag so now we will modify the selector.

The first thing we want to do is convert the pointer to something usable.  This is done by adding `.extract()` to the end of the selector.  

If you do this you will immediately notice that scrapy grabbed all of the html that corresponds with that selector.  Our information is only within the `<a>` tag so we can add that to the selector.

New selector:

    response.xpath('//h2[@class="jobtitle"]/a').extract()

New shell output: 

    In [12]: response.xpath('//h2[@class="jobtitle"]/a').extract()
    Out[12]: 
    [u'<a rel="nofollow" href="/rc/clk?jk=14f5c9bc2bc3b340" target="_blank" onmousedown="return rclk(this,jobmap[0],0);" onclick="return rclk(this,jobmap[0],true,0);" itemprop="title" title="Logistics Data Scientist, Logistics Strategy - Framingham, MA">Logistics Data Scientist, Logistics Strategy - Framingham, M...</a>',
     u'<a rel="nofollow" href="/rc/clk?jk=5c15181492f341c5" target="_blank" onmousedown="return rclk(this,jobmap[1],0);" onclick="return rclk(this,jobmap[1],true,0);" itemprop="title" title="Data Analyst, Operations">Data Analyst, <b>Operations</b></a>', ...]


There is text within the `<a>` tag that could be useful but it also has some junk that we would need to parse out such as the `<b>` tag.  It would be significantly easier if we could grab the title from the tag.

Fortunately, that is something that is relatively straightforward to do by modifying our selector again.

New selector:

    response.xpath('//h2[@class="jobtitle"]/a/@title').extract()

Notice how we can string selector items together.  We wanted the `title` attribute so we simply added @attribute to select it.

At this point, that selector will get us the list of job titles that are not sponsored that appear on the main page.

A detailed explination of xpath selectors can be found [here](http://www.w3schools.com/xpath/xpath_syntax.asp) or [here](http://www.w3schools.com/XPath/default.asp) or [here](http://doc.scrapy.org/en/0.7/topics/selectors.html)

## Integrating the selector

At this point we are going to take a left turn to show how to create an item in scrapy.  An item is what scrapy uses to store scraped information and is simply a python class.  

Within the scrapy directory there will be a file `items.py`.  This file will already contain the following boiler plate:

```python
import scrapy
class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
```

We need to modify this code to store the items we think are interesting.  Adding to many things here is not a bad thing so I'm going to add all of the job attributes I think will be of interest.

```python
import scrapy

class JobListing(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    jobID = scrapy.Field()
    scrapeDate = scrapy.Field()
    postAge = scrapy.Field()
    company = scrapy.Field()
    companyCity = scrapy.Field()
    companyState = scrapy.Field()
    rating = scrapy.Field()
    detailURL = scrapy.Field()
```

Now we can get back to the xpath selector.

Our general path here will be:
1) Find all of the job listing divs
2) Iterate through each of the divs to fill in our JobListing class
3) yield the item so it can be used in the remainder of the scrapy framework

If we go back to the `jobSpider.py` file we can now modify it to work with the selector.

At this point the spider should look like the following:

```python
def parse(self, response):
    results = response.xpath('//div[@itemtype="http://schema.org/JobPosting"]')

    for index, post in enumerate(results):
        print post.xpath('h2[@class="jobtitle"]/a/@title').extract()
```

Notice the second xpath selector does not contain any initial slashes.  This is because it will be appended to the post selector.  Each post selection is a subset of the page so our scraping will run a bit faster.

If this code is run at the command line we should now see a listing of job titles.

The next step is to grab the job titles and other interesting information so we can store it in scrapy item.

I'll go through and add the correct selectors.  Here is what the resulting code will look like:

```python
def parse(self, response):
    results = response.xpath('//div[@itemtype="http://schema.org/JobPosting"]')
    for index, post in enumerate(results):
        posting = JobListing()
        posting['title'] = post.xpath('h2[@class="jobtitle"]/a/@title').extract()[0]
        posting['description'] = post.xpath('span[@class="summary"]/text()').extract()[0]
        posting['jobID'] = post.xpath('h2[@class="jobtitle"]/@id').extract()[0]
        posting['scrapeDate'] = datetime.now()
        posting['postAge'] = post.xpath('span[@class="date"]/text()').extract()[0]
        posting['company'] = post.xpath('span[@class="company"]/span[@itemprop="name"]/text()').extract()[0]
        posting['companyCity'] = post.xpath('span/span/span[@itemprop="addressLocality"]/text()')[0]
        posting['companyState'] = post.xpath('span/span/span[@itemprop="addressLocality"]/text()')[0]
        posting['rating'] = post.xpath('a/span[@class="ratings"]/span[@class="rating"]/@style').extract()[0]
        posting['detailURL'] = post.xpath('h2[@class="jobtitle"]/a/@href').extract()[0]
        yield posting
```

Finding each of these locations involved using the shell in the same way as before.  Load a single page and then iterate through the results selector until you are able to grab the exact item that you want.  

An alternative option that is nearly as good is to make the selections through the dev tools console.  You can make this work by using the console and typing `$x("{selector path}")` where you replace {selector path} with the actual path of the selector.  I have found this can be faster at times but ultimately I like testing in the console at the end to ensure I have what I expect.
![Console xPath Selector](http://i.gyazo.com/5f0019896c81cd68216092aade409d73.gif)

The above code block isn't perfect yet but it will be enough for us to use as we move on.

*notes on the description*
There were a number of additional tags within the description table when rendered by scrapy.  Solving this problem could have taken a few directions.  One option would be to ask scrapy to return all of the text within the span.  This is accomplished with a selector like `.//span[@class="summary"]//text()`.

The double slash here is the universal "find all" for scrapy returns most of what we wanted.

In the end, that wasn't exactly what we wanted so we used a different function `string`.  This converted all of the information in the span to a string before extracting it.  This had the nice benefit of also concatenating the array.  There was one issue with a leading new line that was handled with a simple string replace.

`posting['description'] = post.xpath('string(.//span[@class="summary"])').extract()[0].replace('\n','')`

### Yeilding an Item

If you run the script now you will be able to see the output on the console. To get it into a json file we simply specify an output file with `-o outputFile.json`

## Spanning multiple pages

We now have a gloriously complex scraper that only grabs a single page.  To take full advantage of what we have created we need to change that.  This is a simple change to the parse function.

```python
    for url in response.xpath('//div[@class="pagination"]/a/@href').extract():
        yield sc.Request("http://www.indeed.com"+url, callback=self.parse)
```

This tells the spider to follow all of the links that it finds in the pagination.

## Testing

At this point I run the spider on the command line without dumping the file anywhere.  This is important because I want to see how far the spider gets and also see the data.  According to indeed I should get a little over 2000 jobs from this search.

Look closely at the stats and you will see how many jobs were reported from the spider.
![Job results](http://i.gyazo.com/47f1ff87cb4207ee3ab0e99078f75eae.png)

Fun fact: Even though indeed says there are 2000+ jobs for this search, they are only going to page through the first 1000.

## Scrapy Outout

Once we have the final json file we can begin to play with it, but that will be the subject of a future tutorial.

## References

Writen by Dan Skorski using python and scrapy.

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/javascript"
  src="https://github.com/DmitryBaranovskiy/raphael/raw/master/raphael-min.js">
</script>
<script type="text/javascript"
  src="https://github.com/adrai/flowchart.js/raw/master/release/flowchart-1.2.10.min.js">
</script>





