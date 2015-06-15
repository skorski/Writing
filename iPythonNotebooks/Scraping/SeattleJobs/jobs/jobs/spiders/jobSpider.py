import scrapy as sc
from jobs.items import JobListing
from datetime import datetime
import re

class jobSpider(sc.Spider):
	name = "jobs"
	allowed_domains = ["http://www.indeed.com/", "www.indeed.com"]
	start_urls = [
		"http://www.indeed.com/jobs?q=operations+research&l=seattle%2C+WA",
	]

	def parse(self, response):
		for url in response.xpath('//a/@href').extract():
				yield sc.Request("http://www.indeed.com"+url, callback=self.getJobs)

	def getJobs(self, response):
		results = response.xpath('//div[@itemtype="http://schema.org/JobPosting"]')

		for index, post in enumerate(results):
			posting = JobListing()
			posting['title'] = [ item for item in post.xpath('h2[@class="jobtitle"]/a/@title').extract()]
			posting['description'] = post.xpath('string(.//span[@class="summary"])').extract()[0].replace('\n','')
			posting['jobID'] = post.xpath('.//h2[@class="jobtitle"]/@id').extract()
			posting['scrapeDate'] = datetime.now()
			posting['postAge'] = post.xpath('.//span[@class="date"]/text()').extract()
			posting['company'] = post.xpath('.//span[@class="company"]/span[@itemprop="name"]/text()').extract()
			posting['companyCity'] = post.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
			posting['companyState'] = post.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
			posting['rating'] = post.xpath('.//a/span[@class="ratings"]/span[@class="rating"]/@style').extract()
			posting['detailURL'] = post.xpath('.//h2[@class="jobtitle"]/a/@href').extract()
			yield posting

		for url in response.xpath('//div[@class="pagination"]/a/@href').extract():
			yield sc.Request("http://www.indeed.com"+url, callback=self.getJobs)