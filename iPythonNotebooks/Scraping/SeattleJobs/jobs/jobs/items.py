# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

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
