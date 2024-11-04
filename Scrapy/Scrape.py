import scrapy

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/programming/top/.json']

    def parse(self, response):
        data = response.json()  # Parse the JSON response
        for post in data['data']['children']:
            yield {
                'title': post['data']['title'],
                'url': post['data']['url'],
                'score': post['data']['score'],
                'comments': post['data']['num_comments'],
            }
        # Pagination logic can be added here if necessary