import scrapy as sc

class jobSpider(sc.Spider):
	name = "jobs"
	allowed_domains = ["http://www.indeed.com/"]
	start_urls = [
		"http://www.indeed.com/jobs?q=operations+research&l=seattle%2C+WA",
	]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
